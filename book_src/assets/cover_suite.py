#!/usr/bin/env python3
# Cover suite: front (revised typography), back, spine
# Philosophy of Intimacy and the Theory of Justice
# A5 + 3mm bleed = 154 x 216 mm ; spine width parameterized
import math, random, textwrap
import cairosvg

W, H = 154.0, 216.0
SPINE_W = 14.0
BLUSH      = "#FDF2F4"
BLUSH_DEEP = "#F7E2E7"
ROSE       = "#9E4256"
ROSE_SOFT  = "#C4798B"
GOLD       = "#B08A4C"
INK        = "#342E37"
SERIF = "TeX Gyre Pagella"
GROUND = H

# ---------------- shared drawing helpers ----------------
def blade(x, h, lean, width, color, opacity):
    tipx, tipy = x + lean, GROUND - h
    c1x, c1y = x + lean * 0.25, GROUND - h * 0.45
    c2x, c2y = x + lean * 0.7,  GROUND - h * 0.85
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

def flower(cx, cy, r, petal_color, center_color, n=5, opacity=0.95, rot0=0.0):
    s = []
    for i in range(n):
        a = rot0 + i * 2 * math.pi / n
        px, py = cx + math.cos(a) * r * 0.62, cy + math.sin(a) * r * 0.62
        s.append(f'<ellipse cx="{px:.2f}" cy="{py:.2f}" rx="{r*0.55:.2f}" ry="{r*0.38:.2f}" '
                 f'transform="rotate({math.degrees(a):.1f} {px:.2f} {py:.2f})" '
                 f'fill="{petal_color}" fill-opacity="{opacity:.2f}"/>')
    s.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r*0.22:.2f}" fill="{center_color}"/>')
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

def header(width, height):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}mm" height="{height}mm" viewBox="0 0 {width} {height}">',
            f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="{BLUSH}"/>
  <stop offset="0.62" stop-color="{BLUSH}"/>
  <stop offset="1" stop-color="{BLUSH_DEEP}"/>
</linearGradient>
<radialGradient id="moon" cx="0.5" cy="0.5" r="0.5">
  <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.55"/>
  <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
