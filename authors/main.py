#!/usr/bin/python
import sys
from os import path
import frontmatter

BASE_PATH = path.abspath(".")
filename = sys.argv[1]
filepath = path.join(BASE_PATH, filename)
print(filepath)
with open(filepath) as f:
    post = frontmatter.loads(f.read())
    print(post)
sys.exit(1)
