import sys
from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error

VALID_LANGUAGES = ["Italian", "English"]


def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    language: str = post.get("language", "")
    if not language in VALID_LANGUAGES:
        return print_error(entry, f"Language not valid, must be one of the following: {VALID_LANGUAGES}", True)
    return ok(entry)


def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors
