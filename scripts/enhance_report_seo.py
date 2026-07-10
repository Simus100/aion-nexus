#!/usr/bin/env python3
import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/root/.openclaw/workspace/aion-nexus')
SITE = ROOT / 'site'
REPORTS_INDEX = SITE / 'reports.html'
REPORT_ITEMS = SITE / 'reports' / 'items'
SITE_URL = 'https://nexus.universalis.it/site'
IMAGE_URL = f'{SITE_URL}/assets/aion-brief-generated.jpg'

SEO_START = '<!-- AION_REPORT_SEO_START -->'
SEO_END = '<!-- AION_REPORT_SEO_END -->'


def strip_tags(value: str) -> str:
    value = re.sub(r'<script\b[^>]*>.*?</script>', '', value, flags=re.IGNORECASE | re.DOTALL)
    value = re.sub(r'<style\b[^>]*>.*?</style>', '', value, flags=re.IGNORECASE | re.DOTALL)
    value = re.sub(r'<[^>]+>', ' ', value)
    return re.sub(r'\s+', ' ', html.unescape(value)).strip()


def first_match(pattern: str, text: str) -> str:
    match = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    return strip_tags(match.group(1)) if match else ''


def report_title(page: Path, text: str) -> str:
    title = first_match(r'<h1\b[^>]*>(.*?)</h1>', text)
    if title:
        return title.replace('Cervello Geopolitico 3D:', '').strip()
    title = first_match(r'<title\b[^>]*>(.*?)</title>', text)
    return title or page.stem.replace('-', ' ').title()


def report_description(text: str) -> str:
    tagline = first_match(r'<p\b[^>]*class=["\'][^"\']*tagline[^"\']*["\'][^>]*>(.*?)</p>', text)
    if tagline:
        return tagline[:300]
    paragraph = first_match(r'<p\b[^>]*>(.*?)</p>', text)
    fallback = paragraph or 'Report AI interattivo pubblicato su AION NEXUS con visualizzazione avanzata e lettura strategica.'
    return fallback[:300]


def iso_or_now(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).astimezone().isoformat(timespec='seconds')


def remove_managed_block(text: str) -> str:
    return re.sub(
        rf'\s*{re.escape(SEO_START)}.*?{re.escape(SEO_END)}\s*',
        '\n',
        text,
        flags=re.DOTALL,
    )


def upsert_title(text: str, title: str) -> str:
    title_tag = f'<title>{html.escape(title)} — AION NEXUS Report</title>'
    if re.search(r'<title\b[^>]*>.*?</title>', text, flags=re.IGNORECASE | re.DOTALL):
        return re.sub(r'<title\b[^>]*>.*?</title>', title_tag, text, count=1, flags=re.IGNORECASE | re.DOTALL)
    return text.replace('<head>', f'<head>\n  {title_tag}', 1)


def insert_head_block(text: str, block: str) -> str:
    text = remove_managed_block(text)
    insertion_points = [
        r'(\s*<title\b[^>]*>.*?</title>\s*)',
        r'(\s*<link\b[^>]*fonts\.googleapis\.com[^>]*>\s*)',
        r'(\s*<meta\b[^>]*viewport[^>]*>\s*)',
    ]
    for pattern in insertion_points:
        if re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL):
            return re.sub(pattern, r'\1' + block + '\n', text, count=1, flags=re.IGNORECASE | re.DOTALL)
    return text.replace('</head>', block + '\n</head>', 1)


