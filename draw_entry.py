"""Render entry.png: a one-page newspaper front page summing up the world
news of Thursday 19 November 2026. Pillow only; run once at build time.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 234)
INK = (25, 25, 25)
NAVY = (16, 38, 63)
NAVY2 = (28, 58, 90)
GOLD = (201, 162, 39)
RED = (180, 35, 24)
GREEN = (20, 83, 45)
GREY = (90, 90, 86)
RULE = (200, 192, 172)


def font(name, size):
    paths = {
        "serif": "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "serif_reg": "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "sans": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "sans_reg": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    }
    try:
        return ImageFont.truetype(paths[name], size)
    except Exception:
        return ImageFont.load_default()


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- Header ----------
d.rectangle([0, 0, W, 150], fill=NAVY)
d.rectangle([0, 150, W, 156], fill=GOLD)
d.text((512, 18), "THE WORLD IN ONE DAY", font=font("serif", 56),
       fill=(255, 255, 255), anchor="ma")
d.text((512, 92), "T H U R S D A Y   1 9   N O V E M B E R   2 0 2 6",
       font=font("sans", 30), fill=GOLD, anchor="ma")

# ---------- Lead story: Shenzhen trilateral ----------
# Illustration panel: sky, skyline, three flags.
px0, py0, px1, py1 = 24, 172, 424, 512
d.rectangle([px0, py0, px1, py1], fill=(178, 208, 228))
d.rectangle([px0, py1 - 118, px1, py1], fill=NAVY2)
for bx, bw, bh in [(40, 46, 150), (100, 60, 210), (176, 44, 130),
                   (232, 58, 190), (306, 40, 110), (356, 48, 160)]:
    d.rectangle([px0 + bx, py1 - 118 - bh + 118, px0 + bx + bw,
                 py1], fill=NAVY)
# windows
for bx, bw, bh in [(40, 46, 150), (100, 60, 210), (176, 44, 130),
                   (232, 58, 190), (306, 40, 110), (356, 48, 160)]:
    for wy in range(py1 - bh + 8, py1 - 8, 18):
        for wx in range(px0 + bx + 8, px0 + bx + bw - 8, 16):
            d.rectangle([wx, wy, wx + 6, wy + 8], fill=(255, 214, 120))
# sun
d.ellipse([px0 + 300, py0 + 18, px0 + 360, py0 + 78], fill=(255, 196, 66))
# three flags on poles
def flag(x, y, kind):
    d.rectangle([x, y, x + 4, y + 120], fill=(60, 60, 60))
    if kind == "us":
        for i in range(7):
            d.rectangle([x + 4, y + i * 9, x + 74, y + (i + 1) * 9],
                        fill=RED if i % 2 == 0 else (255, 255, 255))
        d.rectangle([x + 4, y, x + 34, y + 36], fill=NAVY)
        for sx in range(3):
            for sy in range(3):
                d.ellipse([x + 9 + sx * 9, y + 6 + sy * 10,
                           x + 13 + sx * 9, y + 10 + sy * 10],
                          fill=(255, 255, 255))
    elif kind == "cn":
        d.rectangle([x + 4, y, x + 74, y + 63], fill=(222, 41, 16))
        d.ellipse([x + 10, y + 8, x + 22, y + 20], fill=(255, 222, 0))
        for sx, sy in [(34, 10), (44, 20), (40, 32), (28, 34)]:
            d.ellipse([x + sx, y + sy, x + sx + 7, y + sy + 7],
                      fill=(255, 222, 0))
    else:  # russia
        d.rectangle([x + 4, y, x + 74, y + 21], fill=(255, 255, 255))
        d.rectangle([x + 4, y + 21, x + 74, y + 42], fill=(0, 57, 166))
        d.rectangle([x + 4, y + 42, x + 74, y + 63], fill=(213, 0, 50))


flag(px0 + 24, py0 + 96, "us")
flag(px0 + 118, py0 + 96, "cn")
flag(px0 + 212, py0 + 96, "ru")
d.text((px0 + 14, py0 + 10), "SHENZHEN", font=font("sans", 22),
       fill=NAVY)

# Lead text
tx = 452
d.text((tx, 178), "APEC  ·  SHENZHEN, CHINA", font=font("sans", 24),
       fill=RED)
y = text_block(d, tx, 212,
               wrap(d, "TRUMP, XI & PUTIN MEET IN A FIRST-EVER THREE-WAY SUMMIT",
                    font("sans", 36), 548), font("sans", 36), INK, 44)
y += 10
text_block(d, tx, y,
           wrap(d, "Ninety minutes at APEC. A \u201cpeace declaration\u201d on "
                   "nuclear risk \u2014 but no deal on Ukraine or Iran.",
                font("sans_reg", 23), 548), font("sans_reg", 23), (60, 60, 60), 30)
d.line([24, 530, 1000, 530], fill=RULE, width=2)

# ---------- Story grid (2 x 2) ----------
def icon_gavel(d, x, y, s=58):
    d.rectangle([x + 6, y + 8, x + s - 6, y + 20], fill=NAVY)
    d.line([x + s // 2, y + 20, x + s // 2 + 16, y + s - 8], fill=NAVY,
           width=7)
    d.line([x + 8, y + s - 4, x + s - 4, y + s - 4], fill=RED, width=4)


def icon_bridge(d, x, y, s=58):
    d.line([x + 4, y + s - 12, x + s - 4, y + s - 12], fill=NAVY, width=4)
    d.rectangle([x + 8, y + 10, x + 14, y + s - 12], fill=NAVY)
    d.rectangle([x + s - 14, y + 10, x + s - 8, y + s - 12], fill=NAVY)
    d.arc([x + 4, y + 2, x + s - 4, y + s - 2], 180, 360, fill=RED, width=4)


def icon_tank(d, x, y, s=58):
    d.rectangle([x + 6, y + 30, x + s - 6, y + 46], fill=NAVY)
    d.rectangle([x + 18, y + 18, x + s - 20, y + 32], fill=NAVY)
    d.line([x + s - 20, y + 24, x + s - 2, y + 20], fill=NAVY, width=6)
    for cx in (x + 14, x + 28, x + 42):
        d.ellipse([cx, y + 46, cx + 10, y + 56], fill=RED)


def icon_chart(d, x, y, s=58):
    d.line([x + 6, y + s - 8, x + s - 6, y + s - 8], fill=NAVY, width=3)
    for i, h in enumerate((16, 26, 36)):
        d.rectangle([x + 10 + i * 14, y + s - 8 - h, x + 20 + i * 14,
                     y + s - 8], fill=NAVY)
    d.line([x + 8, y + 26, x + s - 4, y + 4], fill=RED, width=4)
    d.polygon([(x + s - 4, y + 4), (x + s - 14, y + 4), (x + s - 4, y + 14)],
              fill=RED)


cells = [
    ("THE HAGUE", "COURT: MYANMAR COMMITTED GENOCIDE",
     "World court rules 9\u20136 on the Rohingya \u2014 the first state "
     "ever held responsible.", icon_gavel),
    ("UKRAINE", "CRIMEAN BRIDGE HIT A THIRD TIME",
     "Overnight strike halts trains; Putin rules out a Black Sea truce.",
     icon_bridge),
    ("GAZA", "ISRAEL ENDS GAZA TANK RAID",
     "First big ground push past the Yellow Line since the Oct 2025 "
     "ceasefire.", icon_tank),
    ("MARKETS", "ANTHROPIC'S RECORD IPO DEBUT",
     "Shares open at $111.50, close +17% at $97 \u2014 $81bn raised, "
     "the largest ever.", icon_chart),
]
gx, gy, cw, chh, gap = 24, 548, 478, 158, 20
for i, (kick, head, body, icon) in enumerate(cells):
    cx = gx + (i % 2) * (cw + gap)
    cy = gy + (i // 2) * (chh + gap)
    d.rectangle([cx, cy, cx + cw, cy + chh], outline=RULE, width=2)
    icon(d, cx + 14, cy + 16)
    tx2 = cx + 88
    d.text((tx2, cy + 12), kick, font=font("sans", 19), fill=RED)
    y2 = text_block(d, tx2, cy + 38,
                    wrap(d, head, font("sans", 25), cw - 102),
                    font("sans", 25), INK, 29)
    text_block(d, tx2, y2 + 4,
               wrap(d, body, font("sans_reg", 19), cw - 102),
               font("sans_reg", 19), (60, 60, 60), 24)

# ---------- COP31 band ----------
d.rectangle([24, 900, 1000, 962], fill=GREEN)
d.text((512, 912), "CLIMATE \u2014 COP31 DRAFT DROPS ALL FOSSIL-FUEL MENTIONS",
       font=font("sans", 25), fill=(255, 255, 255), anchor="ma")
d.text((512, 940), "Revised text in Antalya strips every fossil-fuel reference  ·  Final deal due Friday",
       font=font("sans_reg", 19), fill=(220, 235, 220), anchor="ma")

# ---------- Footer ticker ----------
d.line([24, 978, 1000, 978], fill=RULE, width=2)
d.text((512, 988), "ALSO: BANGLADESH LOCKDOWN \u2014 4 DEAD  ·  "
       "STOCKS SLUMP 2%  ·  THURSDAY 19 NOVEMBER 2026",
       font=font("sans", 17), fill=GREY, anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
