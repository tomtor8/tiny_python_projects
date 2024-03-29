#!/usr/bin/env python3
"""
Author : tom <tom@localhost>
Date   : 2024-03-17
Purpose: Twelve Days of Christmas
"""

import argparse, sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Twelve Days of Christmas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--num",
        help="Number of days to sing",
        metavar="days",
        type=int,
        default=12,
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Outfile",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    args = parser.parse_args()

    if args.num < 1 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    ordinals = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "nineth",
        10: "tenth",
        11: "eleventh",
        12: "twelveth",
    }

    gifts = [
        "And a partridge in a pear tree.",
        "Two turtle doves,",
        "Three French hens,",
        "Four calling birds,",
        "Five gold rings,",
        "Six geese a laying,",
        "Seven swans a swimming,",
        "Eight maids a milking,",
        "Nine ladies dancing,",
        "Ten lords a leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,",
    ]

    def verse(num):
        text = f"On the {ordinals[num]} day of Christmas,\n"
        text += "My true love gave to me,\n"
        if num == 1:
            text += "A partridge in a pear tree.\n"
        if num > 1:
            list_of_gifts = [gifts[i] for i in range(num)]
            text += "\n".join(reversed(list_of_gifts))
            text += "\n\n"
        return text

    for num in range(args.num):
        if args.outfile:
            args.outfile.write(verse(num + 1))
        else:
            print(verse(num + 1))


# --------------------------------------------------
if __name__ == "__main__":
    main()
