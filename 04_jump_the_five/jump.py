#!/usr/bin/env python3
"""
Author : tom <tom@localhost>
Date   : 2024-01-06
Purpose: Dictionary practice
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("input_text", metavar="str", help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sentence = args.input_text
    translator = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }
    # rebuilding the sentence
    new_chars = []

    for char in sentence:
        # get value from dictionary, if not in dictionary, value remains the same, the second char is the default value
        # create a list of changed or unchanged characters
        new_chars.append(translator.get(char, char))

    new_sentence = "".join(new_chars)

    print(new_sentence)


# --------------------------------------------------
if __name__ == "__main__":
    main()
