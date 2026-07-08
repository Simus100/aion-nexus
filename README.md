# AION NEXUS

AION NEXUS is the public intelligence interface of Universalis Produzioni: a static-first editorial system that organizes high-signal news and analysis across artificial intelligence, technology, geopolitics, finance, markets, startups, and science.

The project combines automated editorial pipelines, curated public pages, persistent archives, SEO-oriented static publishing, and dedicated long-form report pages. Its goal is to turn fast-moving information flows into a readable, navigable briefing surface for people who need context, priorities, and continuity.

## What AION NEXUS Is

AION NEXUS is not a generic news aggregator. It is an automation-driven editorial observatory designed to:

- collect and structure signals from strategic domains;
- rank and present the most relevant developments;
- maintain a public homepage with a stable editorial layout;
- preserve historical editions and monthly archives;
- publish dedicated AI-generated reports as standalone HTML experiences;
- expose search-engine-friendly static pages, metadata, and sitemap entries.

## Public Experience

The public site is available at:

```text
https://nexus.universalis.it/site/
```

Main sections include:

- `Home`: the current public editorial briefing;
- `Report`: a dedicated archive for standalone AI-generated reports;
- `History`: persistent news history organized over time;
- `Aion Brief`: a focused daily synthesis page;
- static story and report pages with canonical metadata and social previews.

## Key Capabilities

- Static-first frontend for fast public delivery.
- Data-driven editorial homepage powered by JSON files.
- Automated refresh scripts for news, briefs, images, archives, story pages, and sitemap generation.
- Report publishing workflow with canonical URLs, Open Graph metadata, Twitter cards, and JSON-LD.
- Persistent history management with monthly archive files.
- Local validation scripts for safer publishing.
- Lightweight public UI optimized for navigation, readability, and continuity.

## Project Structure

```text
site/      Public frontend, static pages, assets, reports, sitemap, robots.txt
data/      Current edition data, statistics, and historical archives
scripts/   Generation, validation, refresh, archive, and publishing helpers
docs/      Architecture notes, runbooks, rollback guides, and planning documents
```

## Run Locally

From the project root:

```bash
python3 -m http.server 4173
```

Then open:

```text
http://localhost:4173/site/
```

A local server is recommended because the frontend loads JSON files with `fetch()`.

## Useful Commands

```bash
python3 scripts/validate_nexus_json.py
python3 scripts/generate_story_pages.py
python3 scripts/generate_aion_brief_page.py
python3 scripts/enhance_report_seo.py
python3 scripts/generate_sitemap.py
```

## Publishing Notes

For new report pages, place the HTML file under:

```text
site/reports/items/
```

Then run the report SEO enhancer and sitemap generator before publishing:

```bash
python3 scripts/enhance_report_seo.py
python3 scripts/generate_sitemap.py
```

Some optional automation scripts may require environment variables such as `GEMINI_API_KEY`. Never commit API keys, secrets, private credentials, or machine-local configuration files to the repository.

## Repository Description

Suggested public GitHub description:

```text
Automation-driven public intelligence interface by Universalis Produzioni, organizing AI, technology, geopolitics, markets, science, archives, and AI-generated reports into a static-first editorial briefing system.
```
