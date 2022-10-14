import sys
from ..utils import get_frontmatter, ok, print_error

META_MAX_LEN = 160

def main():
    post = get_frontmatter()
    meta: str = post.get("meta", "")
    if len(meta) > META_MAX_LEN:
        print_error(f"Meta length too long, max {META_MAX_LEN} chars")
        return sys.exit(1)
    ok()
