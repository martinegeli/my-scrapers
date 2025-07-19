"""
Scraper plug‑in package.
Each scraper exposes a single public function:  scrape(out_dir: pathlib.Path) -> None
"""
__all__: list[str] = []     # populated dynamically in runner.py 