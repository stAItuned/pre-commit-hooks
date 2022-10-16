import sys
from ..utils import get_frontmatter, ok, print_error, filepath, rewrite_frontmatter_property
import frontmatter
from frontmatter import Post
ERROR_MSG = "Linkedin url must start with https://linkedin.com/in/"





def main():
    post = get_frontmatter()
    linkedin: str = post.get("linkedin", "")
    if(linkedin.startswith("linkedin.com/")):
        rewrite_frontmatter_property(post, "linkedin", f"https://www.{linkedin}")
        print_error(f"(AUTOFIXED) {ERROR_MSG}", True)
    if(linkedin.startswith("www.linkedin.com/")):
        rewrite_frontmatter_property(post, "linkedin", f"https://{linkedin}")
        print_error(f"(AUTOFIXED) {ERROR_MSG}", True)
    if not linkedin.startswith("https://www.linkedin.com/in/"):
        print_error(ERROR_MSG, True)
    ok()
