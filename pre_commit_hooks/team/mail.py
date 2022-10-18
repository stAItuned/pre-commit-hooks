import re
from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error

mail_pattern = r"([A-Za-z0-9]+[.-_\+])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"


def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    mail: str = post.get("email", "")
    if not re.fullmatch(mail_pattern, mail):
        return print_error(entry, "Mail must be valid", True)
    return ok(entry)


def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors
