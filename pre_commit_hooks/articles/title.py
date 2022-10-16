import sys
from ..utils import get_frontmatter, ok, print_error

TITLE_MAX_LEN = 55

def main():
    post = get_frontmatter()
    title: str = post.get("title", "")
    if len(title) > TITLE_MAX_LEN:
        return print_error(f"Title too long, {len(title)}/{TITLE_MAX_LEN} chars", True)
    ok()