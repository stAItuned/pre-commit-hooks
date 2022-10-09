import sys, re
from .utils import get_frontmatter, print_error
from urllib.parse import urlparse
# ![Rete Generativa Avversaria](./Untitled.png)

eq_pattern = r"(\$+)(?:(?!\1)[\s\S])*\1"

def main():
    post = get_frontmatter()
    content = post.content
    eqs = list(re.finditer(eq_pattern, content))
    malformed_eqs = []
    for eq in [e for e in eqs if e.group(0).startswith("$$")]:
        equation = eq.group(0)
        if not (equation.startswith("$$\n") and re.search(r"\n[ \t]*\$+$", equation)):
            malformed_eqs.append((eq.group(0), eq.span()))
    if len(malformed_eqs) > 0:
        print_error(f"The following equations are not valid: {malformed_eqs} ", True)
    sys.exit(0)