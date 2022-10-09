import sys
import re
from .utils import get_frontmatter

DESCRIPTION_MAX_LEN = 200

def main():
    post = get_frontmatter()
    description: str = post.get("description", "")
    if len(description) > DESCRIPTION_MAX_LEN:
        print(f"Description length too long, max {DESCRIPTION_MAX_LEN} chars")
        return sys.exit(1)
    sys.exit(0)
