import frontmatter
import sys
from os import path

BASE_PATH = path.abspath(".")
filename = sys.argv[1]
filepath = path.join(BASE_PATH, filename)


def get_frontmatter():
    with open(filepath) as f:
        post = frontmatter.loads(f.read())
    return post


def print_error(msg: str):
    print(f"{filename}\t{msg}")
