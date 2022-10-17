from ..utils import Entry, get_frontmatter, ok, print_error

NON_EMPTY_KEYS = ["name", "team", "title", "linkedin", "email", "description"]


def single_entry(entry: Entry):
    post = entry.post
    empty_keys = []

    for key in NON_EMPTY_KEYS:
        if(post.get(key, "") == ""):
            empty_keys.append(key)
    if len(empty_keys) > 0:
        return print_error(entry,
                           f"The following attributes are required in a team card: {', '.join(empty_keys)}", True)
    ok(entry)


def main():
    for entry in get_frontmatter():
        single_entry(entry)
    return 0
