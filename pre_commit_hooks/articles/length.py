from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error

CONTENT_LENGTH = 1500


def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    content = post.content
    if len(content) < CONTENT_LENGTH:
        return print_error(entry, f"Content too short, {len(content)}/{CONTENT_LENGTH} chars", True)
    return ok(entry)


def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors

