#!/usr/bin/env python3
"""
Author : tom <tom@localhost>
Date   : 2024-02-25
Purpose: Bottles of beer song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Bottles of beer song",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n", "--num", help="How many bottles", metavar="number", type=int, default=10
    )

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    def create_verse(num):
        plural = "s" if num > 1 else ""
        text = f"{num} bottle{plural} of beer on the wall,\n"
        text += f"{num} bottle{plural} of beer,\n"
        text += "Take one down, pass it around,\n"
        if num > 1:
            plural = "" if num == 2 else "s"
            text += f"{num - 1} bottle{plural} of beer on the wall!\n"
        if num == 1:
            text += f"No more bottles of beer on the wall!"
        return text

    for i in range(args.num, 0, -1):
        print(create_verse(i))


# --------------------------------------------------
if __name__ == "__main__":
    main()
