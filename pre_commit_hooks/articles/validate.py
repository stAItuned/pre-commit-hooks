from ..utils import get_frontmatter, print_error, ok

NON_EMPTY_KEYS = ["title", "author", "topics",
                  "meta", "target", "language", "cover", "language"]
EMPTY_KEYS = []


def main():
    post = get_frontmatter()
    empty_keys = []
    non_empy = []

    for key in NON_EMPTY_KEYS:
        if(post.get(key, "") == ""):
            empty_keys.append(key)
    for key in EMPTY_KEYS:
        if post.get(key, "") != "":
            non_empy.append(key)
    if len(empty_keys) == 0 and len(non_empy) == 0:
        ok()
    error_msg = ""
    if len(empty_keys) > 0:
        error_msg += f"The following attributes are required: {', '.join(empty_keys)}\n"
    if len(non_empy) > 0:
        error_msg += f"The following attributes are required to be empty: {', '.join(non_empy)}\n"
    return print_error(error_msg, True)