</radialGradient>
</defs>''',
            f'<rect x="0" y="0" width="{width}" height="{height}" fill="url(#bg)"/>']

def meadow(add, dense=1.0, flowers_n=8, halo_x=None):
    if halo_x is not None:
        add(f'<circle cx="{halo_x}" cy="150" r="42" fill="url(#moon)"/>')
    for i in range(int(120 * dense)):
        x = random.uniform(-4, W + 4)
        h = random.uniform(28, 54)
        lean = random.uniform(-9, 9)
        c = random.choice([ROSE_SOFT, GOLD, ROSE_SOFT])
        add(blade(x, h, lean, random.uniform(0.5, 0.9), c, random.uniform(0.16, 0.30)))
    for i in range(int(34 * dense)):
        x = random.uniform(2, W - 2)
        h = random.uniform(20, 40)
        lean = random.uniform(-7, 7)
        color = random.choice([GOLD, ROSE, ROSE_SOFT])
        tipx, tipy, d = stem_path(x, h, lean)
        add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="0.45" stroke-opacity="0.6" stroke-linecap="round"/>')
        kind = random.random()
        if kind < 0.38:
            add(seedhead(tipx, tipy, random.uniform(2.2, 3.4), GOLD if color != GOLD else ROSE_SOFT))
        elif kind < 0.62:
            add(f'<circle cx="{tipx:.2f}" cy="{tipy:.2f}" r="{random.uniform(0.8,1.3):.2f}" fill="{ROSE}" fill-opacity="0.8"/>')
        if random.random() < 0.6:
            add(leaf(x + lean * 0.3, GROUND - h * 0.45, random.choice([-150, -30]) + random.uniform(-12, 12),
                     random.uniform(4, 7), color, 0.35))
    for i in range(int(80 * dense)):
        x = random.uniform(-3, W + 3)
        h = random.uniform(8, 24)
        lean = random.uniform(-5, 5)
        c = random.choice([ROSE, GOLD, INK])
        add(blade(x, h, lean, random.uniform(0.7, 1.2), c, random.uniform(0.30, 0.52) if c != INK else 0.25))
    step = (W - 22) / max(flowers_n - 1, 1)
    for k in range(flowers_n):
        x = 11 + k * step + random.uniform(-5, 5)
        h = random.uniform(14, 30)
        lean = random.uniform(-5, 5)
        tipx, tipy, d = stem_path(x, h, lean)
        add(f'<path d="{d}" fill="none" stroke="{ROSE}" stroke-width="0.5" stroke-opacity="0.7" stroke-linecap="round"/>')
        r = random.uniform(2.4, 3.6)
        petal = random.choice([ROSE, ROSE_SOFT, "#FFFFFF"])
        add(flower(tipx, tipy, r, petal, GOLD, n=5, opacity=0.92, rot0=random.uniform(0, math.pi)))
    for i in range(22):
        x = random.uniform(6, W - 6)
        y = random.uniform(132, 196)
        r = random.uniform(0.4, 0.9)
        c = random.choice([GOLD, ROSE_SOFT])
        add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{c}" fill-opacity="{random.uniform(0.25,0.55):.2f}"/>')

def gold_rule(add, cx, y, half=22):
    add(f'<line x1="{cx-half}" y1="{y}" x2="{cx-3}" y2="{y}" stroke="{GOLD}" stroke-width="0.35"/>')
    add(f'<line x1="{cx+3}" y1="{y}" x2="{cx+half}" y2="{y}" stroke="{GOLD}" stroke-width="0.35"/>')
    add(f'<rect x="{cx-1.1}" y="{y-1.1}" width="2.2" height="2.2" transform="rotate(45 {cx} {y})" fill="{GOLD}"/>')

def write_all(svg, name):
    open(f"/mnt/user-data/outputs/{name}.svg", "w").write(svg)
    cairosvg.svg2pdf(bytestring=svg.encode(), write_to=f"/mnt/user-data/outputs/{name}.pdf")
    wmm = float(svg.split('width="')[1].split('mm')[0])
    hmm = float(svg.split('height="')[1].split('mm')[0])
    px = int(round(wmm / 25.4 * 300))
    py = int(round(hmm / 25.4 * 300))
    cairosvg.svg2png(bytestring=svg.encode(), write_to=f"/mnt/user-data/outputs/{name}.png",
                     output_width=px, output_height=py)

# ================= FRONT =================
random.seed(20260927)
parts = header(W, H)
add = parts.append
meadow(add, dense=1.0, flowers_n=8, halo_x=W * 0.72)
CX = W / 2
# revised typography: smaller, wider margins
add(f'<text x="{CX}" y="50" text-anchor="middle" font-family="{SERIF}" font-size="10.2" '
    f'fill="{ROSE}" font-weight="bold">Philosophy of Intimacy</text>')
add(f'<text x="{CX}" y="60" text-anchor="middle" font-family="{SERIF}" font-size="7.4" '
    f'fill="{ROSE}">and the Theory of Justice</text>')
gold_rule(add, CX, 68.5, half=20)
add(f'<text x="{CX}" y="77" text-anchor="middle" font-family="{SERIF}" font-size="4.8" '
    f'font-style="italic" fill="{INK}" fill-opacity="0.85">Studies in Generative Relational Being</text>')
add(f'<text x="{CX}" y="120" text-anchor="middle" font-family="{SERIF}" font-size="5.0" '
    f'fill="{INK}" letter-spacing="0.9">WANHONG HUANG</text>')
add('</svg>')
write_all("\n".join(parts), "cover_front")

# ================= BACK =================
random.seed(1996)  # a different meadow, same family
parts = header(W, H)
add = parts.append
meadow(add, dense=0.95, flowers_n=7, halo_x=W * 0.30)

MARGIN = 21.0
TEXT_W_CHARS = 54
blurb = [
"Intimate relationships form a small yet structurally complete relational system. Recognition and misrecognition, co-presence and symbolic mediation, joint decision and asymmetries of power, the generation and alienation of value, care and vulnerability, eros and justice: all appear here in highly condensed form, as in a tabletop experiment whose laws govern far larger social systems.",
"This series studies intimacy as a research instance of generative relational being. Drawing on feminist thought, jurisprudence, Kant and Hegel, structural linguistics, Lacanian psychoanalysis, developmental psychology and neuroscience, the theory of epistemic injustice, and generative justice, it seeks the generative mechanisms and the claims of justice that run through all relational systems.",
"How we treat those closest to us is our most honest answer to the question of justice.",
]
y = 38.0
LINE = 5.3
for pi, para in enumerate(blurb):
    italic = ' font-style="italic"' if pi == 2 else ''
    size = 4.0 if pi < 2 else 4.2
    for line in textwrap.wrap(para, TEXT_W_CHARS):
        add(f'<text x="{MARGIN}" y="{y:.1f}" font-family="{SERIF}" font-size="{size}"{italic} '
            f'fill="{INK}" fill-opacity="0.92">{line}</text>')
        y += LINE
    y += 2.6

gold_rule(add, W / 2, y + 1.0, half=16)
y += 9
add(f'<text x="{W/2}" y="{y:.1f}" text-anchor="middle" font-family="{SERIF}" font-size="3.9" '
    f'font-style="italic" fill="{INK}" fill-opacity="0.8">The source of this series is openly available;</text>')
y += 5.2
add(f'<text x="{W/2}" y="{y:.1f}" text-anchor="middle" font-family="{SERIF}" font-size="3.9" '
    f'font-style="italic" fill="{INK}" fill-opacity="0.8">readers are invited to read, contest, continue, and rewrite.</text>')
y += 9
add(f'<text x="{W/2}" y="{y:.1f}" text-anchor="middle" font-family="{SERIF}" font-size="3.8" '
    f'fill="{ROSE}" letter-spacing="0.6">SERENDIP COMMONS SOCIETY \u00b7 TOKYO</text>')
add('</svg>')
write_all("\n".join(parts), "cover_back")

# ================= SPINE =================
random.seed(7)
parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{SPINE_W}mm" height="{H}mm" viewBox="0 0 {SPINE_W} {H}">',
         f'''<defs><linearGradient id="bgs" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="{BLUSH}"/><stop offset="0.62" stop-color="{BLUSH}"/>
