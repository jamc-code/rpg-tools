"""roll a dice"""
from __future__ import annotations
import argparse
from random import randint


def advantage(type_: str, times: int):
    """roll a dice with advantage or disadvantage
    type_: 'adv' for advantage, 'dis' for disadvantage
    """
    rolls: list[int] = []
    roll_msg: str = "With {}, you rolled a {} on a d20"
    while len(rolls) < 2:
        roll = get_roll(20)
        rolls.append(roll)
        print(f"You rolled a {roll:02} on a d20")
    print(roll_msg.format(type_, f"{max(rolls):02}"))
    # if this should be done multiple times, repeat it as long as needed
    if not times or times == 1:
        return
    # get the length of the roll message for printing spacer lines
    roll_msg_len: int = len(roll_msg) + len(type_) - 2
    print("-" * roll_msg_len)
    times -= 1
    advantage(type_, times)


def get_roll(sides: int) -> int:
    """return the result of a dice roll with the amount of sides provided as an arg"""
    return randint(1, sides)


def roll_dice(sides: int, times: int | None):
    """roll a dice with {sides} a certain number of {times}"""
    padding: int = len(str(sides))  # get the amount of zeros to pad the roll with
    roll = get_roll(sides)
    print(f"You rolled a {roll:0{padding}} on a d{sides}")
    if not times:
        return
    for _ in range(times - 1):
        roll = get_roll(sides)
        print(f"You rolled a {roll:0{padding}} on a d{sides}")


def main() -> int:
    """do it"""
    args = get_arguments()
    if args.advantage:
        advantage("advantage", args.count)
    elif args.disadvantage:
        advantage("disadvantage", args.count)
    elif args.sides:
        roll_dice(args.sides, args.count)
    return 0


def get_arguments() -> argparse.Namespace:
    """get arguments for the dice"""
    # TODO option for total rolls
    # TODO option for repeating rolls
    # TODO interactive mode?
    parser = argparse.ArgumentParser()
    main_args = parser.add_argument_group()
    side_args = parser.add_mutually_exclusive_group(required=True)

    side_args.add_argument(
        "-a", "--advantage", help="roll a d20 with advantage", action="store_true"
    )
    side_args.add_argument(
        "-d", "--disadvantage", help="roll a d20 with disadvantage", action="store_true"
    )
    side_args.add_argument(
        "-s", "--sides", help="number of sides on the dice", type=int
    )
    main_args.add_argument(
        "-c", "--count", help="number of times to roll a dice", type=int
    )

    args: argparse.Namespace = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
