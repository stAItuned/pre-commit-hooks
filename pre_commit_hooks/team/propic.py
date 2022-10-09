from .utils import filepath, print_error
import imageio


def main():
    img = imageio.imread(filepath)
    if img.shape[0] != img.shape[1]:
        print_error(
            f"Team member propic is not a square ({img.shape[0]}x{img.shape[1]})")
