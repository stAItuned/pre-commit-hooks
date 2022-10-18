import re
from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error

eq_pattern = r"(\$+)(?:(?!\1)[\s\S])*\1"


def single_entry(entry: Entry) -> Literal[1, 0]:
    post = entry.post
    content = post.content
    eqs = list(re.finditer(eq_pattern, content))
    malformed_eqs = []
    for eq in [e for e in eqs if e.group(0).startswith("$$")]:
        equation = eq.group(0)
        if not(re.search(r"^\$+[ \t]*\n", equation) and re.search(r"\n[ \t]*\$+$", equation)):
            malformed_eqs.append((eq.group(0), eq.span()))
    if len(malformed_eqs) > 0:
        return print_error(entry, f"The following equations are not valid: {malformed_eqs} ", True)
    return ok(entry)


def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors
