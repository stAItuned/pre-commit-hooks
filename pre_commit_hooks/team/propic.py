from ..utils import filepath, ok, print_error, filename
import imageio
from os import rename


def main():
    if not filename.endswith("propic.jpg") and not filename.endswith("propic.jpeg"):
        return print_error(f"Propic filename must be propic.jpg", True)

    if filename.endswith("propic.jpeg"):
        new_name = filename.replace("propic.jpg")
        rename(filename, new_name)
        ok("(AUTOFIX) Propic renamed from .jpeg to .jpg", False)

    img = imageio.imread(filepath.replace("propic.jpeg", "propic.jpg"))
    if img.shape[0] != img.shape[1]:
        return print_error(
            f"Team member propic is not a square ({img.shape[0]}x{img.shape[1]})", True)
    ok()
