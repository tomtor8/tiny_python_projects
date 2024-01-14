#!/usr/bin/env python3
"""
Author : tom <tom@localhost>
Date   : 2024-01-14
Purpose: Emulate word count
"""

import argparse, sys, os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        # zero or more arguments, a LIST of open file handles is returned
        nargs="*",
        help="Input file(s)",
        metavar="FILE",
        type=argparse.FileType("rt"),  # readable text files
        # if there is no input, a LIST containing STDIN will be default
        default=[sys.stdin],
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    files_list = args.file

    total_lines = 0
    total_words = 0
    total_bytes = 0
    report_length = 0
    header = f"Lines   Words   Bytes   Input Name"
    print(header)
    # print separator
    print("-" * len(header))

    for file in files_list:
        num_lines, num_words, num_bytes = 0, 0, 0
        line_list = file.readlines()
        # get number of lines
        num_lines = len(line_list)
        # get number of words
        # strip empty spaces around lines to count words
        for line in line_list:
            # get the number of bytes
            num_bytes += len(line)
            stripped_line = line.strip()
            # get rid of double or more spaces
            while "  " in stripped_line:
                stripped_line = stripped_line.replace("  ", " ")
            num_words += len(stripped_line.split())

        total_words += num_words
        total_lines += num_lines
        total_bytes += num_bytes
        # left align 8 characters in total
        print(f"{num_lines:<8}{num_words:<8}{num_bytes:<8} {file.name}")

    if len(files_list) > 1:
        print(f"{total_lines:<8}{total_words:<8}{total_bytes:<8} total")


# --------------------------------------------------
if __name__ == "__main__":
    main()
