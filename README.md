# AION NEXUS

AION NEXUS is a public-facing editorial news project built as a static-first site focused on AI, technology, geopolitics, finance, markets, startups, and science.

## What it includes
- public homepage
- in-page focus reading experience
- static story pages
- Aion Brief dedicated page
- history page
- `sitemap.xml`
- `robots.txt`

## Project structure
- `site/` public frontend and generated static pages
- `data/` live edition data and history
- `scripts/` generation and validation scripts
- `docs/` operational and project documentation

## Run locally
From the project root:

```bash
python3 -m http.server 4173
```

Then open:

```text
http://localhost:4173/site/
```

A local server is recommended because the frontend loads JSON files with `fetch()`.

## Useful scripts
```bash
python3 scripts/validate_nexus_json.py
python3 scripts/generate_story_pages.py
python3 scripts/generate_aion_brief_page.py
```

## Notes
Some optional scripts may require environment variables such as `GEMINI_API_KEY`.
Never commit API keys, secrets, or private configuration files to the repository.
