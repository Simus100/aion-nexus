#!/usr/bin/env python3
import json
import html
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path('/root/.openclaw/workspace/aion-nexus')
NEWS = ROOT / 'data' / 'news.json'
CATEGORIES = ROOT / 'data' / 'categories.json'
OUT = ROOT / 'site' / 'stories'
IMAGE = '/site/assets/aion-brief-generated.jpg'
SITE_URL = 'https://nexus.universalis.it'

VISUAL_CLASS = {
    'ai': 'visual-ai',
    'tech': 'visual-tech',
    'geo': 'visual-geo',
    'fin': 'visual-fin',
    'markets': 'visual-markets',
    'startup': 'visual-startup',
    'science': 'visual-science',
    'future': 'visual-future',
}


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", '-', value)
    return value.strip('-') or 'story'


def story_slug(item: dict) -> str:
    return slugify(item.get('id') or item.get('title') or 'story')


def fmt_date(ts: str) -> str:
    return ts.replace('T', ' ').replace('+01:00', ' CET').replace('+02:00', ' CEST')


def build_aion_opinion(item: dict, category_name: str) -> str:
    tags = [str(tag).strip() for tag in item.get('tags', []) if str(tag).strip()][:3]
    subcategory = str(item.get('subcategory') or '').strip()
    score = int(item.get('qualityScore') or 0)
    category_id = item.get('category')

    category_lens = {
        'ai': 'la partita vera si giochi sulla capacità di trasformare vantaggio tecnico in distribuzione e standard di mercato',
        'tech': 'conti soprattutto il controllo dei passaggi critici dell’infrastruttura e non solo l’annuncio di giornata',
        'geopolitica': 'il punto decisivo sia quanto rapidamente il rischio politico si trasferisce su logistica, energia e prezzi',
        'finanza': 'il mercato stia misurando soprattutto sostenibilità, costo del capitale e credibilità dell’esecuzione',
        'mercati': 'gli operatori stiano prezzando la tenuta del sistema più che il rumore delle singole headline',
        'startup': 'conti meno la narrativa e molto di più la capacità di finanziare crescita, distribuzione e resistenza nel tempo',
        'scienza': 'il valore emerga quando la scoperta mostra una traiettoria concreta verso applicazioni, piattaforme o vantaggi cumulativi',
        'futuro': 'il segnale abbia peso quando anticipa cambiamenti di abitudini, infrastrutture o modelli industriali',
    }
    lens = category_lens.get(category_id, 'la notizia conti soprattutto per ciò che anticipa sulla direzione del contesto')
    intensity = (
        'Se il quadro regge anche nelle prossime ore, questo può diventare un passaggio che riallinea davvero le aspettative.'
        if score >= 93 else
        'Non è ancora una svolta definitiva, ma è il tipo di movimento che cambia il modo in cui il dossier viene letto.'
        if score >= 88 else
        'Per ora vale più come indicatore anticipatore che come svolta pienamente consolidata.'
    )
    subcategory_line = f' Nel perimetro {subcategory.lower()}, Aion legge qui un indizio che va oltre il fatto singolo.' if subcategory else ''
    tag_line = f" I segnali su {', '.join(tags)} suggeriscono che il mercato leggerà questa storia soprattutto come test di tenuta e direzione." if tags else ''
    text = f"Lettura di Aion: sul fronte {category_name.lower()} il punto non è ripetere la cronaca, ma capire se {lens}.{subcategory_line}{tag_line} {intensity}"
    return re.sub(r'\s+', ' ', text).strip()


