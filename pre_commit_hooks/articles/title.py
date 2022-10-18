from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error

TITLE_MAX_LEN = 55


def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    title: str = post.get("title", "")
    if len(title) > TITLE_MAX_LEN:
        return print_error(entry, f"Title too long, {len(title)}/{TITLE_MAX_LEN} chars", True)
    return ok(entry)


def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors
