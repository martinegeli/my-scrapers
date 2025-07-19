import importlib, sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python runner.py <module_name>")
    module_name = sys.argv[1]
    mod = importlib.import_module(f"scrapers.{module_name}")
    out_dir = Path("data") / module_name
    mod.scrape(out_dir)

if __name__ == "__main__":
    main() 