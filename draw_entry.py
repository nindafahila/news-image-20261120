#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news front page (1024x1024 PNG).

Deterministic: fixed text, fixed geometry, no randomness, no network.
Run: python3 draw_entry.py  -> writes entry.png beside this file.
Fonts: DejaVu (present on the build machine and in most Linux images).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 238)
NAVY = (20, 33, 61)
NAVY2 = (27, 45, 84)
GOLD = (201, 162, 39)
RED = (180, 35, 24)
INK = (24, 24, 24)
GREY = (90, 90, 90)
CARD = (255, 255, 255)
BORDER = (210, 205, 192)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------- masthead ----------------
d.rectangle([0, 0, W, 122], fill=NAVY)
d.text((W // 2, 14), "THE WORLD TODAY", font=font(SERIF, 58),
       fill=(255, 255, 255), anchor="ma")
d.rectangle([W // 2 - 300, 86, W // 2 + 300, 89], fill=GOLD)
d.text((W // 2, 96), "FRIDAY  ·  20 NOVEMBER 2026",
       font=font(SANS_B, 24), fill=(232, 196, 90), anchor="ma")

# ---------------- lead story ----------------
LX, LY, LW, LH = 28, 138, 968, 300
d.rectangle([LX, LY, LX + LW, LY + LH], fill=CARD, outline=BORDER, width=2)
d.rectangle([LX, LY, LX + LW, LY + 6], fill=RED)
tx = LX + 22
d.text((tx, LY + 20), "LEAD  —  INDIA  ·  WEATHER",
       font=font(SANS_B, 19), fill=RED)
headline = "Cyclone Akvan slams into Odisha coast"
y = draw_lines(d, tx, LY + 50,
               wrap(d, headline, font(SANS_B, 38), 560),
               font(SANS_B, 38), INK, 46)
summary = ("The storm crossed near Gopalpur on Friday morning with winds of "
           "70-80 km/h. More than 300,000 people were moved to shelters; "
           "no deaths were reported in the first assessment.")
draw_lines(d, tx, y + 8,
           wrap(d, summary, font(SANS, 18), 560),
           font(SANS, 18), (60, 60, 60), 25)

# lead illustration: storm panel with cyclone spiral
PX, PY, PW, PH = 648, LY + 20, 326, 238
d.rectangle([PX, PY, PX + PW, PY + PH], fill=(214, 232, 245),
            outline=BORDER, width=1)
# cyclone spiral: concentric arcs
cx, cy = PX + PW // 2, PY + 96
for rr, col in [(78, (46, 111, 173)), (58, (70, 130, 190)),
                (38, (110, 165, 210)), (18, (150, 195, 230))]:
    d.arc([cx - rr, cy - rr, cx + rr, cy + rr], 30, 330, fill=col, width=7)
d.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=(20, 33, 61))
d.line([cx, cy, cx + 62, cy - 52], fill=(20, 33, 61), width=4)
d.text((PX + PW // 2, PY + 168), "CYCLONE AKVAN", font=font(SANS_B, 24),
       fill=NAVY, anchor="ma")
d.text((PX + PW // 2, PY + 198), "ODISHA  ·  70-80 KM/H WINDS",
       font=font(SANS_B, 15), fill=(90, 90, 90), anchor="ma")

# ---------------- story cards: 2 cols x 3 rows ----------------
cards = [
    ("MARKETS", (27, 108, 66), "trade",
     "Global sell-off deepens",
     "Nikkei -4.8% and Kospi -5.2% on Friday as the AI rout spreads; "
     "the S&P 500 had fallen 2% on Thursday, a sixth straight loss."),
    ("EUROPE", (20, 33, 61), "gavel",
     "EU approves \u20ac1bn arms for Ukraine",
     "The Council signs off joint procurement of drones, air defence and "
     "ammo on Friday; a record \u20ac7.9bn tranche is disbursed the same day."),
    ("GAMES", (176, 92, 8), "sport",
     "GTA 6 smashes $2.3bn in a day",
     "Sensor Tower estimates 24.6m copies sold in the first 24 hours, the "
     "biggest entertainment launch ever; no official figures yet."),
    ("CLIMATE", (18, 90, 160), "storm",
     "COP31 enters final day, fossil text missing",
     "The Friday deadline nears in Antalya; Thursday's draft dropped all "
     "fossil-fuel language and negotiators race to restore it."),
    ("TECH", (13, 92, 96), "drone",
     "Anthropic's record IPO fades fast",
     "Shares closed 17% above the $83 offer on debut, then fell 4.7% "
     "after hours as the AI sell-off deepened."),
    ("USA", (180, 35, 24), "quake",
     "Quake wakes Los Angeles",
     "A magnitude 4.2 tremor struck near Commerce at 3:25 a.m.; felt "
     "across Southern California, with no major damage reported."),
]

GX, GY = 28, 454
CW, CH, CGAP, RGAP = 476, 152, 16, 12


def icon(draw, kind, x, y, col):
    """Simple 46x46 pictogram in the card's accent colour."""
    if kind == "bridge":
        draw.line([x, y + 36, x + 46, y + 36], fill=col, width=4)
        draw.line([x + 6, y + 36, x + 6, y + 10], fill=col, width=4)
        draw.line([x + 40, y + 36, x + 40, y + 10], fill=col, width=4)
        draw.arc([x + 6, y + 14, x + 40, y + 40], 180, 360, fill=col, width=3)
        draw.line([x + 6, y + 10, x + 40, y + 10], fill=col, width=3)
    elif kind == "drone":
        draw.ellipse([x + 16, y + 16, x + 30, y + 30], fill=col)
        for cx0, cy0 in [(x + 4, y + 4), (x + 34, y + 4),
                         (x + 4, y + 34), (x + 34, y + 34)]:
            draw.ellipse([cx0, cy0, cx0 + 8, cy0 + 8], outline=col, width=2)
        draw.line([x + 8, y + 8, x + 18, y + 18], fill=col, width=2)
        draw.line([x + 38, y + 8, x + 28, y + 18], fill=col, width=2)
        draw.line([x + 8, y + 38, x + 18, y + 28], fill=col, width=2)
        draw.line([x + 38, y + 38, x + 28, y + 28], fill=col, width=2)
    elif kind == "trade":
        draw.line([x + 4, y + 14, x + 34, y + 14], fill=col, width=4)
        draw.polygon([(x + 34, y + 6), (x + 44, y + 14), (x + 34, y + 22)],
                     fill=col)
        draw.line([x + 42, y + 32, x + 12, y + 32], fill=col, width=4)
        draw.polygon([(x + 12, y + 24), (x + 2, y + 32), (x + 12, y + 40)],
                     fill=col)
    elif kind == "gavel":
        draw.line([x + 8, y + 38, x + 38, y + 8], fill=col, width=5)
        draw.rectangle([x + 2, y + 26, x + 20, y + 38], fill=col)
        draw.rectangle([x + 26, y + 8, x + 44, y + 20], fill=col)
        draw.line([x + 4, y + 42, x + 42, y + 42], fill=col, width=3)
    elif kind == "storm":
        for rr in (20, 14, 8):
            draw.arc([x + 23 - rr, y + 23 - rr, x + 23 + rr, y + 23 + rr],
                     40, 300, fill=col, width=3)
        draw.line([x + 23, y + 23, x + 40, y + 12], fill=col, width=3)
    elif kind == "sport":
        draw.line([x + 10, y + 40, x + 34, y + 10], fill=col, width=7)
        draw.ellipse([x + 34, y + 30, x + 44, y + 40], fill=(178, 34, 52))
    elif kind == "quake":
        draw.line([x + 4, y + 34, x + 14, y + 14, x + 24, y + 30,
                   x + 34, y + 10, x + 44, y + 26], fill=col, width=4)


for i, (tag, col, kind, head, body) in enumerate(cards):
    cx0 = GX + (i % 2) * (CW + CGAP)
    cy0 = GY + (i // 2) * (CH + RGAP)
    d.rectangle([cx0, cy0, cx0 + CW, cy0 + CH], fill=CARD,
                outline=BORDER, width=2)
    d.rectangle([cx0, cy0, cx0 + 8, cy0 + CH], fill=col)
    icon(d, kind, cx0 + CW - 62, cy0 + 14, col)
    d.text((cx0 + 22, cy0 + 12), tag, font=font(SANS_B, 15), fill=col)
    y = draw_lines(d, cx0 + 22, cy0 + 34,
                   wrap(d, head, font(SANS_B, 20), CW - 100),
                   font(SANS_B, 20), INK, 24)
    draw_lines(d, cx0 + 22, y + 4,
               wrap(d, body, font(SANS, 14), CW - 44),
               font(SANS, 14), (70, 70, 70), 19)

# ---------------- ticker footer ----------------
FY = 948
d.rectangle([0, FY, W, H], fill=NAVY)
ticker = ("ALSO:  Trump pardons Pete Rose posthumously  ·  IMF: global public debt nears 100% of world GDP  ·  "
          "Kenya starts 42-day Ebola-free countdown")
tfs = 16
while d.textlength(ticker, font=font(SANS_B, tfs)) > W - 40 and tfs > 10:
    tfs -= 1
d.text((W // 2, FY + 10), ticker, font=font(SANS_B, tfs),
       fill=(255, 255, 255), anchor="ma")
d.text((W // 2, FY + 38), "Friday 20 November 2026  ·  The world in one image",
       font=font(SANS, 14), fill=(200, 205, 220), anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
