from ..utils import ok, print_error, filepaths
import imageio
from os import rename


def single_entry(filepath: str):
    if not filepath.endswith("propic.jpg") and not filepath.endswith("propic.jpeg"):
        return print_error(None, f"Propic filename must be propic.jpg", True, filepath)

    if filepath.endswith("propic.jpeg"):
        new_name = filepath.replace("propic.jpg")
        rename(filepath, new_name)
        ok(msg="(AUTOFIX) Propic renamed from .jpeg to .jpg",
           exit=False, filepath=filepath)

    img = imageio.imread(filepath.replace("propic.jpeg", "propic.jpg"))
    if img.shape[0] != img.shape[1]:
        return print_error(None,
                           f"Team member propic is not a square ({img.shape[0]}x{img.shape[1]})", exit=True, filepath=filepath)
    ok(filepath=filepath)


def main():
    for filepath in filepaths:
        single_entry(filepath)
    return 0
