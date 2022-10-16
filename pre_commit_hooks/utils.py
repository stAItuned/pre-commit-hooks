import frontmatter
import sys
from os import path
from yaml.scanner import ScannerError
from frontmatter import Post
BASE_PATH = path.abspath(".")
filename = sys.argv[1]
filepath = path.join(BASE_PATH, filename)


def get_frontmatter():
    try:
        with open(filepath) as f:
            post = frontmatter.loads(f.read())
        return post
    except ScannerError:
        print_error("Frontmatter not well-written.", True)


def print_error(msg: str, exit: bool = False):
    print(f"'{path.relpath(filepath)}'... {msg}")
    if exit:
        sys.exit(1)


def ok(msg: str = "OK", exit: bool = True):
    print(f"'{path.relpath(filepath)}'... {msg}")
    if exit:
        sys.exit(0)


def rewrite_frontmatter_property(post: Post, key: str, new_value: str):
    with open(filepath, "w") as fd:
        post[key] = new_value
        fd.write(frontmatter.dumps(post))
