#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ALLOWED_CATEGORIES = {"ai", "tech", "geopolitica", "finanza", "mercati", "startup", "scienza", "futuro"}
ALLOWED_VISUALS = {"ai", "tech", "geo", "fin", "markets", "startup", "science", "future"}
REQUIRED_KEYS = {
    "id", "category", "subcategory", "title", "hook", "body", "tags",
    "sourceLabel", "sourceUrl", "sourceCount", "timestamp", "featured",
    "opinion", "qualityScore", "visual"
}

def fail(msg: str):
    print(msg, file=sys.stderr)
    raise SystemExit(1)

def main():
    if len(sys.argv) != 3:
        fail("usage: validate_nexus_json.py <news.json> <stats.json>")
    news_path = Path(sys.argv[1])
    stats_path = Path(sys.argv[2])
    news = json.loads(news_path.read_text())
    stats = json.loads(stats_path.read_text())
    if not isinstance(news, list):
        fail("news.json is not a JSON array")
    if not isinstance(stats, dict):
        fail("stats.json is not a JSON object")
    for i, item in enumerate(news):
        missing = REQUIRED_KEYS - set(item.keys())
        if missing:
            fail(f"news[{i}] missing keys: {sorted(missing)}")
        if item["category"] not in ALLOWED_CATEGORIES:
            fail(f"news[{i}] invalid category: {item['category']}")
        if item["visual"] not in ALLOWED_VISUALS:
            fail(f"news[{i}] invalid visual: {item['visual']}")
        if not isinstance(item["tags"], list):
            fail(f"news[{i}] tags is not a list")
    print("OK")

if __name__ == "__main__":
    main()
