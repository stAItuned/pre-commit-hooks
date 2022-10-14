from ..utils import filepath, ok, print_error, filename
import imageio
import sys


def main():
    if not filename.endswith("propic.jpg"):
        print_error(f"Propic filename must be propic.jpg")
        return sys.exit(1)
    img = imageio.imread(filepath)
    if img.shape[0] != img.shape[1]:
        print_error(
            f"Team member propic is not a square ({img.shape[0]}x{img.shape[1]})", True)
    ok()
