import sys
from .utils import get_frontmatter, print_error, filepath
from datetime import date
from os import path
import requests


def main():
    post = get_frontmatter()
    date_str: str = post.get("date", "")
    slug = path.basename(path.dirname(filepath))
    if date_str == "" or date_str is None:
        sys.exit(0)
    parsed = date(date_str)
    if parsed.year < 1970:
        sys.exit(0)
    resp = requests.get("https://staituned.com/sitemap.xml")
    if(slug not in resp.text):
        print_error(
            f"Date must not be set if article is not published", exit=True)
    sys.exit(0)
