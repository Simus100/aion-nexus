#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone
import xml.etree.ElementTree as ET

ROOT = Path('/root/.openclaw/workspace/aion-nexus')
SITE = ROOT / 'site'
DATA = ROOT / 'data'
SITE_URL = 'https://nexus.universalis.it/site'
NS = 'http://www.sitemaps.org/schemas/sitemap/0.9'
ET.register_namespace('', NS)


def iso_or_now(path: Path) -> str:
    dt = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).astimezone()
    return dt.isoformat(timespec='seconds')


def main():
    news = json.loads((DATA / 'news.json').read_text(encoding='utf-8'))
    stats = json.loads((DATA / 'stats.json').read_text(encoding='utf-8'))
    story_dir = SITE / 'stories'
    story_pages = sorted(story_dir.glob('*.html'))
    report_dir = SITE / 'reports' / 'items'
    report_pages = sorted(report_dir.glob('*.html'))
    news_by_slug = {f"{item['id']}.html": item for item in news if item.get('id')}

    root = ET.Element(f'{{{NS}}}urlset')

    def add_url(loc: str, lastmod: str, changefreq: str, priority: str):
        url = ET.SubElement(root, f'{{{NS}}}url')
        ET.SubElement(url, f'{{{NS}}}loc').text = loc
        ET.SubElement(url, f'{{{NS}}}lastmod').text = lastmod
        ET.SubElement(url, f'{{{NS}}}changefreq').text = changefreq
        ET.SubElement(url, f'{{{NS}}}priority').text = priority

    edition_updated = stats.get('editionUpdatedAt') or iso_or_now(SITE / 'index.html')
    add_url(f'{SITE_URL}/', edition_updated, 'hourly', '1.0')
    add_url(f'{SITE_URL}/history.html', iso_or_now(SITE / 'history.html'), 'daily', '0.7')
    add_url(f'{SITE_URL}/aion-brief.html', iso_or_now(SITE / 'aion-brief.html'), 'daily', '0.8')
    reports_index = SITE / 'reports.html'
    if reports_index.exists():
        add_url(f'{SITE_URL}/reports.html', iso_or_now(reports_index), 'daily', '0.86')

    # Include every static story page; prefer JSON story timestamp when available.
    for page in story_pages:
        item = news_by_slug.get(page.name)
        lastmod = (item or {}).get('timestamp') or iso_or_now(page)
        priority = '0.76' if item and item.get('featured') else '0.72'
        add_url(f'{SITE_URL}/stories/{page.name}', lastmod, 'weekly', priority)

    # Include every published report automatically. New report HTML files placed
    # under site/reports/items/ are picked up by the next refresh/sitemap run.
    for page in report_pages:
        add_url(f'{SITE_URL}/reports/items/{page.name}', iso_or_now(page), 'weekly', '0.82')

    out = SITE / 'sitemap.xml'
    ET.ElementTree(root).write(out, encoding='utf-8', xml_declaration=True)
    print(f'Generated {out} with {len(root.findall(f"{{{NS}}}url"))} URLs')


if __name__ == '__main__':
    main()
