import sys
from .utils import get_frontmatter, print_error, filepath
import glob
from os import path
import frontmatter


def get_all_authors() -> list[str]:
    team_path = path.abspath(path.join(filepath, "..", "..", "team"))
    authors_filename = glob.glob("*/*.md", team_path)
    authors_names = []
    for fn in authors_filename:
        with open(fn, "r") as f:
            p = frontmatter.loads(f.read())
            authors_names.append(p.get("name"))
    return author_names


def main():
    post = get_frontmatter()
    author: str = post.get("author", "")
    author_names = get_all_authors()
    if not author in author_names == 0:
        print_error(
            f"Author must exists, {author} doesn't. (List of valid authors: {sorted(author_names)})")
        return sys.exit(1)
    sys.exit(0)
