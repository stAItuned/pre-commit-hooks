import sys
from ..utils import get_frontmatter, ok, print_error, filepath, rewrite_frontmatter_property
from datetime import date
from os import path
import requests


def main():
    post = get_frontmatter()
    date_str: str = post.get("date", None)
    slug = path.basename(path.dirname(filepath))
    if date_str is None:
        return ok()
    parsed = date(date_str)
    if parsed.year < 1970:
        return ok()
    resp = requests.get("https://staituned.com/sitemap.xml")
    if(slug not in resp.text):
        rewrite_frontmatter_property(post, "date", "")
        print_error(
            f"(AUTOFIXED) Date must not be set if article is not published", exit=True)
    ok()
