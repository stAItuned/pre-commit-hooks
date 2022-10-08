import sys
from .utils import get_frontmatter


def main():
    post = get_frontmatter()
    name: str = post.get("name", "no")
    camel = " ".join([a.capitalize() for a in name.split(" ")])
    code = 0 if name == camel else 1
    return sys.exit(code)
