import sys
from ..utils import get_frontmatter, ok, print_error


def main():
    post = get_frontmatter()
    name: str = post.get("name", "no")
    camel = " ".join([a.capitalize() for a in name.split(" ")])
    if name != camel: 
        return print_error("Name must be camel-case", True)
    return ok()
