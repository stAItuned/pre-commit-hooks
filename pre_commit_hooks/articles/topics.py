from ..utils import get_frontmatter, ok, print_error


def main():
    post = get_frontmatter()
    topics: str = post.get("topics", [])
    if not isinstance(topics, list) or len(topics) == 0:
        return print_error(
            f"Topics must be an array with at least an element. ({topics} doesn't match the requirements)", True)
    ok()
