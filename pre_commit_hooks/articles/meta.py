import sys
from ..utils import Entry, get_frontmatter, ok, print_error

META_MAX_LEN = 160

def single_entry(entry: Entry):
    post = entry.post
    meta: str = post.get("meta", "")
    if len(meta) > META_MAX_LEN:
        return print_error(entry, f"Meta too long, {len(meta)}/{META_MAX_LEN} chars", True)
    ok(entry)

def main():
    for entry in get_frontmatter():
        single_entry(entry)
    return 0
