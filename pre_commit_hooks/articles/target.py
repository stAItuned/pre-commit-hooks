from ..utils import get_frontmatter, ok, print_error, rewrite_frontmatter_property

VALID_TARGETS = ["Newbie", "Midway", "Expert"]
ERROR_MSG = f"Target not valid, must be one of the following: {VALID_TARGETS}"


def main():
    post = get_frontmatter()
    target: str = post.get("target", "")
    if target.capitalize() in VALID_TARGETS:
        rewrite_frontmatter_property(post, "target", target.capitalize())
        return print_error(f"(AUTOFIXED) {ERROR_MSG}", True)
    if not target in VALID_TARGETS:
        return print_error(ERROR_MSG, True)
    ok()
