import sys
import re
from ..utils import get_frontmatter, ok, print_error, filepath
from urllib.parse import urlparse
from os import path

img_pattern = r"!\[.*\]\((.*)\)"


def main():
    post = get_frontmatter()
    content = post.content
    urls = re.findall(img_pattern, content)
    malformed_urls = []
    for url in urls:
        parsed = urlparse(url)
        if parsed.netloc:  # if it's an external url consider it valid
            continue
        # otherwise it must be local
        basepath = path.dirname(filepath)
        imgpath = path.join(basepath, url)
        if not path.isfile(imgpath):
            malformed_urls.append(url)
    if len(malformed_urls) > 0:
        return print_error(
            f"The following images are not valid: {malformed_urls} ", True)
    ok()