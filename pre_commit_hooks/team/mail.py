import re
from ..utils import Entry, get_frontmatter, ok, print_error

mail_pattern = r"([A-Za-z0-9]+[.-_\+])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"


def single_entry(entry: Entry):
    post = entry.post
    mail: str = post.get("email", "")
    if not re.fullmatch(mail_pattern, mail):
        return print_error(entry, "Mail must be valid", True)
    ok(entry)


def main():
    for entry in get_frontmatter():
        single_entry(entry)
    return 0