def render_story(item: dict, category_name: str, all_items: list[dict]) -> str:
    slug = story_slug(item)
    title = html.escape(item['title'])
    description = html.escape(item.get('hook') or item.get('opinion') or '')
    canonical = f"{SITE_URL}/site/stories/{quote(slug)}.html"
    image = f"{SITE_URL}{IMAGE}"
    body_parts = [p.strip() for p in str(item.get('body') or '').split('\n\n') if p.strip()]
    body_html = '\n'.join(f'<p class="story-body">{html.escape(p)}</p>' for p in body_parts)
    tags_html = ''.join(f'<span class="tag-pill">#{html.escape(tag)}</span>' for tag in item.get('tags', []))
    aion_opinion = html.escape(build_aion_opinion(item, category_name))

    related = [x for x in all_items if x.get('id') != item.get('id')][:3]
    related_html = ''.join(
        f'''<a class="related-card" href="./{quote(story_slug(rel))}.html">\n'''
        f'''  <span class="related-kicker">{html.escape(rel.get('category', '').title())}</span>\n'''
        f'''  <strong>{html.escape(rel.get('title', ''))}</strong>\n'''
        f'''  <span>{html.escape(rel.get('hook', ''))}</span>\n'''
        f'''</a>'''
        for rel in related
    )

    source_url = html.escape(item.get('sourceUrl') or '#')
    source_label = html.escape(item.get('sourceLabel') or 'Fonte')
    opinion = html.escape(item.get('opinion') or '')
    visual_class = VISUAL_CLASS.get(item.get('visual'), '')

    return f'''<!doctype html>
<html lang="it">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} — AION NEXUS</title>
    <meta name="description" content="{description}" />
    <meta name="robots" content="index,follow" />
    <meta property="og:site_name" content="AION NEXUS" />
    <meta property="og:type" content="article" />
    <meta property="og:locale" content="it_IT" />
    <meta property="og:title" content="{title} — AION NEXUS" />
    <meta property="og:description" content="{description}" />
    <meta property="og:url" content="{canonical}" />
    <meta property="og:image" content="{image}" />
    <meta property="og:image:alt" content="Visual editoriale di AION NEXUS" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{title} — AION NEXUS" />
    <meta name="twitter:description" content="{description}" />
    <meta name="twitter:image" content="{image}" />
    <link rel="canonical" href="{canonical}" />
    <link rel="stylesheet" href="../assets/styles.css?v=20260326-1849" />
    <style>
      .story-page {{ padding: 24px 0 56px; }}
      .story-page-grid {{ display: grid; gap: 20px; }}
      .story-page-card, .related-card {{
        background: linear-gradient(180deg, rgba(18, 26, 40, 0.96), rgba(13, 20, 33, 0.96));
        border: 1px solid rgba(141, 165, 204, 0.12);
        box-shadow: 0 12px 30px rgba(2, 8, 18, 0.18);
        border-radius: 26px;
      }}
      .story-page-card {{ overflow: hidden; border-color: rgba(141, 165, 204, 0.16); }}
      .story-page-inner {{ width: 100%; margin: 0 auto; padding: 28px 0 34px; }}
      .story-panel-static {{ background: transparent; border: 0; box-shadow: none; border-radius: 0; }}
      .story-back {{ display: inline-flex; width: calc(100% - 64px); max-width: 920px; margin: 0 auto 16px; color: var(--muted); }}
      .related-grid {{ display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 16px; }}
      .related-card {{ padding: 18px; display: grid; gap: 10px; }}
      .related-kicker {{ color: var(--cyan); font-size: .74rem; letter-spacing: .12em; text-transform: uppercase; }}
      .related-card strong {{ line-height: 1.35; }}
      .related-card span:last-child {{ color: var(--muted); font-size: .92rem; line-height: 1.55; }}
      @media (max-width: 800px) {{ .related-grid {{ grid-template-columns: 1fr; }} .story-page-inner {{ width: 100%; padding: 24px 0 32px; }} .story-back {{ width: calc(100% - 32px); }} .story-panel-static .story-title {{ max-width: 15ch; }} }}
    </style>
  </head>
  <body>
    <div class="background-grid"></div>
    <div class="background-glow glow-a"></div>
    <div class="background-glow glow-b"></div>
    <header class="topbar container">
      <div class="brand-block">
        <div class="brand-mark">AION NEXUS</div>
        <div class="brand-sub">Automation Intelligence by Universalis Produzioni</div>
      </div>
      <nav class="topnav">
        <a href="../">Home</a>
        <a href="../history.html">History</a>
      </nav>
    </header>
    <main class="container story-page">
      <div class="story-page-grid">
        <article class="story-page-card">
          <div class="story-hero {visual_class}"></div>
          <div class="story-page-inner">
            <a class="story-back" href="../">← Torna alla homepage</a>
            <article class="story-panel story-panel-static">
              <div class="story-meta">
                <span class="meta-pill">{html.escape(category_name)}</span>
                <span class="meta-pill">{html.escape(item.get('subcategory',''))}</span>
                <span class="meta-pill">{html.escape(fmt_date(item.get('timestamp','')))}</span>
                <span class="meta-pill">{int(item.get('sourceCount', 0))} fonti</span>
              </div>
              <h1 class="story-title">{title}</h1>
              <p class="story-hook">{description}</p>
              <div class="story-tags">{tags_html}</div>
              {body_html}
              <div class="story-footer-row">
                <div class="story-meta">
                  <span class="meta-pill">Fonte: {source_label}</span>
                  <span class="meta-pill">Categoria: {html.escape(category_name)}</span>
                </div>
                <div class="story-meta story-meta-share">
                  <div class="share-actions" aria-label="Condivisione articolo">
                    <button class="source-link story-share-button share-pill-main" type="button" data-copy-link="{html.escape(canonical)}">Copia link</button>
                    <a class="source-link" href="https://wa.me/?text={quote(item['title'] + ' — ' + item.get('hook','') + '\n\n' + canonical)}" target="_blank" rel="noreferrer">WhatsApp</a>
                    <a class="source-link" href="https://t.me/share/url?url={quote(canonical)}&text={quote(item['title'] + ' — ' + item.get('hook',''))}" target="_blank" rel="noreferrer">Telegram</a>
                    <a class="source-link" href="https://www.linkedin.com/sharing/share-offsite/?url={quote(canonical)}" target="_blank" rel="noreferrer">LinkedIn</a>
                    <a class="source-link" href="https://twitter.com/intent/tweet?text={quote(item['title'] + ' — ' + item.get('hook',''))}&url={quote(canonical)}" target="_blank" rel="noreferrer">X</a>
                  </div>
                </div>
              </div>
              <div class="story-footer-row story-footer-source-row">
                <div class="story-meta">
                  <a class="source-link" href="{source_url}" target="_blank" rel="noreferrer">Fonte: {source_label}</a>
                </div>
              </div>
              <div class="story-opinion story-opinion-aion"><strong>L'opinione di Aion</strong><p class="story-body story-body-extended">{aion_opinion}</p></div>
              <div class="story-opinion"><strong>Perché conta</strong><p>{opinion}</p></div>
            </article>
          </div>
        </article>
        <section>
          <div class="section-head compact">
            <div>
              <div class="section-kicker">Altre storie</div>
              <h2>Continua a leggere</h2>
            </div>
          </div>
          <div class="related-grid">{related_html}</div>
        </section>
      </div>
    </main>
    <script>
      document.addEventListener('DOMContentLoaded', function () {{
        function fallbackCopy(text) {{
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
        }}
        document.querySelectorAll('[data-copy-link]').forEach(function (button) {{
          const link = button.getAttribute('data-copy-link');
          button.addEventListener('click', async function () {{
            try {{
              if (navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) {{
                await navigator.clipboard.writeText(link);
              }} else if (!fallbackCopy(link)) {{
                throw new Error('clipboard unavailable');
              }}
              button.textContent = 'Link copiato';
            }} catch (error) {{
              button.textContent = 'Copia fallita';
            }}
            window.setTimeout(function () {{
              button.textContent = 'Copia link';
            }}, 1800);
          }});
        }});
      }});
    </script>
  </body>
</html>
'''


def main():
    news = json.loads(NEWS.read_text(encoding='utf-8'))
    categories = {c['id']: c['name'] for c in json.loads(CATEGORIES.read_text(encoding='utf-8'))}
    OUT.mkdir(parents=True, exist_ok=True)

    generated = 0
    for item in news:
        slug = story_slug(item)
        target = OUT / f'{slug}.html'
        html_text = render_story(item, categories.get(item.get('category'), item.get('category', '')), news)
        target.write_text(html_text, encoding='utf-8')
        generated += 1

    print(f'Generated {generated} story pages in {OUT}')


if __name__ == '__main__':
    main()
