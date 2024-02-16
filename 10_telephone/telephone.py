#!/usr/bin/env python3
"""
Author : tom <tom@localhost>
Date   : 2024-02-16
Purpose: Telephone
"""

import argparse, os, random, string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Telephone", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-s", "--seed", help="Random seed", metavar="seed", type=int, default=None
    )

    parser.add_argument(
        "-m",
        "--mutations",
        help="Percent mutations",
        metavar="mutations",
        type=float,
        default=0.1,
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().strip()

    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    text = args.text
    text_list = list(text)
    mutation = args.mutations
    num_mut_chars = int(round(len(text) * mutation))

    # mutate characters
    for _ in range(num_mut_chars):
        # create a set of indices the length of the text
        used_indices = []
        while True:
            rand_index = random.randint(0, len(text) - 1)
            if rand_index in used_indices:
                continue
            used_indices.append(rand_index)
            # choose random letter from all printable ASCII characters using module string
            # random letter cannot be the same as the replaced character
            rand_letter = random.choice(string.ascii_letters + string.punctuation)
            if rand_letter != text_list[rand_index]:
                text_list[rand_index] = rand_letter
                break
            else:
                continue

    mutated_text = "".join(text_list)

    print(f'You said: "{text}"\nI heard : "{mutated_text}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
