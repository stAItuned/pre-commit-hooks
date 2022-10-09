import sys
import re
from .utils import get_frontmatter

NON_EMPTY_KEYS = ["name", "team", "title", "linkedin", "email", "description"]


def main():
    post = get_frontmatter()
    empty_keys = []

    for key in NON_EMPTY_KEYS:
        if(post.get(key, "") == ""):
            empty_keys.append(key)
    if len(empty_keys) > 0:
        print(
            f"The following attributes are required in a team card: {', '.join(empty_keys)}")
        return sys.exit(1)
    sys.exit(0)
