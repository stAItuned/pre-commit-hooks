from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error

DESCRIPTION_MAX_LEN = 200


def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    description: str = post.get("description", "")
    if len(description) > DESCRIPTION_MAX_LEN:
        return print_error(entry, f"Description too long, {len(description)}/{DESCRIPTION_MAX_LEN} chars", True)
    return ok(entry)


def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors
