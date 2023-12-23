from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error, rewrite_frontmatter_property

VALID_TARGETS = ["Newbie", "Midway", "Expert"]
ERROR_MSG = f"Target not valid, must be one of the following: {VALID_TARGETS}"


def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    target: str = post.get("target", "")
    if target.lower() == target and target.capitalize() in VALID_TARGETS:
        rewrite_frontmatter_property(entry, "target", target.capitalize())
        return print_error(entry, f"(AUTOFIXED) {ERROR_MSG}", True)
    if not target in VALID_TARGETS:
        return print_error(entry, ERROR_MSG, True)
    return ok(entry)


def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors
