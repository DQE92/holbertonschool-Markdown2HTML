#!/usr/bin/python3
    """
    The above Python script is a command-line tool that converts a Markdown file to an HTML file.
    """

import sys
import os


def main() -> None:
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    in_md = sys.argv[1]
    out_html = sys.argv[2]

    if not os.path.exists(in_md):
        sys.stderr.write(f"Missing {in_md}\n")
        sys.exit(1)

    try:
        with open(out_html, "w", encoding="utf-8"):
            pass
    except OSError:
        sys.exit(1)

    sys.exit(0)

    open(in_md, mode="r", encoding="utf-8")
    
    
    
if __name__ == "__main__":
    main()