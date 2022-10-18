from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error, filepaths
import glob
from os import path
import frontmatter


def get_all_authors() -> list[str]:
    team_path = path.abspath(
        path.join(path.dirname(filepaths[0]), "..", "..", "team"))
    authors_filename = [path.join(team_path, a)
                        for a in glob.glob("*/*.md", root_dir=team_path)]
    authors_names = []
    for fn in authors_filename:
        try:
            with open(fn, "r") as f:
                p = frontmatter.loads(f.read())
                authors_names.append(p.get("name"))
        except:
            pass
    return authors_names


author_names = get_all_authors()


def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    author: str = post.get("author", "")
    if author not in author_names:
        return print_error(entry,
                           f"Author must exists, {author} doesn't. (List of valid authors: {sorted(author_names)})", True)
    return ok(entry)


def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors
