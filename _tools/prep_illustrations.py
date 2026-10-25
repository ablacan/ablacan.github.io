"""Prepare a black & white drawing for the website.

What it does:
  1. makes the white background around the drawing transparent
     (only the background touching the image borders: the white inside
     the drawing, e.g. a sweater or a sheet of paper, stays white),
  2. crops the empty margins,
  3. resizes to at most 600 x 900 px and saves a light WebP file
     in assets/img/illustrations/.

Usage (from the repository folder):
  python3 _tools/prep_illustrations.py                         # redo every drawing listed in DRAWINGS below
  python3 _tools/prep_illustrations.py my_drawing.jpeg teaching   # one drawing -> assets/img/illustrations/teaching.webp

Then use it in a page front matter:
  illustration: /assets/img/illustrations/teaching.webp

Needs Python with Pillow (pip install pillow).
"""
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw

REPO = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO / "_images_examples"          # original drawings
OUTPUT_DIR = REPO / "assets" / "img" / "illustrations"

# Original file (in SOURCE_DIR) -> name of the website image (without .webp)
DRAWINGS = {
    "main_illustration.png": "home",
    "papers_illustration.png": "papers",
    "cv_illustration.jpeg": "cv",
    "teaching_illustration.jpeg": "teaching",
    "presentation_illustration_1.png": "talk",
    "presentation_illustration_2.png": "talk-front",
}

MAX_SIZE = (600, 900)   # max width, height in pixels
MARGIN = 12             # pixels kept around the drawing after cropping
TOLERANCE = 60          # how far from pure white still counts as background (JPEG noise)


def prepare(source: Path, name: str) -> None:
    im = Image.open(source).convert("RGB")
    w, h = im.size

    # Paint the background reachable from the borders with a marker colour.
    marker = (255, 0, 255)
    border = [(x, y) for x in range(0, w, 20) for y in (0, h - 1)] + \
             [(x, y) for y in range(0, h, 20) for x in (0, w - 1)]
    for xy in border:
        pixel = im.getpixel(xy)
        if pixel != marker and sum(pixel) > 600:   # light pixel = background
            ImageDraw.floodfill(im, xy, marker, thresh=TOLERANCE)

    # Marker colour -> transparent.
    rgba = im.convert("RGBA")
    rgba.putdata([(255, 255, 255, 0) if p[:3] == marker else p for p in rgba.getdata()])

    # Crop to the drawing, keep a small margin, resize.
    left, top, right, bottom = rgba.getchannel("A").getbbox()
    rgba = rgba.crop((max(left - MARGIN, 0), max(top - MARGIN, 0),
                      min(right + MARGIN, w), min(bottom + MARGIN, h)))
    rgba.thumbnail(MAX_SIZE, Image.LANCZOS)

    # Write a hidden temporary file, then rename it: a running `jekyll serve`
    # ignores hidden files, so it never copies a half-written image.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    final = OUTPUT_DIR / f"{name}.webp"
    temp = OUTPUT_DIR / f".{name}.webp.tmp"
    rgba.save(temp, "WEBP", quality=88, method=6)
    os.replace(temp, final)
    print(f"{final.relative_to(REPO)}  {rgba.size[0]}x{rgba.size[1]}  {final.stat().st_size // 1024} KB")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        prepare(Path(sys.argv[1]), sys.argv[2])
    elif len(sys.argv) == 1:
        for source, name in DRAWINGS.items():
            prepare(SOURCE_DIR / source, name)
    else:
        print(__doc__)
        sys.exit(1)
