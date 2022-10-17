from ..utils import Entry, get_frontmatter, ok, print_error

TITLE_MAX_LEN = 55


def single_entry(entry: Entry):
    post = entry.post
    title: str = post.get("title", "")
    if len(title) > TITLE_MAX_LEN:
        return print_error(entry, f"Title too long, {len(title)}/{TITLE_MAX_LEN} chars", True)
    ok(entry)


def main():
    for entry in get_frontmatter():
        single_entry(entry)
    return 0
