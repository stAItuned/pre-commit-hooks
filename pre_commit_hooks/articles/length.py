from ..utils import Entry, get_frontmatter, ok, print_error

CONTENT_LENGTH = 1500


def single_entry(entry: Entry):
    post = entry.post
    content = post.content
    if len(content) < CONTENT_LENGTH:
        return print_error(entry, f"Content too short, {len(content)}/{CONTENT_LENGTH} chars", True)
    ok(entry)


def main():
    for entry in get_frontmatter():
        single_entry(entry)
    return 0
