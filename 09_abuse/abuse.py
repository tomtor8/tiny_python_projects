#!/usr/bin/env python3
"""
Author : tom <tom@localhost>
Date   : 2024-02-14
Purpose: Rock the Casbah
"""

import argparse, random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Heap abuse",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-a",
        "--adjectives",
        help="Number of adjectives",
        metavar="adjectives",
        type=int,
        default=2,
    )

    parser.add_argument(
        "-n",
        "--number",
        help="Number of insults",
        metavar="insults",
        type=int,
        default=3,
    )

    parser.add_argument(
        "-s",
        "--seed",
        help="Random seed",
        metavar="seed",
        type=int,
        default=None,
    )

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    adjectives_num = args.adjectives
    insults_num = args.number
    # if seed is None, nothing happens
    random.seed(args.seed)

    # create two lists using split method
    insults = """Judas Satan ape ass barbermonger beggar block boy braggart butt carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool gull harpy jack jolthead knave liar lunatic maw milksop minion ratcatcher recreant rogue scold slave swine traitor varlet villain worm""".strip().split(
        " "
    )

    adjectives = """bankrupt base caterwauling corrupt cullionly detestable dishonest false filthsome filthy foolish foul gross heedless indistinguishable infected insatiate irksome lascivious lecherous loathsome lubbery old peevish rascaly rotten ruinous scurilous scurvy slanderous sodden-witted thin-faced toad-spotted unmannered vile wall-eyed""".strip().split(
        " "
    )

    # create a selected number of insults
    for _ in range(insults_num):
        # pick just one insult from the list
        chosen_insult = random.choice(insults)
        # choose a selected number of items from the list
        chosen_adjectives = random.sample(adjectives, k=adjectives_num)
        # the join method turns a list into a string joined by commas
        print(f"You {', '.join(chosen_adjectives)} {chosen_insult}!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
