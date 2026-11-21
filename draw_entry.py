#!/usr/bin/env python3
"""Render the Friday 20 November 2026 front page as a 1024x1024 PNG.

Everything is fixed: the same text at the same coordinates on every run,
so the output bytes never change. Run `python3 draw_entry.py` and it writes
entry.png next to this script. Needs Pillow and the DejaVu fonts.
"""
from PIL import Image, ImageDraw, ImageFont

PAGE_W, PAGE_H = 1024, 1024
BACKGROUND = (250, 246, 238)
DARK_BLUE = (20, 33, 61)
GOLD_LINE = (201, 162, 39)
LEAD_RED = (180, 35, 24)
BODY_INK = (24, 24, 24)
SOFT_GREY = (90, 90, 90)
CARD_WHITE = (255, 255, 255)
HAIRLINE = (210, 205, 192)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_BOLD = FONT_DIR + "DejaVuSerif-Bold.ttf"
SANS_PLAIN = FONT_DIR + "DejaVuSans.ttf"
SANS_BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"


def load_font(path, size):
    return ImageFont.truetype(path, size)


def fit_lines(draw, text, font, max_width):
    """Split text into as few lines as fit in max_width pixels."""
    out, current = [], ""
    for word in text.split():
        candidate = (current + " " + word).strip()
        if draw.textlength(candidate, font=font) <= max_width:
            current = candidate
        else:
            if current:
                out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def put_lines(draw, x, y, lines, font, fill, step):
    """Draw lines top to bottom; return the y just past the last line."""
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += step
    return y


canvas = Image.new("RGB", (PAGE_W, PAGE_H), BACKGROUND)
d = ImageDraw.Draw(canvas)

