"""Revise the designed cover SVGs for the three-volume book:
  - front: add a VOLUME N line + volume title (keep the WANHONG HUANG author line)
  - back:  remove the 'SERENDIP COMMONS SOCIETY · TOKYO' line (SCS unnecessary)
Meadow/moon art is preserved verbatim (edit the shipped SVGs, don't regenerate).
Then convert each to PDF with rsvg-convert."""
import re, os, subprocess

import os as _os
A = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "assets")
os.chdir(A)

ROSE, INK = "#9E4256", "#342E37"
VOLS = {
    1: ("I",   "Relational Being, the Subject, and the Word"),
    2: ("II",  "Generativity, Value, and Power"),
    3: ("III", "Happiness, Ethics, Aesthetics, and Culture"),
}

# Re-trim the A5+bleed art (154x216) to B5+3mm bleed (182x256). The two aspect
# ratios are within 0.3%, so preserveAspectRatio="none" stretches imperceptibly.
def to_b5(svg):
    return svg.replace(
        '<svg xmlns="http://www.w3.org/2000/svg" width="154.0mm" height="216.0mm" viewBox="0 0 154.0 216.0">',
        '<svg xmlns="http://www.w3.org/2000/svg" width="182mm" height="256mm" viewBox="0 0 154.0 216.0" preserveAspectRatio="none">')

# ---------- FRONT (per volume) ----------
front = open("cover_front.svg", encoding="utf-8").read()
author_line = ('<text x="77.0" y="120" text-anchor="middle" font-family="TeX Gyre Pagella" '
               'font-size="5.0" fill="#342E37" letter-spacing="0.9">WANHONG HUANG</text>')
assert author_line in front, "author line not found"

for v, (roman, title) in VOLS.items():
    vol_block = (
        f'<text x="77.0" y="95" text-anchor="middle" font-family="TeX Gyre Pagella" '
        f'font-size="5.4" fill="{ROSE}" letter-spacing="2.2">VOLUME {roman}</text>\n'
        f'<text x="77.0" y="102.4" text-anchor="middle" font-family="TeX Gyre Pagella" '
        f'font-size="3.9" font-style="italic" fill="{INK}" fill-opacity="0.9">{title}</text>\n'
    )
    edition_line = (
        f'\n<text x="77.0" y="131.5" text-anchor="middle" font-family="TeX Gyre Pagella" '
        f'font-size="3.9" fill="{ROSE}" letter-spacing="1.6">First Edition</text>'
    )
    svg = to_b5(front.replace(author_line, vol_block + author_line + edition_line))
    out = f"cover_front_vol{v}.svg"
    open(out, "w", encoding="utf-8").write(svg)
    subprocess.run(["rsvg-convert", "-f", "pdf", "-o", f"cover_front_vol{v}.pdf", out], check=True)
    print("wrote", out, "-> pdf")

# ---------- BACK (shared; SCS removed) ----------
back = open("cover_back.svg", encoding="utf-8").read()
scs = re.search(r'<text[^>]*>SERENDIP COMMONS SOCIETY[^<]*</text>\n?', back)
assert scs, "SCS line not found"
back2 = back[:scs.start()] + back[scs.end():]
back2 = to_b5(back2)
open("cover_back_book.svg", "w", encoding="utf-8").write(back2)
subprocess.run(["rsvg-convert", "-f", "pdf", "-o", "cover_back_book.pdf", "cover_back_book.svg"], check=True)
print("wrote cover_back_book.svg -> pdf (SCS removed)")

print("\ngenerated:", [f for f in sorted(os.listdir('.')) if f.startswith('cover_front_vol') or f == 'cover_back_book.pdf'])
