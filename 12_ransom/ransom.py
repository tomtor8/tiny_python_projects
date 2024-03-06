#!/usr/bin/env python3
"""
Author : tom <tom@localhost>
Date   : 2024-03-06
Purpose: Ransom note
"""

import argparse, random, os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Ransom note",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-s", "--seed", help="Random seed", metavar="int", type=int, default=None
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().strip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if args.seed:
        random.seed(args.seed)

    text_to_list = list(args.text)

    # this function is used only for the map method below
    def case_changer(char):
        return char.upper() if random.random() < 0.5 else char.lower()

    # 1. CLASSICAL METHOD
    # new_list = []

    # for char in text_to_list:
    #     # toss a coin to decide to change case
    #     processed_char = char.upper() if random.random() < 0.5 else char
    #     new_list.append(processed_char)

    # 2. LIST COMPREHENSION METHOD
    # new_list = [
    #     char.upper() if random.random() < 0.5 else char.lower() for char in text_to_list
    # ]

    # 3. MAP METHOD

    new_list = map(case_changer, text_to_list)

    print("".join(new_list))


# --------------------------------------------------
if __name__ == "__main__":
    main()
