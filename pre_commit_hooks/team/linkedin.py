import sys
from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error, rewrite_frontmatter_property
import frontmatter
from frontmatter import Post
ERROR_MSG = "Linkedin url must start with https://linkedin.com/in/"





def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    linkedin: str = post.get("linkedin", "")
    if(linkedin.startswith("linkedin.com/")):
        rewrite_frontmatter_property(entry, "linkedin", f"https://www.{linkedin}")
        return print_error(entry, f"(AUTOFIXED) {ERROR_MSG}", True)
    if(linkedin.startswith("www.linkedin.com/")):
        rewrite_frontmatter_property(entry, "linkedin", f"https://{linkedin}")
        return print_error(entry, f"(AUTOFIXED) {ERROR_MSG}", True)
    if not linkedin.startswith("https://www.linkedin.com/in/"):
        return print_error(entry, ERROR_MSG, True)
    return ok(entry)

def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors
