import argparse
from random import randint
from sys import argv


def advantage(adv: str):
    """roll with advantage/disadvantage (two s20 and choose higher/lower)"""
    rolls = [0]
    while rolls[0] < 2:
        rolls.append(randint(1, 20))
        rolls[0] += 1
    for roll in rolls[1:]:
        print(f"You rolled a {roll} on a d20")
    if adv == "adv":
        print("With advantage, you rolled a", sorted(rolls)[2])
    elif adv == "disadv":
        print("With disadvantage, you rolled a", sorted(rolls)[1])
    exit(0)


def choose_sides():
    """choose the amount of sides on the die you want to roll"""
    choosing = True
    while choosing:
        try:
            sides = int(input("What sided die would you like to roll? "))
            return sides
        except (TypeError, ValueError):
            print("Positive integers only please!")
            exit(1)


def interactive(starting=None):
    """interactively roll dice"""
    started = False
    while True:
        if starting and started is False:
            sides = starting
        else:
            sides = choose_sides()
        # this prevents choose_dice from being repeated
        started = True
        while True:
            roll_dice(sides, again=True)
            break
        cont = input("Continue with different die? ").lower()
        if cont == "y":
            continue
        else:
            exit(0)


# TODO option to sum x highest/lowest rolls
# TODO round up/down (read manual to implement this correctly)
def parse_args():
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

    sides_group = parser.add_mutually_exclusive_group()
    sides_group.add_argument(
        "-a",
        "--advantage",
        action="store_true",
        help="roll two d20 and choose the higher roll",
    )
    sides_group.add_argument(
        "-d",
        "--disadvantage",
        action="store_true",
        help="roll two d20 and choose the lower roll",
    )
    sides_group.add_argument(
        "-s", "--sides", type=int, help="number of sides on die to roll"
    )

    parser.add_argument(
        "-t",
        "--total",
        action="store_true",
        help="""sum the dice rolled (the count flag
        is also required)""",
    )

    args = parser.parse_args()

    if args.advantage:
        advantage("adv")
    elif args.disadvantage:
        advantage("disadv")
    elif args.sides:
        sides = args.sides
    else:
        sides = choose_sides()

    if args.repeat:
        interactive(sides)
    if args.count:
        count = args.count
    else:
        count = None
    if args.total:
        total = True
    else:
        total = None

    roll_dice(sides, count, total)


def roll_dice(sides, again=None, total=None):
    """roll a dice with {sides} specified by input"""
    rolling = True
    while rolling:
        if again is True:
            print(f"You rolled a {randint(1, sides)} on a d{sides}")
            reroll = input("Roll again? ").lower()
            if reroll == "y":
                pass
            else:
                break

        # roll set number of times
        elif isinstance(again, int):
            roll_sum = 0
            for i in range(1, again + 1):
                roll = randint(1, sides)
                print(f"You rolled a {roll} on a d{sides}")
                # if total is passed, sum rolls
                if total:
                    roll_sum += roll
            if total and total > 0:
                if sides >= 10:
                    print(f"{'-' * 24}\n   Sum of rolls is {roll_sum}")
                else:
                    print(f"{'-' * 22}\n   Sum of rolls is {roll_sum}")
            break

        else:
            print(f"You rolled a {randint(1, sides)} on a d{sides}")
            exit(0)


def main():
    """
    check if program will be run in interactive mode or set with flags
    """
    # we're using argv here to negate the need for a whole parser
    # just in case the user wants to enter interactive mode
    try:
        if not len(argv) > 1:
            interactive()
        else:
            parse_args()
    except KeyboardInterrupt:
        print("\nCtrl-C entered. Exiting.")
    exit(0)


if __name__ == "__main__":
    main()
