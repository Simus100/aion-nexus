#!/usr/bin/env python3
import json
import html
from pathlib import Path

ROOT = Path('/root/.openclaw/workspace/aion-nexus')
NEWS = ROOT / 'data' / 'news.json'
STATS = ROOT / 'data' / 'stats.json'
CATEGORIES = ROOT / 'data' / 'categories.json'
OUT = ROOT / 'site' / 'aion-brief.html'
SITE_URL = 'https://nexus.universalis.it'
IMAGE = f'{SITE_URL}/site/assets/aion-brief-generated.jpg'

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


def fmt(ts: str) -> str:
    return ts.replace('T', ' ').replace('+01:00', ' CET').replace('+02:00', ' CEST')


def main():
    news = json.loads(NEWS.read_text(encoding='utf-8'))
    stats = json.loads(STATS.read_text(encoding='utf-8'))
    categories = {c['id']: c['name'] for c in json.loads(CATEGORIES.read_text(encoding='utf-8'))}

    sorted_news = sorted(news, key=lambda x: ((x.get('qualityScore') or 0), x.get('timestamp') or ''), reverse=True)
    top = sorted_news[:3]
    latest = sorted(news, key=lambda x: x.get('timestamp') or '', reverse=True)[0] if news else None
    lead = top[0] if top else None
    lead_category = categories.get(lead.get('category'), lead.get('category')) if lead else 'AION NEXUS'
    score_spread = [x.get('qualityScore') or 0 for x in top]
    strong_execution_theme = 'Esecuzione operativa e distribuzione' if any(score >= 90 for score in score_spread) else 'Riposizionamento competitivo'
    watchpoint = 'Trasferimento del rischio geopolitico su energia e mercati' if len(top) > 1 and top[1].get('category') == 'geopolitica' else 'Capacità di trasformare annuncio in adozione reale'
    freshness = stats.get('editionUpdatedAt') or (latest.get('timestamp') if latest else '')

    summary = (
        "Il quadro di oggi è più interessante per convergenza che per singola headline. "
        "Le storie più forti mostrano che il baricentro si sta spostando dall'effetto novità alla capacità di integrare tecnologie, asset industriali e distribuzione in flussi operativi concreti. "
        f"Letti insieme, {top[0]['title'] if len(top) > 0 else 'il tema principale'}, {top[1]['title'] if len(top) > 1 else 'il secondo segnale'} e {top[2]['title'] if len(top) > 2 else 'il terzo fronte'} raccontano un mercato che premia esecuzione, presidio dei colli di bottiglia e velocità di messa a terra più dei semplici annunci."
    ) if top else 'Sintesi del giorno in aggiornamento.'

    related = ''.join(
        f'''<a class="related-card" href="./stories/{html.escape(item['id'])}.html">'''
        f'''<span class="related-kicker">{html.escape(categories.get(item.get('category'), item.get('category','')))}</span>'''
        f'''<strong>{html.escape(item.get('title',''))}</strong>'''
        f'''<span>{html.escape(item.get('hook',''))}</span></a>'''
        for item in top
    )

    html_text = f'''<!doctype html>
<html lang="it">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Aion Brief — Sintesi del giorno — AION NEXUS</title>
    <meta name="description" content="{html.escape(summary[:280])}" />
    <meta name="robots" content="index,follow" />
    <meta property="og:site_name" content="AION NEXUS" />
    <meta property="og:type" content="article" />
    <meta property="og:locale" content="it_IT" />
    <meta property="og:title" content="Aion Brief — Sintesi del giorno — AION NEXUS" />
    <meta property="og:description" content="{html.escape(summary[:280])}" />
    <meta property="og:url" content="{SITE_URL}/site/aion-brief.html" />
    <meta property="og:image" content="{IMAGE}" />
    <meta property="og:image:alt" content="Visual editoriale dell'Aion Brief" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Aion Brief — Sintesi del giorno — AION NEXUS" />
    <meta name="twitter:description" content="{html.escape(summary[:280])}" />
    <meta name="twitter:image" content="{IMAGE}" />
    <link rel="canonical" href="{SITE_URL}/site/aion-brief.html" />
    <link rel="stylesheet" href="./assets/styles.css?v=20260326-1849" />
    <style>
      .brief-page {{ padding: 24px 0 56px; }}
      .brief-card, .related-card {{ background: linear-gradient(180deg, rgba(18, 26, 40, 0.96), rgba(13, 20, 33, 0.96)); border: 1px solid rgba(141, 165, 204, 0.12); box-shadow: 0 12px 30px rgba(2, 8, 18, 0.18); border-radius: 26px; }}
      .brief-card {{ padding: 28px; display: grid; gap: 18px; justify-items: center; }}
      .brief-image {{ width: 100%; display: block; border-radius: 20px; border: 1px solid rgba(141, 165, 204, 0.14); }}
      .brief-share {{ display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; }}
      .brief-title {{ max-width: 16ch; margin: 0; text-align: center; }}
      .brief-meta {{ justify-content: center; }}
      .brief-summary {{ max-width: 76ch; text-align: center; margin: 0; }}
      .brief-grid {{ display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 14px; }}
      .brief-mini {{ display: grid; gap: 8px; padding: 16px 18px; border-radius: 18px; background: rgba(255,255,255,0.025); border: 1px solid rgba(141, 165, 204, 0.12); }}
      .brief-mini span {{ color: var(--muted); font-size: .74rem; letter-spacing: .12em; text-transform: uppercase; }}
      .related-grid {{ display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 16px; margin-top: 20px; }}
      .related-card {{ padding: 18px; display: grid; gap: 10px; }}
      .related-kicker {{ color: var(--cyan); font-size: .74rem; letter-spacing: .12em; text-transform: uppercase; }}
      .related-card span:last-child {{ color: var(--muted); font-size: .92rem; line-height: 1.55; }}
      @media (max-width: 800px) {{ .brief-grid, .related-grid {{ grid-template-columns: 1fr; }} }}
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
        <a href="./">Home</a>
        <a href="./history.html">History</a>
      </nav>
    </header>
    <main class="container brief-page">
      <article class="brief-card">
        <div class="section-kicker">Aion Brief</div>
        <h1 class="story-title brief-title">Sintesi del giorno</h1>
        <div class="story-meta brief-meta">
          <span class="meta-pill">Segnale dominante: {html.escape(lead_category)}</span>
          <span class="meta-pill">Aggiornato {html.escape(fmt(freshness))}</span>
        </div>
        <img class="brief-image" src="./assets/aion-brief-generated.jpg" alt="Visual editoriale dell'Aion Brief" />
        <p class="story-hook brief-summary">{html.escape(summary)}</p>
        <div class="brief-grid">
          <div class="brief-mini"><span>Segnale dominante</span><strong>{html.escape(lead_category)}</strong></div>
          <div class="brief-mini"><span>Tema principale</span><strong>{html.escape(strong_execution_theme)}</strong></div>
          <div class="brief-mini"><span>Cosa osservare</span><strong>{html.escape(watchpoint)}</strong></div>
        </div>
        <div class="brief-share">
          <button class="source-link" type="button" id="copy-brief-link">Copia link</button>
          <a class="source-link" href="https://wa.me/?text={html.escape('Aion Brief — Sintesi del giorno\n\n' + SITE_URL + '/site/aion-brief.html')}" target="_blank" rel="noreferrer">WhatsApp</a>
          <a class="source-link" href="https://t.me/share/url?url={SITE_URL}/site/aion-brief.html&text=Aion%20Brief%20%E2%80%94%20Sintesi%20del%20giorno" target="_blank" rel="noreferrer">Telegram</a>
          <a class="source-link" href="https://www.linkedin.com/sharing/share-offsite/?url={SITE_URL}/site/aion-brief.html" target="_blank" rel="noreferrer">LinkedIn</a>
          <a class="source-link" href="https://twitter.com/intent/tweet?text=Aion%20Brief%20%E2%80%94%20Sintesi%20del%20giorno&url={SITE_URL}/site/aion-brief.html" target="_blank" rel="noreferrer">X</a>
        </div>
      </article>
      <section class="section-block" style="padding-top: 26px;">
        <div class="section-head compact">
          <div>
            <div class="section-kicker">Top stories</div>
            <h2>Le storie che guidano la sintesi</h2>
          </div>
        </div>
        <div class="related-grid">{related}</div>
      </section>
    </main>
    <script>
      document.addEventListener('DOMContentLoaded', function () {{
        const button = document.getElementById('copy-brief-link');
        const briefUrl = 'https://nexus.universalis.it/site/aion-brief.html';
        if (!button) return;
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
        button.addEventListener('click', async function () {{
          try {{
            if (navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) {{
              await navigator.clipboard.writeText(briefUrl);
            }} else if (!fallbackCopy(briefUrl)) {{
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
    </script>
  </body>
</html>
'''
    OUT.write_text(html_text, encoding='utf-8')
    print(f'Generated {OUT}')


if __name__ == '__main__':
    main()
