from datetime import datetime, timezone
from pathlib import Path
from firecrawl import FirecrawlApp, ScrapeOptions
from bs4 import BeautifulSoup
import json
import re

URL = "https://www.finn.no/bap/browse.html"

def scrape(out_dir: Path) -> None:
    """
    Fetch FINN front page, count the visible listings, save as JSON.
    Called by `runner.py`.
    """
    app = FirecrawlApp()                     # uses FIRECRAWL_API_KEY env var
    html = app.scrape_url(
        URL, scrape_options=ScrapeOptions(formats=["html"])
    )["html"]

    count = len(BeautifulSoup(html, "lxml").select("article, div[data-qa='ad']"))
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # Save as JSON with date-based filename
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    json_path = out_dir / f"{date_str}.json"
    
    data = {
        "date_utc": date_str,
        "count": count,
        "scraped_at": datetime.now(timezone.utc).isoformat(),
        "url": URL
    }
    
    with json_path.open("w") as f:
        json.dump(data, f, indent=2) 