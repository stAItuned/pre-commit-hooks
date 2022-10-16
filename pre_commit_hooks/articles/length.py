from ..utils import get_frontmatter, ok, print_error

CONTENT_LENGTH = 1500

def main():
    post = get_frontmatter()
    content = post.content
    if len(content) < CONTENT_LENGTH:
        return print_error(f"Content too short, {len(content)}/{CONTENT_LENGTH} chars", True)
    ok()