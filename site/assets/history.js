const categoriesUrl = '../../data/categories.json';
const historyIndexUrl = '../../data/history/index.json';
const DESKTOP_INITIAL_ITEMS_PER_CATEGORY = 12;
const MOBILE_INITIAL_ITEMS_PER_CATEGORY = 3;
const DESKTOP_LOAD_MORE_STEP = 12;
const MOBILE_LOAD_MORE_STEP = 6;
const MOBILE_BREAKPOINT = 900;

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

const monthCache = new Map();
const groupedCache = new Map();
let currentCategories = [];
let currentNews = [];
let currentVisibleByCategory = new Map();
let currentRequestedStoryId = null;
let currentActiveMonthKey = null;
let currentActiveStoryId = null;
let currentOpenCategoryId = null;
let latestCategories = [];
let latestIndex = null;
let currentMedia = null;

function isMobileView() {
  return window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT}px)`).matches;
}

function initialItemsPerCategory() {
  return isMobileView() ? MOBILE_INITIAL_ITEMS_PER_CATEGORY : DESKTOP_INITIAL_ITEMS_PER_CATEGORY;
}

function loadMoreStep() {
  return isMobileView() ? MOBILE_LOAD_MORE_STEP : DESKTOP_LOAD_MORE_STEP;
}

function shouldSmoothScroll() {
  return !isMobileView() && !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}

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

async function fetchMonth(month) {
  const files = Array.isArray(month?.files) && month.files.length ? month.files : (month?.file ? [month.file] : []);
  if (!files.length) return [];
  const cacheKey = files.join('|');
  if (monthCache.has(cacheKey)) return monthCache.get(cacheKey);
  const payloads = await Promise.all(files.map((file) => fetchJson(file)));
  const payload = payloads.flat();
  monthCache.set(cacheKey, payload);
  return payload;
}

function groupedByCategory(categories, news) {
  const cacheKey = `${currentActiveMonthKey || 'month'}:${news.length}`;
  if (groupedCache.has(cacheKey)) return groupedCache.get(cacheKey);
  const grouped = Object.fromEntries(categories.map((category) => [
    category.id,
    news.filter((item) => item.category === category.id).sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp)),
  ]));
  groupedCache.set(cacheKey, grouped);
  return grouped;
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

function historyItemMarkup(item) {
  return `
    <article class="history-item" data-id="${item.id}">
      <div class="history-item-top">
        <span class="meta-pill">${fmtDate(item.timestamp)}</span>
        <span class="meta-pill">${item.sourceLabel || 'Fonte'}</span>
      </div>
      <h3>${item.title}</h3>
      <p>${item.hook || ''}</p>
    </article>
  `;
}

function getVisibleCount(categoryId, itemsLength) {
  const fallback = initialItemsPerCategory();
  const current = currentVisibleByCategory.get(categoryId) || fallback;
  return Math.min(current, itemsLength);
}

function renderCategoryList(section, items, categoryId) {
  const list = section.querySelector('.history-list');
  if (!list) return;
  const visible = getVisibleCount(categoryId, items.length);
  const shown = items.slice(0, visible);
  const hasMore = items.length > shown.length;
  const step = loadMoreStep();
  list.innerHTML = shown.length
    ? `${shown.map(historyItemMarkup).join('')}${hasMore ? `<button class="history-load-more source-link" type="button" data-category="${categoryId}">Mostra altri ${Math.min(step, items.length - shown.length)}</button>` : ''}`
    : '<div class="history-item"><p>Nessuna notizia in questa categoria.</p></div>';
}

function ensureOpenCategoryVisibility() {
  if (currentOpenCategoryId && currentCategories.some((category) => category.id === currentOpenCategoryId)) {
    return;
  }
  const grouped = groupedByCategory(currentCategories, currentNews);
  const firstWithItems = currentCategories.find((category) => (grouped[category.id] || []).length > 0);
  currentOpenCategoryId = firstWithItems?.id || currentCategories[0]?.id || null;
}

function syncOpenCategories() {
  const host = document.getElementById('history-sidebar');
  if (!host) return;
  ensureOpenCategoryVisibility();
  host.querySelectorAll('.history-category').forEach((section) => {
    const isOpen = section.dataset.id === currentOpenCategoryId;
    section.classList.toggle('open', isOpen);
  });
}

function setOpenCategory(categoryId) {
  if (!categoryId) return;
  currentOpenCategoryId = categoryId;
  if (isMobileView()) {
    const grouped = groupedByCategory(currentCategories, currentNews);
    const section = document.getElementById('history-sidebar')?.querySelector(`.history-category[data-id="${categoryId}"]`);
    if (section) renderCategoryList(section, grouped[categoryId] || [], categoryId);
  }
  syncOpenCategories();
}

function activateItem(itemId, options = {}) {
  const item = currentNews.find((entry) => entry.id === itemId);
  if (!item) return;
  currentActiveStoryId = item.id;
  const host = document.getElementById('history-sidebar');
  const category = currentCategories.find((entry) => entry.id === item.category);
  const grouped = groupedByCategory(currentCategories, currentNews);
  const categoryItems = grouped[item.category] || [];
  const itemIndex = categoryItems.findIndex((entry) => entry.id === item.id);
  if (itemIndex >= 0) {
    const baseVisible = initialItemsPerCategory();
    const requiredVisible = Math.max(baseVisible, itemIndex + 1);
    if ((currentVisibleByCategory.get(item.category) || baseVisible) < requiredVisible) {
      currentVisibleByCategory.set(item.category, requiredVisible);
      const section = host?.querySelector(`.history-category[data-id="${item.category}"]`);
      if (section) renderCategoryList(section, categoryItems, item.category);
    }
  }
  setOpenCategory(item.category);
  host?.querySelectorAll('.history-item').forEach((el) => el.classList.remove('active'));
  const node = host?.querySelector(`.history-item[data-id="${item.id}"]`);
  if (node) {
    node.classList.add('active');
    if (options.scrollSidebar && !isMobileView()) {
      node.scrollIntoView({ block: 'nearest' });
    }
  }
  renderDetail(item, category);
  const url = new URL(window.location.href);
  url.searchParams.set('story', item.id);
  window.history.replaceState({ story: item.id }, '', url.toString());
  if (options.scrollDetail) {
    document.getElementById('history-detail')?.scrollIntoView({ behavior: shouldSmoothScroll() ? 'smooth' : 'auto', block: 'start' });
  }
}

function initializeVisibleCounts(categories, grouped) {
  const baseVisible = initialItemsPerCategory();
  currentVisibleByCategory = new Map(categories.map((category) => {
    const items = grouped[category.id] || [];
    return [category.id, Math.min(baseVisible, items.length)];
  }));
}

function renderSidebar(categories, news) {
  const host = document.getElementById('history-sidebar');
  currentCategories = categories;
  currentNews = news;
  const grouped = groupedByCategory(categories, news);
  initializeVisibleCounts(categories, grouped);

  host.innerHTML = categories.map((category) => {
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
        <div class="history-list"></div>
      </section>
    `;
  }).join('');

  const first = (currentRequestedStoryId ? news.find((entry) => entry.id === currentRequestedStoryId) : null) || news.slice().sort(byTimestampDesc)[0];
  if (first) {
    currentOpenCategoryId = first.category;
    categories.forEach((category) => {
      const section = host.querySelector(`.history-category[data-id="${category.id}"]`);
      if (section && (!isMobileView() || category.id === currentOpenCategoryId)) {
        renderCategoryList(section, grouped[category.id] || [], category.id);
      }
    });
    if (!isMobileView() || currentRequestedStoryId) {
      activateItem(first.id, { scrollSidebar: false, scrollDetail: false });
    } else {
      syncOpenCategories();
      const detail = document.getElementById('history-detail');
      if (detail) detail.innerHTML = '<div class="history-empty">Scegli una notizia dallo storico per aprire il dettaglio.</div>';
    }
  } else {
    ensureOpenCategoryVisibility();
    syncOpenCategories();
    const detail = document.getElementById('history-detail');
    if (detail) detail.innerHTML = '<div class="history-empty">Nessuna notizia archiviata per questo mese.</div>';
  }
  syncOpenCategories();
}

