import sys
from ..utils import get_frontmatter, ok, print_error

CONTENT_LENGTH = 1500

def main():
    post = get_frontmatter()
    content = post.content
    if len(content) < CONTENT_LENGTH:
        print_error(f"Content too short, min {CONTENT_LENGTH} chars (currently {len(content)} chars)")
        return sys.exit(1)
    ok()