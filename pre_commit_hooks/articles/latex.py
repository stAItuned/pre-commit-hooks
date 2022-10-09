import sys, re
from .utils import get_frontmatter, print_error
from urllib.parse import urlparse
# ![Rete Generativa Avversaria](./Untitled.png)

eq = r"(\$+)(?:(?!\1)[\s\S])*\1"

def main():
    post = get_frontmatter()
    content = post.content
    eqs = list(re.finditer(eq, content))
    malformed_eqs = []
    for eq in [eq for eq in eqs if eq.group(0).startswith("$$")]:
        if not (eq.group(0).startswith("$$\n") and eq.group(0).endswith("\n$$")):
            malformed_eqs.append((eq.group(0), eq.span()))
    if len(malformed_eqs) > 0:
        print_error(f"The following equations are not valid: {malformed_eqs} ", True)
    sys.exit(0)
