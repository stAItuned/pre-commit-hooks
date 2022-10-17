import frontmatter
import sys
from os import path
from yaml.scanner import ScannerError
from frontmatter import Post
from dataclasses import dataclass
from rich.console import Console
from rich.text import Text

BASE_PATH = path.abspath(".")
filenames = sys.argv[1:]
filepaths = [path.join(BASE_PATH, filename) for filename in filenames]

console = Console()
print = console.print


@dataclass
class Entry:
    filepath: str
    post: Post


def get_frontmatter() -> list[Entry]:
    posts: list[Entry] = []
    for filepath in filepaths:
        try:
            with open(filepath) as f:
                post = frontmatter.loads(f.read())
                posts.append(Entry(filepath, post))
        except ScannerError:
            print_error("Frontmatter not well-written.", True)
    return posts


def print_error(entry: Entry = None, msg: str = ":cross_mark:", exit: bool = True, filepath: str = None):
    if filepath is not None:
        filepath = path.relpath(filepath)
    if entry is not None:
        filepath = path.relpath(entry.filepath)
    if filepath is None:
        filepath = ""
    print(f"[red]'{filepath}'... [bold]{msg}")
    if exit:
        sys.exit(1)
    return 1


def ok(entry: Entry = None, msg: str = ":white_check_mark:", exit: bool = True, filepath: str = None):
    if filepath is not None:
        filepath = path.relpath(filepath)
    if entry is not None:
        filepath = path.relpath(entry.filepath)
    if filepath is None:
        filepath = ""
    print(f"[green]'{filepath}'... {msg}")
    if exit:
        # sys.exit(0)
        pass


def rewrite_frontmatter_property(entry: Entry, key: str, new_value: str):
    with open(entry.filepath, "w") as fd:
        entry.post[key] = new_value
        fd.write(frontmatter.dumps(entry.post))
