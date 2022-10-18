from ..utils import ok, print_error, filepaths
from PIL import Image


def single_entry(filepath: str):
    if not filepath.endswith("propic.jpg") and not filepath.endswith("propic.jpeg"):
        return print_error(None, f"Propic filename must be `propic.jpg`", True, filepath)

    if filepath.endswith("propic.jpeg"):
        return print_error(None, msg="Rename from .jpeg to .jpg",
           exit=True, filepath=filepath)

    img = Image.open(filepath)
    width, height = img.width, img.height

    if width != height:
        cropped_img = img.crop((0, 0, min(width, height), min(width, height)))
        img.close()
        ERROR_MSG = f"Team member propic is not a square ({width}x{height})"

        try:
            cropped_img.save(filepath)
            ERROR_MSG = "(AUTOFIX) " + ERROR_MSG
        except:
            pass
        print_error(None, ERROR_MSG, True, filepath)
    ok(filepath=filepath)


def main():
    for filepath in filepaths:
        single_entry(filepath)
    return 0
