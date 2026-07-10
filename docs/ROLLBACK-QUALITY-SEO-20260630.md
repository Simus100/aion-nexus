# Rollback qualità articoli e SEO - 2026-06-30

Questo intervento è stato tenuto separato dalla logica di refresh e selezione notizie. I backup puntuali sono in:

- `backups/manual-style-fixes/generate_story_pages.py.pre-quality-seo-20260630-200134.bak`
- `backups/manual-style-fixes/generate_aion_brief_page.py.pre-quality-seo-20260630-200134.bak`
- `backups/manual-style-fixes/run_nexus_refresh_local.sh.pre-quality-seo-20260630-200134.bak`
- `backups/manual-style-fixes/generate_sitemap.py.pre-quality-seo-20260630-200134.bak`
- `backups/manual-style-fixes/styles.css.pre-quality-seo-20260630-200134.bak`
- `backups/manual-style-fixes/app.js.pre-quality-seo-20260630-200134.bak`
- `backups/manual-style-fixes/index.html.pre-quality-seo-20260630-200134.bak`

## Ripristino manuale

```bash
cd /root/.openclaw/workspace/aion-nexus
cp backups/manual-style-fixes/generate_story_pages.py.pre-quality-seo-20260630-200134.bak scripts/generate_story_pages.py
cp backups/manual-style-fixes/generate_aion_brief_page.py.pre-quality-seo-20260630-200134.bak scripts/generate_aion_brief_page.py
cp backups/manual-style-fixes/run_nexus_refresh_local.sh.pre-quality-seo-20260630-200134.bak scripts/run_nexus_refresh_local.sh
cp backups/manual-style-fixes/generate_sitemap.py.pre-quality-seo-20260630-200134.bak scripts/generate_sitemap.py
cp backups/manual-style-fixes/styles.css.pre-quality-seo-20260630-200134.bak site/assets/styles.css
cp backups/manual-style-fixes/app.js.pre-quality-seo-20260630-200134.bak site/assets/app.js
cp backups/manual-style-fixes/index.html.pre-quality-seo-20260630-200134.bak site/index.html
python3 scripts/generate_story_pages.py
python3 scripts/generate_aion_brief_page.py
python3 scripts/generate_sitemap.py
```

## Ripristino con script

```bash
cd /root/.openclaw/workspace/aion-nexus
bash scripts/rollback_quality_seo_20260630.sh
```

Lo script rigenera anche story pages, Aion Brief e sitemap dopo il ripristino dei file sorgente.
