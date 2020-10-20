import argparse
from random import randint
from sys import argv


# TODO add option to press 'q' to exit
def choose_sides():
    """choose the amount of sides on the die you want to roll"""
    choosing = True
    while choosing:
        try:
            sides = int(input("What sided die would you like to roll? "))
            return sides
        except (TypeError, ValueError):
            print("Postitive integers only please!")
            continue


# split this up even more
def roll_dice(sides, again=None, rolling=None, total=None):
    """roll a dice with {sides} specified by input"""
    rolling = True
    while rolling:
        if again == True:
            print(f"You rolled a {randint(1, sides)} on a d{sides}")
            reroll = input("Roll again? ").lower()
            if reroll == "y":
                pass
            else:
                break

        # roll set number of times
        elif isinstance(again, int) and not total:
            for i in range(1, again + 1):
                roll = randint(1, sides)
                print(f"You rolled a {roll} on a d{sides}")
            break

        # roll set number of times and sum up total
        elif isinstance(again, int) and total:
            total = 0
            for i in range(1, again + 1):
                roll = randint(1, sides)
                print(f"You rolled a {roll} on a d{sides}")
                total += roll
            print("-" * 24)
            print(f"Sum of rolls is {total}")
            break
        else:
            print(f"You rolled a {randint(1, sides)} on a d{sides}")
            break


def interactive(starting=None):
    """interactively roll dice"""
    started = False
    while True:
        if starting and started == False:
            sides = starting
        else:
            sides = choose_sides()
        started = True
        while True:
            roll_dice(sides, again=True)
            break
        cont = input("Continue with different die? ").lower()
        if cont == "y":
            continue
        else:
            break


# TODO option to sum x highest/lowest rolls
# TODO option to specify number of times to roll die and average -a d12 4
# TODO option to roll with advantage/disadvantage
def with_args():
    """roll dice based off of values passed as args"""
    parser = argparse.ArgumentParser(
        description="""Roll dice. If no arguments are given,
                    interactive mode is assumed."""
    )

    repeat_group = parser.add_mutually_exclusive_group()
    repeat_group.add_argument(
        "-c", "--count", type=int, help="number of times to roll die"
    )
    repeat_group.add_argument(
        "-r",
        "--repeat",
        action="store_true",
        help="repeat rolls for as long as desired, with {sides} as starting",
    )

    parser.add_argument("sides", type=int, help="number of sides on die to roll")
    parser.add_argument(
        "-t",
        "--total",
        action="store_true",
        help="""sum the dice rolled (the count flag
        is also required)""",
    )

    args = parser.parse_args()

    # TODO definitely switch these to var assignments, this is confusing
    if args.repeat:
        interactive(starting=args.sides)
    elif args.sides and not args.count and not args.total:
        roll_dice(args.sides, again=None)
    elif args.sides and args.count and not args.total:
        roll_dice(args.sides, args.count)
    elif args.sides and args.count and args.total:
        roll_dice(args.sides, args.count, rolling=True, total=True)
    else:
        parser.print_help()


def main():
    """
    check if program will be run in interactive mode or set with flags
    """
    # we're using argv here to negate the need for a whole parser
    # just in case the user wants to enter interactive mode
    if not len(argv) > 1:
        interactive()
    else:
        with_args()
    exit(0)


if __name__ == "__main__":
    main()
