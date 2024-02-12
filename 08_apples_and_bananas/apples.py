#!/usr/bin/env python3
"""
Author : tom <tom@localhost>
Date   : 2024-02-12
Purpose: Rock the Casbah
"""

import argparse, os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Apples and bananas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-v",
        "--vowel",
        help="The vowel to substitute",
        metavar="vowel",
        type=str,
        default="a",
        choices=["a", "e", "i", "o", "u"],
    )

    parser.add_argument("text", metavar="text", help="Input text or file")
    if parser.parse_args().vowel not in ["a", "e", "i", "o", "u"]:
        print("invalid choice: choose from 'a', 'e', 'i', 'o', 'u'")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel

    for i in list("aeiou"):
        text = text.replace(i, vowel)

    for i in list("AEIOU"):
        text = text.replace(i, vowel.upper())

    print(text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
