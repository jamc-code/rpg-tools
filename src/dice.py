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
        adv_message = f"With advantage, you rolled a {sorted(rolls)[2]}\n"
    elif adv == "disadv":
        adv_message = f"With disadvantage, you rolled a {sorted(rolls)[1]}\n"
    print(adv_message)


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


def interactive():
    """interactively roll dice"""
    while True:
        sides = choose_sides()
        while True:
            roll_dice(sides, repeat=True)
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
        adv_disadv = "adv"
    elif args.disadvantage:
        adv_disadv = "disadv"
    elif not args.advantage and not args.disadvantage:
        adv_disadv = None
    if args.sides:
        sides = args.sides
    elif not args.sides and not adv_disadv:
        sides = choose_sides()

    if args.repeat:
        roll_dice(sides, repeat=True)
    if args.count:
        count = args.count
    else:
        count = None
    if args.total:
        total = True
    else:
        total = None

    if adv_disadv:
        advantage(adv_disadv)
    else:
        roll_dice(sides, count, total)


def roll_dice(sides, repeat=None, total=None, gui=None):
    """roll a dice with {sides} specified by input"""
    rolling = True
    while rolling:
        if repeat is True:
            print(f"You rolled a {randint(1, sides)} on a d{sides}")
            reroll = input("Roll repeat? ").lower()
            if reroll == "y":
                pass
            else:
                break
        # roll set number of times
        elif isinstance(repeat, int) and repeat > 1:
            roll_sum = 0
            for i in range(1, repeat + 1):
                roll = randint(1, sides)
                print(f"You rolled a {roll} on a d{sides}")
                # if total is passed, sum rolls
                if total:
                    roll_sum += roll
            if total:
                if gui:
                    sum_message = f"{'-' * 36}\n   Sum of rolls is {roll_sum}\n"
                else:
                    if sides >= 10:
                        sum_message = f"{'-' * 24}\n   Sum of rolls is {roll_sum}\n"
                    else:
                        sum_message = f"{'-' * 22}\n   Sum of rolls is {roll_sum}\n"
                print(sum_message)
            else:
                print()
            break
        else:
            print(f"You rolled a {randint(1, sides)} on a d{sides}")
            break


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