def build_report_block(page: Path, title: str, description: str) -> str:
    canonical = f'{SITE_URL}/reports/items/{page.name}'
    payload = {
        '@context': 'https://schema.org',
        '@type': 'Report',
        'mainEntityOfPage': {'@type': 'WebPage', '@id': canonical},
        'headline': title,
        'name': title,
        'description': description,
        'url': canonical,
        'image': [IMAGE_URL],
        'dateModified': iso_or_now(page),
        'inLanguage': 'it-IT',
        'isAccessibleForFree': True,
        'publisher': {
            '@type': 'Organization',
            'name': 'Universalis Produzioni',
            'url': 'https://www.universalis.it/',
            'logo': {'@type': 'ImageObject', 'url': IMAGE_URL},
        },
    }
    esc_title = html.escape(f'{title} — AION NEXUS Report')
    esc_description = html.escape(description)
    escaped_json = json.dumps(payload, ensure_ascii=False).replace('</', '<\\/')
    return f'''  {SEO_START}
  <meta name="description" content="{esc_description}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta property="og:site_name" content="AION NEXUS">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="it_IT">
  <meta property="og:title" content="{esc_title}">
  <meta property="og:description" content="{esc_description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{IMAGE_URL}">
  <meta property="og:image:alt" content="Visual editoriale del report AION NEXUS">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc_title}">
  <meta name="twitter:description" content="{esc_description}">
  <meta name="twitter:image" content="{IMAGE_URL}">
  <link rel="canonical" href="{canonical}">
  <script type="application/ld+json">{escaped_json}</script>
  {SEO_END}'''


def enhance_report_page(page: Path) -> dict:
    text = page.read_text(encoding='utf-8')
    title = report_title(page, text)
    description = report_description(text)
    text = upsert_title(text, title)
    text = insert_head_block(text, build_report_block(page, title, description))
    page.write_text(text, encoding='utf-8')
    return {'title': title, 'description': description, 'path': page}


def build_index_block(reports: list[dict]) -> str:
    description = 'Archivio dei report AI interattivi di AION NEXUS: analisi visuali, simulazioni 3D e letture strategiche pubblicate da Universalis Produzioni.'
    canonical = f'{SITE_URL}/reports.html'
    item_list = [
        {
            '@type': 'ListItem',
            'position': index,
            'url': f"{SITE_URL}/reports/items/{item['path'].name}",
            'name': item['title'],
        }
        for index, item in enumerate(reports, start=1)
    ]
    payload = {
        '@context': 'https://schema.org',
        '@type': 'CollectionPage',
        'name': 'AION NEXUS — Report',
        'description': description,
        'url': canonical,
        'image': [IMAGE_URL],
        'inLanguage': 'it-IT',
        'mainEntity': {'@type': 'ItemList', 'itemListElement': item_list},
        'publisher': {'@type': 'Organization', 'name': 'Universalis Produzioni', 'url': 'https://www.universalis.it/'},
    }
    escaped_json = json.dumps(payload, ensure_ascii=False).replace('</', '<\\/')
    return f'''    {SEO_START}
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <script type="application/ld+json">{escaped_json}</script>
    {SEO_END}'''


def enhance_index(reports: list[dict]) -> None:
    if not REPORTS_INDEX.exists():
        return
    description = 'Archivio dei report AI interattivi di AION NEXUS: analisi visuali, simulazioni 3D e letture strategiche pubblicate da Universalis Produzioni.'
    text = REPORTS_INDEX.read_text(encoding='utf-8')
    text = remove_managed_block(text)
    text = re.sub(
        r'<meta name="description" content="[^"]*" />',
        f'<meta name="description" content="{html.escape(description)}" />',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta name="robots" content="[^"]*" />',
        '<meta name="robots" content="index,follow,max-image-preview:large" />',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta property="og:description" content="[^"]*" />',
        f'<meta property="og:description" content="{html.escape(description)}" />',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta name="twitter:description" content="[^"]*" />',
        f'<meta name="twitter:description" content="{html.escape(description)}" />',
        text,
        count=1,
    )
    text = insert_head_block(text, build_index_block(reports))
    REPORTS_INDEX.write_text(text, encoding='utf-8')


def main() -> None:
    REPORT_ITEMS.mkdir(parents=True, exist_ok=True)
    reports = [enhance_report_page(page) for page in sorted(REPORT_ITEMS.glob('*.html'))]
    enhance_index(reports)
    print(f'Enhanced SEO for {len(reports)} report pages')


if __name__ == '__main__':
    main()
