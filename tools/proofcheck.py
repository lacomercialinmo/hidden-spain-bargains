"""Automatic proofreading checks run on every build. Fails the build on hard errors."""
import glob, html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")

BANNED = [r"idealista"]                        # never mention (owner's rule)
HARD = [
    (r"\b(\w+) \1\b", "repeated word"),
    (r"\.\.(?!\.)", "double full stop"),
    (r" ,", "space before comma"),
    (r"\{F\(|\{Fc\(|None\b", "unrendered template"),
    (r"[.!?] [a-z]", "lowercase after full stop"),
]
SOFT = [
    (r"\b(cheap|cheapest)\b", "word 'cheap' (brand tone: prefer 'affordable'/'bargain')"),
    (r"\b(guarantee|guaranteed)\b", "promise wording"),
]

def text_of(path):
    s = open(path, encoding="utf-8").read()
    s = re.sub(r"<script.*?</script>|<style.*?</style>", " ", s, flags=re.S)
    s = re.sub(r"</?(h[1-6]|p|li|td|th|tr|div|summary|details|figcaption|option|span|b|em|a|label|button|section|header|footer|nav|ul|ol|table|select|i)\b[^>]*>", " ¶ ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s))

def run(strict=True):
    hard, soft = [], []
    for f in sorted(glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True)):
        rel = os.path.relpath(f, SITE)
        raw = open(f, encoding="utf-8").read()
        t = text_of(f)
        for b in BANNED:
            if re.search(b, raw, re.I):
                hard.append(f"{rel}: banned term '{b}'")
        for rx, label in HARD:
            for m in re.finditer(rx, t):
                ctx = t[max(0, m.start() - 30): m.end() + 30]
                if label == "lowercase after full stop" and re.search(r"(e\.g|i\.e|approx|vs|m²|No|Min|Max)\. [a-z€]", ctx):
                    continue
                hard.append(f"{rel}: {label}: …{ctx}…")
        for rx, label in SOFT:
            for m in re.finditer(rx, t, re.I):
                soft.append(f"{rel}: {label}: …{t[max(0, m.start() - 30): m.end() + 30]}…")
    for s in soft:
        print("WARN", s)
    if hard:
        print("\n".join("ERROR " + h for h in hard))
        if strict:
            raise SystemExit(f"Proofreading found {len(hard)} error(s). Fix them before publishing.")
    print(f"proofcheck: {len(hard)} errors, {len(soft)} warnings")

if __name__ == "__main__":
    run()
