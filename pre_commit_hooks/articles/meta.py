import sys
from ..utils import get_frontmatter, ok, print_error

META_MAX_LEN = 160

def main():
    post = get_frontmatter()
    meta: str = post.get("meta", "")
    if len(meta) > META_MAX_LEN:
        return print_error(f"Meta too long, {len(meta)}/{META_MAX_LEN} chars", True)
    ok()
