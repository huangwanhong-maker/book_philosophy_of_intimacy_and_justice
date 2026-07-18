import re, glob, os, sys

# Repo-relative: this file lives in book_src/tools/, papers are ../papers/.
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "papers"))

hits = []
for t in sorted(glob.glob("paper_*/**/*.tex", recursive=True)):
    if t.endswith('content.tex'):
        continue
    for i, line in enumerate(open(t, encoding='utf-8', errors='replace'), 1):
        s = re.sub(r'(?<!\\)%.*', '', line)          # ignore commented-out
        m = re.search(r'\\(todo|TODO)\s*\{', s)
        if m:
            # pull the argument
            j = s.index('{', m.start())
            depth, k = 0, j
            for k in range(j, len(s)):
                if s[k] == '{': depth += 1
                elif s[k] == '}':
                    depth -= 1
                    if depth == 0: break
            arg = s[j+1:k]
            hits.append((t, i, arg.strip()))

by_paper = {}
for t, i, arg in hits:
    by_paper.setdefault(t.split('/')[0], []).append((t, i, arg))

print(f"UNRESOLVED \\todo IN THE MANUSCRIPT: {len(hits)} in {len(by_paper)} papers\n")
for p in sorted(by_paper):
    print(f"{p}  ({len(by_paper[p])})")
    for t, i, arg in by_paper[p]:
        f = t.split('/', 1)[1]
        print(f"   {f}:{i}")
        print(f"      {arg[:150]}")
    print()

# Non-zero exit if any remain, so `make todo-check` gates the book build.
sys.exit(1 if hits else 0)
