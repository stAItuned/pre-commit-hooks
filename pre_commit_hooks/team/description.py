from ..utils import get_frontmatter, ok, print_error

DESCRIPTION_MAX_LEN = 200


def main():
    post = get_frontmatter()
    description: str = post.get("description", "")
    if len(description) > DESCRIPTION_MAX_LEN:
        return print_error(f"Description too long, {len(description)}/{DESCRIPTION_MAX_LEN} chars", True)
    ok()
