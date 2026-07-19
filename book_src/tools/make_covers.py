#!/usr/bin/env python3
# Native cover generator for the three-volume book, at the print trim.
# Redraws the meadow/moon art (from the original cover_suite.py) at the current
# trim so nothing is stretched, and adds: per-volume VOLUME line + title, the
# author, "First Edition" (front); the series blurb without "Serendip Commons
# Society" (back). Outputs SVG + PDF + PNG (300 DPI) via rsvg-convert.
#
# Trim: 7.5 x 9.25 in = 190.5 x 234.95 mm; + 3 mm bleed each side.
import math, random, textwrap, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "..", "assets")
os.chdir(A)

BLEED = 3.0
TRIM_W, TRIM_H = 190.5, 234.95            # 7.5 x 9.25 in
W, H = TRIM_W + 2 * BLEED, TRIM_H + 2 * BLEED   # 196.5 x 240.95
GROUND = H
VS = H / 216.0                            # vertical-scale vs the original design
CX = W / 2

BLUSH, BLUSH_DEEP = "#FDF2F4", "#F7E2E7"
ROSE, ROSE_SOFT, GOLD, INK = "#9E4256", "#C4798B", "#B08A4C", "#342E37"
SERIF = "TeX Gyre Pagella"

VOLS = {
    1: ("I",   "Relational Being, the Subject, and the Word"),
    2: ("II",  "Generativity, Value, and Power"),
    3: ("III", "Happiness, Ethics, Aesthetics, and Culture"),
}


# ---------------- drawing helpers (from cover_suite.py) ----------------
def blade(x, h, lean, width, color, opacity):
    tipx, tipy = x + lean, GROUND - h
    c1x, c1y = x + lean * 0.25, GROUND - h * 0.45
    c2x, c2y = x + lean * 0.7, GROUND - h * 0.85
    return (f'<path d="M {x-width/2:.2f} {GROUND} '
            f'C {c1x-width*0.3:.2f} {c1y:.2f} {c2x-width*0.12:.2f} {c2y:.2f} {tipx:.2f} {tipy:.2f} '
            f'C {c2x+width*0.12:.2f} {c2y:.2f} {c1x+width*0.3:.2f} {c1y:.2f} {x+width/2:.2f} {GROUND} Z" '
            f'fill="{color}" fill-opacity="{opacity:.2f}"/>')


def stem_path(x, h, lean):
    tipx, tipy = x + lean, GROUND - h
    c1x, c1y = x + lean * 0.2, GROUND - h * 0.5
    c2x, c2y = x + lean * 0.65, GROUND - h * 0.85
    return (tipx, tipy,
            f'M {x:.2f} {GROUND} C {c1x:.2f} {c1y:.2f} {c2x:.2f} {c2y:.2f} {tipx:.2f} {tipy:.2f}')


def flower(cx, cy, r, petal, center, n=5, opacity=0.95, rot0=0.0):
    s = []
    for i in range(n):
        a = rot0 + i * 2 * math.pi / n
        px, py = cx + math.cos(a) * r * 0.62, cy + math.sin(a) * r * 0.62
        s.append(f'<ellipse cx="{px:.2f}" cy="{py:.2f}" rx="{r*0.55:.2f}" ry="{r*0.38:.2f}" '
                 f'transform="rotate({math.degrees(a):.1f} {px:.2f} {py:.2f})" '
                 f'fill="{petal}" fill-opacity="{opacity:.2f}"/>')
    s.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r*0.22:.2f}" fill="{center}"/>')
    return "".join(s)


def seedhead(cx, cy, r, color, n=9):
    s = []
    for i in range(n):
        a = -math.pi * 0.95 + i * (math.pi * 0.9) / (n - 1)
        ex, ey = cx + math.cos(a) * r, cy + math.sin(a) * r
        s.append(f'<line x1="{cx:.2f}" y1="{cy:.2f}" x2="{ex:.2f}" y2="{ey:.2f}" '
                 f'stroke="{color}" stroke-width="0.22" stroke-opacity="0.85"/>')
        s.append(f'<circle cx="{ex:.2f}" cy="{ey:.2f}" r="0.42" fill="{color}" fill-opacity="0.9"/>')
    return "".join(s)