async function loadMonth(categories, month) {
  currentActiveMonthKey = month?.key || null;
  const payload = await fetchMonth(month);
  renderSidebar(categories, payload);
}

async function bootstrap() {
  const [categories, index] = await Promise.all([fetchJson(categoriesUrl), fetchJson(historyIndexUrl)]);
  latestCategories = categories;
  latestIndex = index;
  const months = index.months || [];
  if (!months.length) {
    const detail = document.getElementById('history-detail');
    if (detail) detail.innerHTML = '<div class="history-empty">Archivio mensile non ancora disponibile.</div>';
    return;
  }
  currentRequestedStoryId = new URL(window.location.href).searchParams.get('story');
  let active = months[0];
  if (currentRequestedStoryId && index.storyToMonth?.[currentRequestedStoryId]) {
    active = months.find((month) => month.key === index.storyToMonth[currentRequestedStoryId]) || active;
  }
  renderMonthChips(months, active.key);
  await loadMonth(categories, active);

  document.getElementById('history-months')?.querySelectorAll('.history-month-chip').forEach((button) => {
    button.addEventListener('click', async () => {
      const key = button.dataset.key;
      const month = months.find((entry) => entry.key === key);
      if (!month) return;
      currentRequestedStoryId = new URL(window.location.href).searchParams.get('story');
      document.querySelectorAll('.history-month-chip').forEach((el) => el.classList.remove('active'));
      button.classList.add('active');
      await loadMonth(categories, month);
    });
  });

  const sidebar = document.getElementById('history-sidebar');
  sidebar?.addEventListener('click', (event) => {
    const head = event.target.closest('.history-category-head');
    if (head) {
      const categoryId = head.parentElement.dataset.id;
      if (isMobileView()) {
        const parent = head.parentElement;
        const isAlreadyOpen = parent.classList.contains('open');
        if (isAlreadyOpen) {
          const grouped = groupedByCategory(currentCategories, currentNews);
          const firstWithItems = currentCategories.find((category) => category.id !== categoryId && (grouped[category.id] || []).length > 0);
          setOpenCategory(firstWithItems?.id || categoryId);
        } else {
          setOpenCategory(categoryId);
        }
      } else {
        head.parentElement.classList.toggle('open');
      }
      return;
    }

    const loadMore = event.target.closest('.history-load-more');
    if (loadMore) {
      const categoryId = loadMore.dataset.category;
      const current = currentVisibleByCategory.get(categoryId) || initialItemsPerCategory();
      currentVisibleByCategory.set(categoryId, current + loadMoreStep());
      const grouped = groupedByCategory(currentCategories, currentNews);
      const section = sidebar.querySelector(`.history-category[data-id="${categoryId}"]`);
      if (section) {
        renderCategoryList(section, grouped[categoryId] || [], categoryId);
        setOpenCategory(categoryId);
      }
      return;
    }

    const itemNode = event.target.closest('.history-item[data-id]');
    if (itemNode) {
      activateItem(itemNode.dataset.id, { scrollSidebar: false, scrollDetail: true });
    }
  });

  currentMedia = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT}px)`);
  const mediaHandler = () => {
    if (!latestCategories || !currentNews.length) return;
    groupedCache.clear();
    renderSidebar(latestCategories, currentNews);
    if (currentActiveStoryId) {
      activateItem(currentActiveStoryId, { scrollSidebar: false, scrollDetail: false });
    }
  };
  if (currentMedia.addEventListener) {
    currentMedia.addEventListener('change', mediaHandler);
  } else if (currentMedia.addListener) {
    currentMedia.addListener(mediaHandler);
  }
}

bootstrap().catch((error) => {
  const host = document.getElementById('history-detail');
  if (host) {
    host.innerHTML = `<div class="history-empty">Impossibile caricare la pagina history.<br /><small>${error.message}</small></div>`;
  }
});
