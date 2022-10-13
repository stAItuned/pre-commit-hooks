import sys
from .utils import get_frontmatter, ok, print_error


def main():
    post = get_frontmatter()
    linkedin: str = post.get("linkedin", "")
    if not linkedin.startswith("https://www.linkedin.com/in/"):
        print_error("Linkedin url must start with: https://www.linkedin.com/in/", True)
    ok()