# ---- masthead ----
d.rectangle([0, 0, PAGE_W, 122], fill=DARK_BLUE)
d.text((PAGE_W // 2, 14), "THE WORLD TODAY",
       font=load_font(SERIF_BOLD, 58), fill=(255, 255, 255), anchor="ma")
d.rectangle([PAGE_W // 2 - 300, 86, PAGE_W // 2 + 300, 89], fill=GOLD_LINE)
d.text((PAGE_W // 2, 96), "FRIDAY  ·  20 NOVEMBER 2026",
       font=load_font(SANS_BOLD, 24), fill=(232, 196, 90), anchor="ma")

# ---- lead story ----
LEAD_X, LEAD_Y, LEAD_W, LEAD_H = 28, 138, 968, 300
d.rectangle([LEAD_X, LEAD_Y, LEAD_X + LEAD_W, LEAD_Y + LEAD_H],
            fill=CARD_WHITE, outline=HAIRLINE, width=2)
d.rectangle([LEAD_X, LEAD_Y, LEAD_X + LEAD_W, LEAD_Y + 6], fill=LEAD_RED)
text_x = LEAD_X + 22
d.text((text_x, LEAD_Y + 20), "LEAD  —  INDIA  ·  WEATHER",
       font=load_font(SANS_BOLD, 19), fill=LEAD_RED)
headline = "Cyclone Akvan slams into Odisha coast"
next_y = put_lines(d, text_x, LEAD_Y + 50,
                   fit_lines(d, headline, load_font(SANS_BOLD, 38), 560),
                   load_font(SANS_BOLD, 38), BODY_INK, 46)
summary = ("The storm crossed near Gopalpur on Friday morning with winds of "
           "70-80 km/h. More than 300,000 people were moved to shelters; "
           "no deaths were reported in the first assessment.")
put_lines(d, text_x, next_y + 8,
          fit_lines(d, summary, load_font(SANS_PLAIN, 18), 560),
          load_font(SANS_PLAIN, 18), (60, 60, 60), 25)

# ---- lead art: cyclone spiral in a sky-blue panel ----
ART_X, ART_Y, ART_W, ART_H = 648, LEAD_Y + 20, 326, 238
d.rectangle([ART_X, ART_Y, ART_X + ART_W, ART_Y + ART_H],
            fill=(214, 232, 245), outline=HAIRLINE, width=1)
eye_x, eye_y = ART_X + ART_W // 2, ART_Y + 96
rings = [(78, (46, 111, 173)), (58, (70, 130, 190)),
         (38, (110, 165, 210)), (18, (150, 195, 230))]
for radius, shade in rings:
    d.arc([eye_x - radius, eye_y - radius, eye_x + radius, eye_y + radius],
          30, 330, fill=shade, width=7)
d.ellipse([eye_x - 10, eye_y - 10, eye_x + 10, eye_y + 10], fill=(20, 33, 61))
d.line([eye_x, eye_y, eye_x + 62, eye_y - 52], fill=(20, 33, 61), width=4)
d.text((ART_X + ART_W // 2, ART_Y + 168), "CYCLONE AKVAN",
       font=load_font(SANS_BOLD, 24), fill=DARK_BLUE, anchor="ma")
d.text((ART_X + ART_W // 2, ART_Y + 198), "ODISHA  ·  70-80 KM/H WINDS",
       font=load_font(SANS_BOLD, 15), fill=(90, 90, 90), anchor="ma")

# ---- six story cards, two columns by three rows ----
STORIES = [
    {"tag": "MARKETS", "color": (27, 108, 66), "glyph": "trade",
     "head": "Global sell-off deepens",
     "body": ("Nikkei -4.8% and Kospi -5.2% on Friday as the AI rout spreads; "
              "the S&P 500 had fallen 2% on Thursday, a sixth straight loss.")},
    {"tag": "EUROPE", "color": (20, 33, 61), "glyph": "gavel",
     "head": "EU approves \u20ac1bn arms for Ukraine",
     "body": ("The Council signs off joint procurement of drones, air defence and "
              "ammo on Friday; a record \u20ac7.9bn tranche is disbursed the same day.")},
    {"tag": "GAMES", "color": (176, 92, 8), "glyph": "sport",
     "head": "GTA 6 smashes $2.3bn in a day",
     "body": ("Sensor Tower estimates 24.6m copies sold in the first 24 hours, the "
              "biggest entertainment launch ever; no official figures yet.")},
    {"tag": "CLIMATE", "color": (18, 90, 160), "glyph": "storm",
     "head": "COP31 enters final day, fossil text missing",
     "body": ("The Friday deadline nears in Antalya; Thursday's draft dropped all "
              "fossil-fuel language and negotiators race to restore it.")},
    {"tag": "TECH", "color": (13, 92, 96), "glyph": "drone",
     "head": "Anthropic's record IPO fades fast",
     "body": ("Shares closed 17% above the $83 offer on debut, then fell 4.7% "
              "after hours as the AI sell-off deepened.")},
    {"tag": "USA", "color": (180, 35, 24), "glyph": "quake",
     "head": "Quake wakes Los Angeles",
     "body": ("A magnitude 4.2 tremor struck near Commerce at 3:25 a.m.; felt "
              "across Southern California, with no major damage reported.")},
]

GRID_X, GRID_Y = 28, 454
CELL_W, CELL_H, COL_GAP, ROW_GAP = 476, 152, 16, 12


def glyph(draw, kind, x, y, color):
    """Draw one small 46x46 pictogram in the card's accent colour."""
    if kind == "bridge":
        draw.line([x, y + 36, x + 46, y + 36], fill=color, width=4)
        draw.line([x + 6, y + 36, x + 6, y + 10], fill=color, width=4)
        draw.line([x + 40, y + 36, x + 40, y + 10], fill=color, width=4)
        draw.arc([x + 6, y + 14, x + 40, y + 40], 180, 360, fill=color, width=3)
        draw.line([x + 6, y + 10, x + 40, y + 10], fill=color, width=3)
    elif kind == "drone":
        draw.ellipse([x + 16, y + 16, x + 30, y + 30], fill=color)
        for cx0, cy0 in [(x + 4, y + 4), (x + 34, y + 4),
                         (x + 4, y + 34), (x + 34, y + 34)]:
            draw.ellipse([cx0, cy0, cx0 + 8, cy0 + 8], outline=color, width=2)
        draw.line([x + 8, y + 8, x + 18, y + 18], fill=color, width=2)
        draw.line([x + 38, y + 8, x + 28, y + 18], fill=color, width=2)
        draw.line([x + 8, y + 38, x + 18, y + 28], fill=color, width=2)
        draw.line([x + 38, y + 38, x + 28, y + 28], fill=color, width=2)
    elif kind == "trade":
        draw.line([x + 4, y + 14, x + 34, y + 14], fill=color, width=4)
        draw.polygon([(x + 34, y + 6), (x + 44, y + 14), (x + 34, y + 22)],
                     fill=color)
        draw.line([x + 42, y + 32, x + 12, y + 32], fill=color, width=4)
        draw.polygon([(x + 12, y + 24), (x + 2, y + 32), (x + 12, y + 40)],
                     fill=color)
    elif kind == "gavel":
        draw.line([x + 8, y + 38, x + 38, y + 8], fill=color, width=5)
        draw.rectangle([x + 2, y + 26, x + 20, y + 38], fill=color)
        draw.rectangle([x + 26, y + 8, x + 44, y + 20], fill=color)
        draw.line([x + 4, y + 42, x + 42, y + 42], fill=color, width=3)
    elif kind == "storm":
        for radius in (20, 14, 8):
            draw.arc([x + 23 - radius, y + 23 - radius,
                      x + 23 + radius, y + 23 + radius],
                     40, 300, fill=color, width=3)
        draw.line([x + 23, y + 23, x + 40, y + 12], fill=color, width=3)
    elif kind == "sport":
        draw.line([x + 10, y + 40, x + 34, y + 10], fill=color, width=7)
        draw.ellipse([x + 34, y + 30, x + 44, y + 40], fill=(178, 34, 52))
    elif kind == "quake":
        draw.line([x + 4, y + 34, x + 14, y + 14, x + 24, y + 30,
                   x + 34, y + 10, x + 44, y + 26], fill=color, width=4)


for pos, story in enumerate(STORIES):
    cell_x = GRID_X + (pos % 2) * (CELL_W + COL_GAP)
    cell_y = GRID_Y + (pos // 2) * (CELL_H + ROW_GAP)
    accent = story["color"]
    d.rectangle([cell_x, cell_y, cell_x + CELL_W, cell_y + CELL_H],
                fill=CARD_WHITE, outline=HAIRLINE, width=2)
    d.rectangle([cell_x, cell_y, cell_x + 8, cell_y + CELL_H], fill=accent)
    glyph(d, story["glyph"], cell_x + CELL_W - 62, cell_y + 14, accent)
    d.text((cell_x + 22, cell_y + 12), story["tag"],
           font=load_font(SANS_BOLD, 15), fill=accent)
    after_head = put_lines(
        d, cell_x + 22, cell_y + 34,
        fit_lines(d, story["head"], load_font(SANS_BOLD, 20), CELL_W - 100),
        load_font(SANS_BOLD, 20), BODY_INK, 24)
    put_lines(d, cell_x + 22, after_head + 4,
              fit_lines(d, story["body"], load_font(SANS_PLAIN, 14), CELL_W - 44),
              load_font(SANS_PLAIN, 14), (70, 70, 70), 19)

# ---- ticker footer ----
FOOT_Y = 948
d.rectangle([0, FOOT_Y, PAGE_W, PAGE_H], fill=DARK_BLUE)
ticker = ("ALSO:  Trump pardons Pete Rose posthumously  ·  IMF: global public debt nears 100% of world GDP  ·  "
          "Kenya starts 42-day Ebola-free countdown")
tick_size = 16
while (d.textlength(ticker, font=load_font(SANS_BOLD, tick_size)) > PAGE_W - 40
       and tick_size > 10):
    tick_size -= 1
d.text((PAGE_W // 2, FOOT_Y + 10), ticker,
       font=load_font(SANS_BOLD, tick_size), fill=(255, 255, 255), anchor="ma")
d.text((PAGE_W // 2, FOOT_Y + 38), "Friday 20 November 2026  ·  The world in one image",
       font=load_font(SANS_PLAIN, 14), fill=(200, 205, 220), anchor="ma")

canvas.save("entry.png", optimize=True)
print("saved entry.png", canvas.size)
