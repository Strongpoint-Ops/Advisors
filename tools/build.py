#!/usr/bin/env python3
"""Re-copy index.html's <style> block into the other pages.

Every page here is self-contained on purpose — no <link rel=stylesheet>, no
shared asset files — which is what keeps this site a no-build-step site. The
cost of that choice is four copies of the same design tokens, and four copies
drift. This script is the cheap fix: edit the <style> block in index.html,
run this, and the other pages match again.

It is an AUTHORING convenience, not a build step. The committed HTML is always
already correct; nothing has to run before a deploy.

    python3 tools/build.py            # rewrite the other pages
    python3 tools/build.py --check    # exit 1 if any page has drifted

Each page keeps its own page-specific <style> block (the second one), which is
left untouched.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "site"
SOURCE = "index.html"
TARGETS = ["contact.html", "404.html"]
STYLE = re.compile(r"<style>[\s\S]*?</style>")


def shared_block(text):
    """The first <style> block on a page is the shared one."""
    m = STYLE.search(text)
    if not m:
        raise SystemExit("no <style> block found")
    return m


def main():
    check = "--check" in sys.argv
    src = (ROOT / SOURCE).read_text()
    block = shared_block(src).group(0)

    drifted, rewritten = [], []
    for name in TARGETS:
        path = ROOT / name
        text = path.read_text()
        m = shared_block(text)
        if m.group(0) == block:
            continue
        drifted.append(name)
        if not check:
            path.write_text(text[: m.start()] + block + text[m.end() :])
            rewritten.append(name)

    if check:
        if drifted:
            print("drifted from %s: %s" % (SOURCE, ", ".join(drifted)))
            return 1
        print("all pages match %s" % SOURCE)
        return 0

    print("rewritten: %s" % (", ".join(rewritten) or "nothing — already in sync"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