def leaf(x, y, ang, L, color, opacity):
    a = math.radians(ang)
    tx, ty = x + math.cos(a) * L, y + math.sin(a) * L
    n1x, n1y = -math.sin(a), math.cos(a)
    mx, my = (x + tx) / 2, (y + ty) / 2
    wdt = L * 0.30
    return (f'<path d="M {x:.2f} {y:.2f} Q {mx + n1x*wdt:.2f} {my + n1y*wdt:.2f} {tx:.2f} {ty:.2f} '
            f'Q {mx - n1x*wdt:.2f} {my - n1y*wdt:.2f} {x:.2f} {y:.2f} Z" '
            f'fill="{color}" fill-opacity="{opacity:.2f}"/>')


def header():
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">',
            f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="{BLUSH}"/><stop offset="0.62" stop-color="{BLUSH}"/>
  <stop offset="1" stop-color="{BLUSH_DEEP}"/>
</linearGradient>
<radialGradient id="moon" cx="0.5" cy="0.5" r="0.5">
  <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.55"/>
  <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
</radialGradient>
</defs>''',
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#bg)"/>']


def meadow(add, dense=1.0, flowers_n=9, halo_x=None):
    if halo_x is not None:
        add(f'<circle cx="{halo_x:.1f}" cy="{150*VS:.1f}" r="{42*VS:.1f}" fill="url(#moon)"/>')
    for _ in range(int(150 * dense)):
        x = random.uniform(-4, W + 4); h = random.uniform(28, 54) * VS; lean = random.uniform(-9, 9)
        c = random.choice([ROSE_SOFT, GOLD, ROSE_SOFT])
        add(blade(x, h, lean, random.uniform(0.5, 0.9), c, random.uniform(0.16, 0.30)))
    for _ in range(int(42 * dense)):
        x = random.uniform(2, W - 2); h = random.uniform(20, 40) * VS; lean = random.uniform(-7, 7)
        color = random.choice([GOLD, ROSE, ROSE_SOFT])
        tipx, tipy, d = stem_path(x, h, lean)
        add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="0.45" stroke-opacity="0.6" stroke-linecap="round"/>')
        k = random.random()
        if k < 0.38:
            add(seedhead(tipx, tipy, random.uniform(2.2, 3.4), GOLD if color != GOLD else ROSE_SOFT))
        elif k < 0.62:
            add(f'<circle cx="{tipx:.2f}" cy="{tipy:.2f}" r="{random.uniform(0.8,1.3):.2f}" fill="{ROSE}" fill-opacity="0.8"/>')
        if random.random() < 0.6:
            add(leaf(x + lean * 0.3, GROUND - h * 0.45, random.choice([-150, -30]) + random.uniform(-12, 12),
                     random.uniform(4, 7), color, 0.35))
    for _ in range(int(100 * dense)):
        x = random.uniform(-3, W + 3); h = random.uniform(8, 24) * VS; lean = random.uniform(-5, 5)
        c = random.choice([ROSE, GOLD, INK])
        add(blade(x, h, lean, random.uniform(0.7, 1.2), c, random.uniform(0.30, 0.52) if c != INK else 0.25))
    step = (W - 26) / max(flowers_n - 1, 1)
    for k in range(flowers_n):
        x = 13 + k * step + random.uniform(-5, 5); h = random.uniform(14, 30) * VS; lean = random.uniform(-5, 5)
        tipx, tipy, d = stem_path(x, h, lean)
        add(f'<path d="{d}" fill="none" stroke="{ROSE}" stroke-width="0.5" stroke-opacity="0.7" stroke-linecap="round"/>')
        add(flower(tipx, tipy, random.uniform(2.4, 3.6), random.choice([ROSE, ROSE_SOFT, "#FFFFFF"]), GOLD,
                   n=5, opacity=0.92, rot0=random.uniform(0, math.pi)))
    for _ in range(26):
        x = random.uniform(6, W - 6); y = random.uniform(132 * VS, 196 * VS); r = random.uniform(0.4, 0.9)
        c = random.choice([GOLD, ROSE_SOFT])
        add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{c}" fill-opacity="{random.uniform(0.25,0.55):.2f}"/>')


def gold_rule(add, cx, y, half=26):
    add(f'<line x1="{cx-half}" y1="{y}" x2="{cx-3.5}" y2="{y}" stroke="{GOLD}" stroke-width="0.35"/>')
    add(f'<line x1="{cx+3.5}" y1="{y}" x2="{cx+half}" y2="{y}" stroke="{GOLD}" stroke-width="0.35"/>')
    add(f'<rect x="{cx-1.2}" y="{y-1.2}" width="2.4" height="2.4" transform="rotate(45 {cx} {y})" fill="{GOLD}"/>')


def txt(x, y, size, fill, s, *, bold=False, italic=False, ls=None, anchor="middle"):
    b = ' font-weight="bold"' if bold else ''
    i = ' font-style="italic"' if italic else ''
    l = f' letter-spacing="{ls}"' if ls is not None else ''
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{SERIF}" '
            f'font-size="{size}"{b}{i}{l} fill="{fill}">{s}</text>')


def render(svg, name):
    open(f"{name}.svg", "w", encoding="utf-8").write(svg)
    subprocess.run(["rsvg-convert", "-f", "pdf", "-o", f"{name}.pdf", f"{name}.svg"], check=True)
    subprocess.run(["rsvg-convert", "-f", "png", "--dpi-x", "300", "--dpi-y", "300",
                    "-o", f"{name}.png", f"{name}.svg"], check=True)


# ================= FRONT (per volume) =================
for v, (roman, title) in VOLS.items():
    random.seed(20260927)
    p = header(); add = p.append
    meadow(add, dense=1.0, flowers_n=9, halo_x=W * 0.72)
    add(txt(CX, 66, 12.4, ROSE, "Philosophy of Intimacy", bold=True))
    add(txt(CX, 79, 9.0, ROSE, "and the Theory of Justice"))
    gold_rule(add, CX, 89)
    add(txt(CX, 100, 5.7, INK, "Studies in Generative Relational Being", italic=True))
    add(txt(CX, 124, 6.5, ROSE, f"VOLUME&#160;{roman}", ls="2.6"))
    add(txt(CX, 133, 4.7, INK, title, italic=True))
    add(txt(CX, 156, 6.0, INK, "WANHONG HUANG", ls="1.1"))
    add(txt(CX, 169, 4.7, ROSE, "First Edition", ls="1.9"))
    add("</svg>")
    render("\n".join(p), f"cover_front_vol{v}")
    print(f"front vol{v} -> svg/pdf/png")

# ================= BACK (shared; no SCS) =================
random.seed(1996)
p = header(); add = p.append
meadow(add, dense=0.95, flowers_n=8, halo_x=W * 0.30)
MARGIN, CHARS, LINE = 27.0, 62, 5.3
blurb = [
 "Intimate relationships form a small yet structurally complete relational system. Recognition and misrecognition, co-presence and symbolic mediation, joint decision and asymmetries of power, the generation and alienation of value, care and vulnerability, eros and justice: all appear here in highly condensed form, as in a tabletop experiment whose laws govern far larger social systems.",
 "This series studies intimacy as a research instance of generative relational being. Drawing on feminist thought, jurisprudence, Kant and Hegel, structural linguistics, Lacanian psychoanalysis, developmental psychology and neuroscience, the theory of epistemic injustice, and generative justice, it seeks the generative mechanisms and the claims of justice that run through all relational systems.",
 "How we treat those closest to us is our most honest answer to the question of justice.",
]
y = 44.0
for pi, para in enumerate(blurb):
    it = (pi == 2)
    size = 4.0 if pi < 2 else 4.2
    for line in textwrap.wrap(para, CHARS):
        add(txt(MARGIN, y, size, INK, line, italic=it, anchor="start"))
        y += LINE
    y += 2.6
gold_rule(add, CX, y + 1.0, half=18)
y += 9
add(txt(CX, y, 3.9, INK, "The source of this series is openly available;", italic=True)); y += 5.2
add(txt(CX, y, 3.9, INK, "readers are invited to read, contest, continue, and rewrite.", italic=True))
add("</svg>")
render("\n".join(p), "cover_back_book")
print("back -> svg/pdf/png (no SCS)")

print(f"\ntrim {TRIM_W}x{TRIM_H}mm (+{BLEED}mm bleed) => {W}x{H}mm")
