#!/usr/bin/env python3
"""
strip_changes.py -- Collapse `changes` package markup in LaTeX source.

Rewrites:
    \\added[opts]{X}        -> X
    \\deleted[opts]{X}      ->
    \\replaced[opts]{N}{O}  -> N
    \\highlight[opts]{X}    -> X
    \\comment[opts]{X}      ->

The optional [opts] is brace-aware (supports comment={...} containing
commas/braces). Arguments are brace-aware and tolerate nested {} and \\{.

Run:
    python3 tools/strip_changes.py FILE [FILE ...]
    python3 tools/strip_changes.py --in-place FILE [FILE ...]
"""

from __future__ import annotations
import argparse
import sys
from pathlib import Path

MACROS = {
    "added":     ("keep", 1),
    "deleted":   ("drop", 1),
    "replaced":  ("first", 2),
    "highlight": ("keep", 1),
    "comment":   ("drop", 1),
}


def skip_optional(s: str, i: int) -> int:
    """If s[i] == '[', consume balanced [...] (brace-aware) and return new index.
       Otherwise return i unchanged."""
    if i >= len(s) or s[i] != "[":
        return i
    depth_brace = 0
    j = i + 1
    while j < len(s):
        c = s[j]
        if c == "\\" and j + 1 < len(s):
            j += 2
            continue
        if c == "{":
            depth_brace += 1
        elif c == "}":
            depth_brace -= 1
        elif c == "]" and depth_brace == 0:
            return j + 1
        j += 1
    raise ValueError(f"Unbalanced '[' starting at {i}")


def read_braced(s: str, i: int) -> tuple[str, int]:
    """Expect s[i] == '{'. Return (inner, index_after_closing_brace)."""
    if i >= len(s) or s[i] != "{":
        raise ValueError(f"Expected '{{' at {i}, got {s[i:i+10]!r}")
    depth = 1
    j = i + 1
    start = j
    while j < len(s):
        c = s[j]
        if c == "\\" and j + 1 < len(s):
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[start:j], j + 1
        j += 1
    raise ValueError(f"Unbalanced '{{' starting at {i}")


def strip(src: str) -> str:
    out = []
    i = 0
    n = len(src)
    while i < n:
        c = src[i]
        # Skip line comments verbatim (but copy them).
        if c == "%" and (i == 0 or src[i - 1] != "\\"):
            j = src.find("\n", i)
            if j == -1:
                out.append(src[i:])
                return "".join(out)
            out.append(src[i:j + 1])
            i = j + 1
            continue
        if c == "\\":
            # Find the macro name.
            j = i + 1
            while j < n and (src[j].isalpha()):
                j += 1
            name = src[i + 1:j]
            if name in MACROS:
                action, nargs = MACROS[name]
                # Optional skip whitespace, then [opts]
                k = j
                while k < n and src[k] in " \t":
                    k += 1
                k = skip_optional(src, k)
                # Read N braced args.
                args = []
                for _ in range(nargs):
                    while k < n and src[k] in " \t\n":
                        k += 1
                    if k >= n or src[k] != "{":
                        # Not a real changes macro call; bail out and copy literally.
                        args = None
                        break
                    inner, k = read_braced(src, k)
                    args.append(inner)
                if args is None:
                    out.append(src[i:j])
                    i = j
                    continue
                if action == "keep":
                    out.append(strip(args[0]))
                elif action == "first":
                    out.append(strip(args[0]))
                # action == "drop": emit nothing
                i = k
                continue
            else:
                # Some other macro -- copy \name and let outer loop handle the rest.
                out.append(src[i:j])
                i = j
                continue
        out.append(c)
        i += 1
    return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--in-place", action="store_true",
                    help="Overwrite files; otherwise print to stdout.")
    ap.add_argument("--suffix", default=".bak",
                    help="Backup suffix when using --in-place (default: .bak). "
                         "Pass empty string to skip backup.")
    args = ap.parse_args()

    for path in args.files:
        src = path.read_text(encoding="utf-8")
        out = strip(src)
        if args.in_place:
            if args.suffix:
                path.with_suffix(path.suffix + args.suffix).write_text(src, encoding="utf-8")
            path.write_text(out, encoding="utf-8")
            print(f"stripped {path}", file=sys.stderr)
        else:
            sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
