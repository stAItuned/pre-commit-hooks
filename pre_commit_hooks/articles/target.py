from ..utils import Entry, get_frontmatter, ok, print_error, rewrite_frontmatter_property

VALID_TARGETS = ["Newbie", "Midway", "Expert"]
ERROR_MSG = f"Target not valid, must be one of the following: {VALID_TARGETS}"


def single_entry(entry: Entry):
    post = entry.post
    target: str = post.get("target", "")
    if target.lower() == target and target.capitalize() in VALID_TARGETS:
        rewrite_frontmatter_property(entry, "target", target.capitalize())
        return print_error(entry, f"(AUTOFIXED) {ERROR_MSG}", True)
    if not target in VALID_TARGETS:
        return print_error(entry, ERROR_MSG, True)
    ok(entry)


def main():
    for entry in get_frontmatter():
        single_entry(entry)
    return 0
