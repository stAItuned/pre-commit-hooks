import sys
from .utils import get_frontmatter, print_error, filepath
import glob
from os import path
import frontmatter


def get_all_authors() -> list[str]:
    team_path = path.abspath(path.join(path.dirname(filepath), "..", "..", "team"))
    authors_filename = [path.join(team_path, a) for a in glob.glob("*/*.md", root_dir=team_path)]
    authors_names = []
    for fn in authors_filename:
        with open(fn, "r") as f:
            p = frontmatter.loads(f.read())
            authors_names.append(p.get("name"))
    return authors_names


def main():
    post = get_frontmatter()
    author: str = post.get("author", "")
    author_names = get_all_authors()
    if author not in author_names:
        print_error(
            f"Author must exists, {author} doesn't. (List of valid authors: {sorted(author_names)})")
        return sys.exit(1)
    sys.exit(0)
