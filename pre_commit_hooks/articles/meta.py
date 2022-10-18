import sys
from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error

META_MAX_LEN = 160

def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    meta: str = post.get("meta", "")
    if len(meta) > META_MAX_LEN:
        return print_error(entry, f"Meta too long, {len(meta)}/{META_MAX_LEN} chars", True)
    return ok(entry)

def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors
