from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error


def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    topics: str = post.get("topics", [])
    if not isinstance(topics, list) or len(topics) == 0:
        return print_error(entry,
                           f"Topics must be an array with at least an element. ({topics} doesn't match the requirements)", True)
    return ok(entry)


def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors

