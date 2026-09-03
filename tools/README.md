# Seed Build Tooling

`bootstrap_repo.py` and `catalog_data.py` record the initial curated conversion.
They overwrite generated seed content and require `--force`; do not use them for
normal contributions. Edit canonical packages directly, then run the deterministic
scripts under `scripts/` to rebuild indexes and artifacts.
