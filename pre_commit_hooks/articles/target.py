import sys
from .utils import get_frontmatter, ok, print_error

VALID_TARGETS = ["Newbie", "Midway", "Expert"]

def main():
    post = get_frontmatter()
    target: str = post.get("target", "")
    if not target in VALID_TARGETS:
        print_error(f"Target not valid, must be one of the following: {VALID_TARGETS}")
        return sys.exit(1)
    ok()
