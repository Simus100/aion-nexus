const categoriesUrl = '../../data/categories.json';
const historyIndexUrl = '../../data/history/index.json';

const visualClassMap = {
  ai: 'visual-ai',
  tech: 'visual-tech',
  geo: 'visual-geo',
  fin: 'visual-fin',
  markets: 'visual-markets',
  startup: 'visual-startup',
  science: 'visual-science',
  future: 'visual-future',
};

function storyPageSlug(storyId) {
  return String(storyId || 'story')
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '') || 'story';
}

function storyPageUrl(item) {
  if (!item?.id) return window.location.href;
  return new URL(`./stories/${storyPageSlug(item.id)}.html`, window.location.href).toString();
}

function historyItemUrl(item) {
  const url = new URL(window.location.href);
  if (item?.id) {
    url.searchParams.set('story', item.id);
  }
  return url.toString();
}

function hasDedicatedStoryPage(item) {
  if (!item?.id) return false;
  const ts = String(item.timestamp || '');
  return ts >= '2026-03-26T19:05:00+01:00';
}

function shareUrlForItem(item) {
  return hasDedicatedStoryPage(item) ? storyPageUrl(item) : historyItemUrl(item);
}

function fallbackCopyText(text) {
  const temp = document.createElement('textarea');
  temp.value = text;
  temp.setAttribute('readonly', '');
  temp.style.position = 'absolute';
  temp.style.left = '-9999px';
  document.body.appendChild(temp);
  temp.select();
  temp.setSelectionRange(0, temp.value.length);
  const ok = document.execCommand('copy');
  document.body.removeChild(temp);
  return ok;
}

function bindCopyButtons(scope = document) {
  scope.querySelectorAll('[data-copy-link]').forEach((button) => {
    if (button.dataset.copyBound === 'true') return;
    button.dataset.copyBound = 'true';
    const link = button.dataset.copyLink;
    const defaultLabel = button.dataset.copyLabel || 'Copia link';
    button.addEventListener('click', async () => {
      try {
        if (navigator.clipboard?.writeText && window.isSecureContext) {
          await navigator.clipboard.writeText(link);
        } else if (!fallbackCopyText(link)) {
          throw new Error('clipboard unavailable');
        }
        button.textContent = 'Link copiato';
      } catch (error) {
        button.textContent = 'Copia fallita';
      }
      window.setTimeout(() => {
        button.textContent = defaultLabel;
      }, 1800);
    });
  });
}

async function fetchJson(url) {
  const response = await fetch(url, { cache: 'no-store' });
  if (!response.ok) throw new Error(`HTTP ${response.status} for ${url}`);
  return response.json();
}

