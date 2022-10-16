from ..utils import filepath, ok, print_error, filename
import imageio
from os import rename


def main():
    if filename.endswith("propic.jpeg"):
        new_name = filename.replace("propic.jpg")
        rename(filename, new_name)
        filename = new_name
        ok("(AUTOFIX) Propic renamed from .jpeg to .jpg", False)

    if not filename.endswith("propic.jpg"):
        return print_error(f"Propic filename must be propic.jpg", True)
    img = imageio.imread(filepath)
    if img.shape[0] != img.shape[1]:
        return print_error(
            f"Team member propic is not a square ({img.shape[0]}x{img.shape[1]})", True)
    ok()
