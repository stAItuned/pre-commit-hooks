from .utils import filepath, print_error, filename
import imageio
import sys


def main():
    if filename != "propic.jpg":
        print_error("Propic filename must be propic.jpg")
        return sys.exit(1)
    img = imageio.imread(filepath)
    if img.shape[0] != img.shape[1]:
        print_error(
            f"Team member propic is not a square ({img.shape[0]}x{img.shape[1]})")
        return sys.exit(1)
    sys.exit(0)
