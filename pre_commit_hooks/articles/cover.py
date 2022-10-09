from genericpath import isfile
import sys
from .utils import get_frontmatter, print_error, filepath
from os import path
from identify.identify import tags_from_filename

def main():
    post = get_frontmatter()
    cover: str = post.get("cover", "")
    cover_path = path.join(path.dirname(filepath), cover)

    if "image" not in tags_from_filename(cover_path):
        print_error(f"Cover not valid, must be a valid image inside {path.dirname(filepath)} folder")
        return sys.exit(1)
    sys.exit(0)
