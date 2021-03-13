"""roll a dice"""
from __future__ import annotations
from random import randint

# TODO fix this stupid import shit (more modules?)
# pylint: disable=E0401
from lib.dice_args import get_arguments  # type: ignore


def advantage(type_: str, times=None):
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
    if not times:
        return
    # get the length of the roll message for printing spacer lines
    roll_msg_len: int = len(roll_msg) + len(type_) - 2
    for _ in range(times - 1):
        print("-" * roll_msg_len)
        advantage(type_)


def get_roll(sides: int) -> int:
    """return the result of a dice roll with the amount of sides provided as an arg"""
    return randint(1, sides)


def roll_dice(sides: int, times=None):
    """roll a dice with {sides} a certain number of {times}"""
    padding: int = len(str(sides))  # get the amount of zeros to pad the roll with
    roll = get_roll(sides)
    print(f"You rolled a {roll:0{padding}} on a d{sides}")
    if not times:
        return
    for _ in range(times - 1):
        roll_dice(sides)


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


if __name__ == "__main__":
    main()