<stop offset="1" stop-color="{BLUSH_DEEP}"/></linearGradient></defs>''',
         f'<rect x="0" y="0" width="{SPINE_W}" height="{H}" fill="url(#bgs)"/>']
add = parts.append
# tiny meadow at spine foot
for i in range(16):
    x = random.uniform(0, SPINE_W)
    h = random.uniform(5, 14)
    lean = random.uniform(-2, 2)
    c = random.choice([ROSE, GOLD, ROSE_SOFT])
    add(blade(x, h, lean, random.uniform(0.4, 0.7), c, random.uniform(0.3, 0.5)))
tipx, tipy, d = stem_path(SPINE_W / 2, 11, 1.0)
add(f'<path d="{d}" fill="none" stroke="{ROSE}" stroke-width="0.45" stroke-opacity="0.75" stroke-linecap="round"/>')
add(flower(tipx, tipy, 2.0, ROSE_SOFT, GOLD))
cx = SPINE_W / 2
# diamond ornament near the head
add(f'<rect x="{cx-0.9}" y="13.1" width="1.8" height="1.8" transform="rotate(45 {cx} 14)" fill="{GOLD}"/>')
# title reading top-to-bottom
add(f'<text x="{cx}" y="0" font-family="{SERIF}" font-size="4.6" font-weight="bold" fill="{ROSE}" '
    f'text-anchor="middle" transform="translate(1.0,0) rotate(90 {cx} 0) translate(0,{-(0)})" '
    f'transform-origin="{cx} 0">'
    f'</text>')
add(f'<text font-family="{SERIF}" font-size="4.4" font-weight="bold" fill="{ROSE}" '
    f'transform="translate({cx+1.55},19) rotate(90)">Philosophy of Intimacy and the Theory of Justice</text>')
add(f'<text font-family="{SERIF}" font-size="3.4" fill="{INK}" letter-spacing="0.5" '
    f'transform="translate({cx+1.2},152) rotate(90)">WANHONG HUANG</text>')
add('</svg>')
write_all("\n".join(parts), "cover_spine")

print("front, back, spine written (svg/pdf/png each)")
