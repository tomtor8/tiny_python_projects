#!/usr/bin/env python3
"""
Author : tom <tom@localhost>
Date   : 2024-01-11
Purpose: Rock the Casbah
"""

import argparse, os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", help="Input string or file")

    parser.add_argument(
        "-o", "--outfile", help="Output filename", metavar="str", type=str, default=""
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    outfile = args.outfile

    if os.path.isfile(text):
        with open(text) as fi:
            final_text = fi.read().upper()
    else:
        final_text = text.upper()

    if outfile:
        with open(outfile, "wt") as fi:
            fi.write(final_text)
    else:
        print(final_text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