function fmtDate(ts) {
  const d = new Date(ts);
  return d.toLocaleString('it-IT', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' });
}

function byTimestampDesc(a, b) {
  return new Date(b.timestamp) - new Date(a.timestamp);
}

function sourceLink(item) {
  return item.sourceUrl
    ? `<a class="source-link" href="${item.sourceUrl}" target="_blank" rel="noreferrer">Vai alla fonte</a>`
    : '';
}

function renderDetail(item, category) {
  const host = document.getElementById('history-detail');
  const hasShare = hasDedicatedStoryPage(item);
  const shareUrl = shareUrlForItem(item);
  const shareText = `${item.title} — ${item.hook || ''}`.trim();
  const paragraphs = String(item.body || '')
    .split(/\n\n+/)
    .map((paragraph) => paragraph.trim())
    .filter(Boolean)
    .map((paragraph) => `<p class="story-body">${paragraph}</p>`)
    .join('');

  host.innerHTML = `
    <div class="history-detail-body">
      <div class="story-hero ${visualClassMap[item.visual] || ''}"></div>
      <div class="story-meta">
        <span class="meta-pill">${category?.name || item.archivedCategoryName || item.category}</span>
        <span class="meta-pill">${item.subcategory || 'Archivio'}</span>
        <span class="meta-pill">${fmtDate(item.timestamp)}</span>
        <span class="meta-pill">${item.sourceLabel || 'Fonte'}</span>
      </div>
      <h3 class="story-title">${item.title}</h3>
      <p class="story-hook">${item.hook || ''}</p>
      <div class="story-tags">${(item.tags || []).map((tag) => `<span class="tag-pill">#${tag}</span>`).join('')}</div>
      ${paragraphs}
      <div class="story-footer-row">
        <div class="story-meta">
          <span class="meta-pill">Fonte: ${item.sourceLabel || '—'}</span>
          <span class="meta-pill">Categoria: ${category?.name || item.archivedCategoryName || item.category}</span>
        </div>
        <div class="story-meta story-meta-share">
          ${hasShare ? `
            <button class="source-link share-pill-main" type="button" data-copy-link="${shareUrl}" data-copy-label="Copia link">Copia link</button>
            <a class="source-link" href="https://wa.me/?text=${encodeURIComponent(`${shareText}\n\n${shareUrl}`)}" target="_blank" rel="noreferrer">WhatsApp</a>
            <a class="source-link" href="https://t.me/share/url?url=${encodeURIComponent(shareUrl)}&text=${encodeURIComponent(shareText)}" target="_blank" rel="noreferrer">Telegram</a>
            <a class="source-link" href="https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(shareUrl)}" target="_blank" rel="noreferrer">LinkedIn</a>
            <a class="source-link" href="https://twitter.com/intent/tweet?text=${encodeURIComponent(shareText)}&url=${encodeURIComponent(shareUrl)}" target="_blank" rel="noreferrer">X</a>
          ` : ''}
          ${sourceLink(item)}
        </div>
      </div>
      ${item.opinion ? `<div class="story-opinion"><strong>Perché conta</strong><p>${item.opinion}</p></div>` : ''}
    </div>
  `;

  bindCopyButtons(host);
}

function renderMonthChips(months, activeKey) {
  const host = document.getElementById('history-months');
  if (!host) return;
  host.innerHTML = months.map((month) => `
    <button class="history-month-chip ${month.key === activeKey ? 'active' : ''}" type="button" data-key="${month.key}" data-file="${month.file}">
      <span>${month.label}</span>
      <strong>${month.count}</strong>
    </button>
  `).join('');
}

function renderSidebar(categories, news) {
  const host = document.getElementById('history-sidebar');
  const grouped = Object.fromEntries(categories.map((category) => [
    category.id,
    news.filter((item) => item.category === category.id).sort(byTimestampDesc),
  ]));

  host.innerHTML = categories.map((category, idx) => {
    const items = grouped[category.id] || [];
    return `
      <section class="history-category" data-id="${category.id}">
        <button class="history-category-head" type="button">
          <span>
            <strong>${category.name}</strong>
            <small>${items.length} notizie disponibili</small>
          </span>
          <span class="history-category-chevron">▾</span>
        </button>
        <div class="history-list">
          ${items.length ? items.map((item) => `
            <article class="history-item" data-id="${item.id}">
              <div class="history-item-top">
                <span class="meta-pill">${fmtDate(item.timestamp)}</span>
                <span class="meta-pill">${item.sourceLabel || 'Fonte'}</span>
              </div>
              <h3>${item.title}</h3>
              <p>${item.hook || ''}</p>
            </article>
          `).join('') : '<div class="history-item"><p>Nessuna notizia in questa categoria.</p></div>'}
        </div>
      </section>
    `;
  }).join('');

  host.querySelectorAll('.history-category-head').forEach((button) => {
    button.addEventListener('click', () => {
      button.parentElement.classList.toggle('open');
    });
  });

  host.querySelectorAll('.history-item').forEach((node) => {
    node.addEventListener('click', () => {
      const item = news.find((entry) => entry.id === node.dataset.id);
      if (!item) return;
      const category = categories.find((entry) => entry.id === item.category);
      host.querySelectorAll('.history-item').forEach((el) => el.classList.remove('active'));
      node.classList.add('active');
      renderDetail(item, category);
      const url = new URL(window.location.href);
      url.searchParams.set('story', item.id);
      window.history.replaceState({ story: item.id }, '', url.toString());
      document.getElementById('history-detail')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  const requestedStoryId = new URL(window.location.href).searchParams.get('story');
  const first = (requestedStoryId ? news.find((entry) => entry.id === requestedStoryId) : null) || news.slice().sort(byTimestampDesc)[0];
  if (first) {
    const firstNode = host.querySelector(`.history-item[data-id="${first.id}"]`);
    if (firstNode) {
      firstNode.classList.add('active');
      firstNode.closest('.history-category')?.classList.add('open');
    }
    renderDetail(first, categories.find((entry) => entry.id === first.category));
  } else {
    const detail = document.getElementById('history-detail');
    if (detail) detail.innerHTML = '<div class="history-empty">Nessuna notizia archiviata per questo mese.</div>';
  }
}

async function loadMonth(categories, month) {
  const payload = await fetchJson(month.file);
  renderSidebar(categories, payload);
}

Promise.all([fetchJson(categoriesUrl), fetchJson(historyIndexUrl)])
  .then(async ([categories, index]) => {
    const months = index.months || [];
    if (!months.length) {
      const detail = document.getElementById('history-detail');
      if (detail) detail.innerHTML = '<div class="history-empty">Archivio mensile non ancora disponibile.</div>';
      return;
    }
    const requestedStoryId = new URL(window.location.href).searchParams.get('story');
    let active = months[0];
    if (requestedStoryId) {
      for (const month of months) {
        try {
          const payload = await fetchJson(month.file);
          if (Array.isArray(payload) && payload.some((item) => item.id === requestedStoryId)) {
            active = month;
            break;
          }
        } catch (error) {
          console.warn('Failed to inspect history month', month.file, error);
        }
      }
    }
    renderMonthChips(months, active.key);
    await loadMonth(categories, active);
    document.getElementById('history-months')?.querySelectorAll('.history-month-chip').forEach((button) => {
      button.addEventListener('click', async () => {
        const key = button.dataset.key;
        const month = months.find((entry) => entry.key === key);
        if (!month) return;
        document.querySelectorAll('.history-month-chip').forEach((el) => el.classList.remove('active'));
        button.classList.add('active');
        await loadMonth(categories, month);
      });
    });
  })
  .catch((error) => {
    const host = document.getElementById('history-detail');
    if (host) {
      host.innerHTML = `<div class="history-empty">Impossibile caricare la pagina history.<br /><small>${error.message}</small></div>`;
    }
  });
