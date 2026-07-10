#!/usr/bin/env python3
import base64
import json
import os
import pathlib
import shutil
import sys
import urllib.request
from datetime import datetime

ROOT = pathlib.Path('/root/.openclaw/workspace/aion-nexus')
NEWS_PATH = ROOT / 'data' / 'news.json'
STATS_PATH = ROOT / 'data' / 'stats.json'
OUT_PATH = ROOT / 'site' / 'assets' / 'aion-brief-generated.jpg'
TMP_PATH = ROOT / 'site' / 'assets' / 'aion-brief-generated.jpg.tmp'
BACKUP_DIR = ROOT / 'tmp' / 'aion-brief-image-history'
MODEL = 'nano-banana-pro-preview'


def load_json(path: pathlib.Path):
    return json.loads(path.read_text())


def build_summary(news, stats):
    news = sorted(news, key=lambda x: (x.get('qualityScore', 0), x.get('timestamp', '')), reverse=True)
    top = news[:3]
    dominant = stats.get('topicEmerging', [])[:4]
    summary = (
        "Le storie più forti del giorno mostrano uno spostamento dall'effetto novità "
        "alla capacità di integrare tecnologie, asset industriali e distribuzione in flussi operativi concreti. "
        "Il mercato premia esecuzione, presidio dei colli di bottiglia e velocità di messa a terra più dei semplici annunci."
    )
    prompt = (
        "Create a premium editorial image that represents Aion's vision of the day in a more human, emotionally legible, and visually engaging way. "
        "This is the visual for an Italian section called 'Sintesi del giorno': it should feel like a human editorial mind making sense of the day, not a cold tech wallpaper. "
        "Show interpretation, convergence, and strategic reading of events, but with warmth, atmosphere, and a subtle sense of presence. "
        "Prefer a semi-figurative editorial scene or evocative symbolic composition over pure abstraction. "
        "If a human presence appears, make it discreet, elegant, and non-specific: a silhouette, a figure seen from behind, hands over papers, or a person facing a map/light/data wall. "
        "No text, no logos, no flags, no ugly sci-fi UI, no chaotic lines, no cyberpunk cliché. "
        f"Daily summary sense: {summary} "
        f"Emerging themes: {', '.join(dominant)}. "
        f"Top stories: {'; '.join(item.get('title', '') for item in top)}. "
        "Visual language: premium magazine illustration or cinematic editorial artwork, dark but attractive, refined, intelligent, human, memorable. "
        "Palette: deep navy, graphite, nuanced cyan and violet accents, with subtle warm highlights to make the image feel more alive. "
        "Composition: one clear focal point, strong hierarchy, restrained depth, horizontal banner. The image should feel like the cover visual of a serious daily briefing with a human point of view."
    )
    return prompt


def generate_image(api_key: str, prompt: str) -> bytes:
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key=' + api_key
    payload = {
        'contents': [{'parts': [{'text': prompt}]}],
        'generationConfig': {'responseModalities': ['TEXT', 'IMAGE']},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
    )
    with urllib.request.urlopen(req, timeout=240) as response:
        data = json.loads(response.read().decode('utf-8'))
    for candidate in data.get('candidates', []):
        for part in candidate.get('content', {}).get('parts', []):
            inline = part.get('inlineData') or part.get('inline_data')
            if inline and inline.get('data'):
                return base64.b64decode(inline['data'])
    raise RuntimeError(f'No image returned by model: {json.dumps(data)[:2000]}')


def main():
    api_key = os.environ.get('GEMINI_API_KEY', '').strip()
    if not api_key:
        raise SystemExit('Missing GEMINI_API_KEY')

    news = load_json(NEWS_PATH)
    stats = load_json(STATS_PATH)
    prompt = build_summary(news, stats)
    image_bytes = generate_image(api_key, prompt)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    if OUT_PATH.exists():
        stamp = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
        shutil.copy2(OUT_PATH, BACKUP_DIR / f'aion-brief-generated-{stamp}.jpg')

    TMP_PATH.write_bytes(image_bytes)
    TMP_PATH.replace(OUT_PATH)
    print(str(OUT_PATH))


if __name__ == '__main__':
    main()
