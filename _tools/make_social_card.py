"""Draw the images used by browsers and social networks.

Creates in assets/img/:
  social-card.png       1200 x 630 picture shown when the site is shared
                        (LinkedIn, Slack, WhatsApp...), set in _config.yml
  favicon-32.png        tab icon for browsers that do not use favicon.svg
  apple-touch-icon.png  icon used when the site is added to a phone home screen

Usage (from the repository folder), e.g. after changing your title below:
  python3 _tools/make_social_card.py

Needs Python with Pillow, and the Liberation fonts (installed on most Linux systems;
change FONT_DIR otherwise).
"""
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "assets" / "img"
ILLUSTRATION = OUT / "illustrations" / "home.webp"

NAME = "Alice Lacan, Ph.D."
ROLE = "Junior AI Fellow · CBIO, Mines Paris – PSL & Institut Curie"
TOPICS = "Generative AI  ·  Biomedical data  ·  Teaching"
ADDRESS = "ablacan.github.io"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
BOLD = FONT_DIR / "LiberationSans-Bold.ttf"
REGULAR = FONT_DIR / "LiberationSans-Regular.ttf"

# Same palette as assets/css/site.css
INK, MUTED, PAPER = (29, 29, 31), (95, 99, 104), (251, 250, 247)
BLUE, RED, YELLOW = (31, 79, 163), (214, 64, 43), (242, 194, 48)


def multiply(base, draw_shape):
    """Draw a shape on a white layer and blend it with "multiply" (like the website)."""
    layer = Image.new("RGB", base.size, (255, 255, 255))
    draw_shape(ImageDraw.Draw(layer))
    return ImageChops.multiply(base, layer)


def logo(size):
    """The Kandinsky logo of the header, drawn at `size` pixels."""
    k = size / 40
    img = Image.new("RGB", (size, size), (255, 255, 255))
    img = multiply(img, lambda d: d.ellipse([(22 - 13) * k, (17 - 13) * k, (22 + 13) * k, (17 + 13) * k], fill=YELLOW))
    img = multiply(img, lambda d: d.polygon([(4 * k, 37 * k), (15 * k, 17 * k), (26 * k, 37 * k)], fill=BLUE))
    img = multiply(img, lambda d: d.ellipse([29 * k, 28 * k, 37 * k, 36 * k], fill=RED))
    # transparent background: white -> transparent
    rgba = img.convert("RGBA")
    rgba.putdata([(255, 255, 255, 0) if p[:3] == (255, 255, 255) else p for p in rgba.getdata()])
    return rgba


def social_card():
    W, H = 1200, 630
    card = Image.new("RGB", (W, H), PAPER)

    # Shapes behind the illustration (right side), same composition as _includes/illustration.html
    ox, oy, s = 790, 40, 1.1
    card = multiply(card, lambda d: d.ellipse([ox + (215 - 150) * s, oy + (215 - 150) * s, ox + (215 + 150) * s, oy + (215 + 150) * s], fill=YELLOW))
    card = multiply(card, lambda d: d.polygon([(ox + 40 * s, oy + 470 * s), (ox + 175 * s, oy + 250 * s), (ox + 300 * s, oy + 470 * s)], fill=BLUE))
    card = multiply(card, lambda d: d.ellipse([ox + 301 * s, oy + 61 * s, ox + 369 * s, oy + 129 * s], fill=RED))
    draw = ImageDraw.Draw(card)
    draw.polygon([(ox + 70 * s, oy + 40 * s), (ox + 82 * s, oy + 250 * s), (ox + 58 * s, oy + 250 * s)], fill=INK)
    draw.line([(ox + 10 * s, oy + 345 * s), (ox + 390 * s, oy + 300 * s)], fill=INK, width=3)
    draw.line([(ox + 300 * s, oy + 20 * s), (ox + 365 * s, oy + 500 * s)], fill=INK, width=3)

    # Illustration with its red offset outline
    art = Image.open(ILLUSTRATION).convert("RGBA")
    art.thumbnail((400, 560), Image.LANCZOS)
    ax, ay = ox + int(215 * s) - art.width // 2, H - art.height - 20
    offset = Image.new("RGBA", art.size, RED + (255,))
    card.paste(offset, (ax + 9, ay + 7), art.getchannel("A"))
    card.paste(art, (ax, ay), art)

    # Text (left side)
    draw = ImageDraw.Draw(card)
    x = 70
    draw.text((x, 150), NAME, font=ImageFont.truetype(str(BOLD), 74), fill=INK)

    role_font = ImageFont.truetype(str(REGULAR), 26)
    left, top, right, bottom = draw.textbbox((x, 270), ROLE, font=role_font)
    # highlighter stroke: a slightly tilted yellow band behind the lower part of the role
    text_h = bottom - top
    band = Image.new("RGBA", (right - left + 24, int(text_h * 0.85)), (0, 0, 0, 0))
    ImageDraw.Draw(band).rounded_rectangle([0, 0, band.width - 1, band.height - 1], radius=10, fill=YELLOW + (225,))
    band = band.rotate(0.8, expand=True, resample=Image.BICUBIC)
    card.paste(band, (left - 10, top + int(text_h * 0.3) - band.height // 2 + int(text_h * 0.42)), band)
    draw.text((x, 270), ROLE, font=role_font, fill=INK)

    draw.text((x, 360), TOPICS, font=ImageFont.truetype(str(REGULAR), 30), fill=MUTED)
    draw.text((x, 520), ADDRESS, font=ImageFont.truetype(str(BOLD), 30), fill=BLUE)

    path = OUT / "social-card.png"
    card.save(path, optimize=True)
    print(f"{path.relative_to(REPO)}  {path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    social_card()
    for size, name in [(32, "favicon-32.png"), (180, "apple-touch-icon.png")]:
        icon = logo(size)
        if name.startswith("apple"):   # phones need an opaque background
            bg = Image.new("RGBA", icon.size, PAPER + (255,))
            icon = Image.alpha_composite(bg, icon)
        icon.save(OUT / name)
        print(f"assets/img/{name}")
