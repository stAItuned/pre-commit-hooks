import frontmatter
import sys
from os import path

def get_frontmatter():
    BASE_PATH = path.abspath(".")
    filename = sys.argv[1]
    filepath = path.join(BASE_PATH, filename)
    with open(filepath) as f:
        post = frontmatter.loads(f.read())
    return post
