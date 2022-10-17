from ..utils import Entry, get_frontmatter, ok, print_error
from os import path
from identify.identify import tags_from_filename
from urllib.parse import urlparse


def single_entry(entry: Entry):
    post = entry.post
    cover: str = post.get("cover", "")
    cover_path = path.join(path.dirname(entry.filepath), cover)
    if(urlparse(cover).netloc):
        return ok(entry)
    if "image" not in tags_from_filename(cover_path) or not path.isfile(cover_path):
        return print_error(
            entry, f"Cover not valid, must be a valid image inside '{path.dirname(path.relpath(entry.filepath))}' folder ('{cover_path}' not valid)")
    return ok(entry)


def main():
    for entry in get_frontmatter():
        single_entry(entry)
    return 0
