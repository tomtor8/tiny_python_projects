#!/usr/bin/env python3
"""
Author : tom <tom@localhost>
Date   : 2023-12-30
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="List of picnic items",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-s",
        "--sorted",
        default=False,
        # if this argument is chosen, True is stored in the variable
        action="store_true",
        help="Sort the items",
    )

    # nargs="+" accept one or more positional values
    parser.add_argument(
        "items", metavar="items", nargs="+", type=str, help="Item(s) to bring"
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    list_of_items = args.items
    sorted_option = args.sorted

    if sorted_option:
        list_of_items.sort()

    items_length = len(list_of_items)

    bringing = ""
    if items_length == 1:
        bringing = list_of_items[0]
    elif items_length == 2:
        bringing = " and ".join(list_of_items)
    else:
        bringing = f"{list_of_items[0]}, "

        for i in range(1, items_length - 1):
            bringing += f"{list_of_items[i]}, "

        bringing += f"and {list_of_items[-1]}"

    print(f"You are bringing {bringing}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
