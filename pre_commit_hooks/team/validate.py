from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error

NON_EMPTY_KEYS = ["name", "team", "title", "linkedin", "email", "description"]


def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    empty_keys = []

    for key in NON_EMPTY_KEYS:
        if(post.get(key, "") == ""):
            empty_keys.append(key)
    if len(empty_keys) > 0:
        return print_error(entry,
                           f"The following attributes are required in a team card: {', '.join(empty_keys)}", True)
    return ok(entry)


def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors
