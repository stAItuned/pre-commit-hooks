from ..utils import Entry, ok, print_error, filepaths
from os import path, rename
import slugify


def single_entry(dirpath):
    slug: str = path.basename(dirpath)
    clean_slug = slugify.slugify(slug, allow_unicode=True)
    if(slug != clean_slug):
        if path.exists(dirpath.replace(slug, clean_slug)):
            return print_error(
                None, f"Slug is not valid, someone similar already exists ({clean_slug})", True, dirpath)
        rename(dirpath, dirpath.replace(slug, clean_slug))
        print_error(
            None, f"(AUTOFIX) Slug not valid ({slug} => {clean_slug})", True, dirpath)
    ok(filepath=dirpath)


def main():
    for filepath in filepaths:
        single_entry(path.dirname(filepath))
    return 0
