import sys
import re
from ..utils import get_frontmatter, ok, print_error

mail_pattern = r"([A-Za-z0-9]+[.-_\+])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"


def main():
    post = get_frontmatter()
    mail: str = post.get("email", "")
    if not re.fullmatch(mail_pattern, mail):
        print_error("Mail must be valid", True)
    ok()
