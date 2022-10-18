from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error, rewrite_frontmatter_property

ERROR_MSG = "Name must be camel-case"


def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    name: str = post.get("name", "no")
    camel = " ".join([a.capitalize() for a in name.split(" ")])
    if name != camel:
        rewrite_frontmatter_property(entry, "name", camel)
        return print_error(entry, f"(AUTOFIXED) {ERROR_MSG}", True)
    return ok(entry)


def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors
