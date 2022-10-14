import sys
from ..utils import get_frontmatter, ok, print_error

VALID_LANGUAGES = ["Italian", "English"]

def main():
    post = get_frontmatter()
    language: str = post.get("language", "")
    if not language in VALID_LANGUAGES:
        print_error(f"Language not valid, must be one of the following: {VALID_LANGUAGES}")
        return sys.exit(1)
    ok()
