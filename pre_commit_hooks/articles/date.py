from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error
from datetime import date
from os import path
import requests


def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    date_str: str = post.get("date", None)
    # slug = path.basename(path.dirname(entry.filepath))
    if date_str is None:
        return ok(entry)
    if isinstance(date_str, str):
        parsed = date(date_str)
    elif isinstance(date_str, date):
        parsed = date_str
    else:
        return print_error(entry, f"Unable to parse date ({date_str})", True)
    if parsed.year < 1970:
        return ok(entry)
    if post.get("published", None) is None:
        return print_error(entry, "Date attribute should not be set unless it is published")
    return ok(entry)


def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors

