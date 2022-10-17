from ..utils import Entry, get_frontmatter, ok, print_error

DESCRIPTION_MAX_LEN = 200


def single_entry(entry: Entry):
    post = entry.post
    description: str = post.get("description", "")
    if len(description) > DESCRIPTION_MAX_LEN:
        return print_error(entry, f"Description too long, {len(description)}/{DESCRIPTION_MAX_LEN} chars", True)
    ok(entry)


def main():
    for entry in get_frontmatter():
        single_entry(entry)
    return 0