import sys
from .utils import get_frontmatter, ok, print_error

NON_EMPTY_KEYS = ["name", "team", "title", "linkedin", "email", "description"]


def main():
    post = get_frontmatter()
    empty_keys = []

    for key in NON_EMPTY_KEYS:
        if(post.get(key, "") == ""):
            empty_keys.append(key)
    if len(empty_keys) > 0:
        return print_error(
            f"The following attributes are required in a team card: {', '.join(empty_keys)}", True)
    ok()
