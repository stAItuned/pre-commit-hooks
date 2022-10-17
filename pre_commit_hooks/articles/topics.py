from ..utils import Entry, get_frontmatter, ok, print_error


def single_entry(entry: Entry):
    post = entry.post
    topics: str = post.get("topics", [])
    if not isinstance(topics, list) or len(topics) == 0:
        return print_error(entry,
                           f"Topics must be an array with at least an element. ({topics} doesn't match the requirements)", True)
    ok(entry)


def main():
    for entry in get_frontmatter():
        single_entry(entry)
    return 0
