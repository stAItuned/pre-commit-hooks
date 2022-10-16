from ..utils import get_frontmatter, ok, print_error, rewrite_frontmatter_property

ERROR_MSG = "Name must be camel-case"

def main():
    post = get_frontmatter()
    name: str = post.get("name", "no")
    camel = " ".join([a.capitalize() for a in name.split(" ")])
    if name != camel: 
        rewrite_frontmatter_property(post, "name", camel)
        return print_error(f"(AUTOFIXED) {ERROR_MSG}", True)
    return ok()
