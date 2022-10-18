from typing import Literal
from ..utils import ok, print_error, filepaths
from os import path
import slugify


def single_entry(dirpath) -> Literal[1, 0]:
    slug: str = path.basename(dirpath)
    clean_slug = slugify.slugify(slug, allow_unicode=True)
    if(slug != clean_slug):
        if path.exists(dirpath.replace(slug, clean_slug)):
            return print_error(
                None, f"Slug is not valid, someone similar already exists ({clean_slug})", True, dirpath)
        return print_error(
            None, f"Slug not valid (suggested '{clean_slug}')", True, dirpath)
    return ok(filepath=dirpath)


def main():
    errors = 0
    for filepath in filepaths:
        errors += single_entry(path.dirname(filepath))
    return errors
