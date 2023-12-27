#!/usr/bin/env python3
"""
Author : tom <tom@localhost>
Date   : 2023-12-27
Purpose: Use `a` or `an` before a chosen word in a sentence.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Choose an object the sailor noticed",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "word",
        metavar="word",
        help="Any word",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.word
    # vowels = ["a", "e", "i", "o", "u"]
    # we can use the array approach or string as lower
    if pos_arg.strip().lower()[0] in "aeiou":
        article = "an"
    else:
        article = "a"
    """
        the if statement can be rewritten using `if expression`
        
        article = "a" if word.strip().lower()[0] in "aeiou" else "an"   
    """
    print(f"Ahoy, Captain, {article} {pos_arg} off the larboard bow!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
