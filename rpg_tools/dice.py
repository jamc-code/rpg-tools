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
    for _ in range(2):
        roll = roll_dice(20)
        rolls.append(roll)
    roll_msg: str = f"With {type_}, you rolled {max(rolls):02} on a d20"
    print(roll_msg)
    if not times:
        return
    # get the length of the roll message for printing divider lines
    roll_msg_len = len(roll_msg)
    for _ in range(times - 1):
        print("-" * roll_msg_len)
        advantage(type_)


def get_roll(sides: int) -> int:
    """return the result of a dice roll with the amount of sides provided as an arg"""
    return randint(1, sides)


def roll_dice(sides: int, times=None, total=None) -> int:
    """roll a dice with {sides} a certain number of {times}"""
    padding: int = len(str(sides))  # get the amount of zeros to pad the roll with
    roll = get_roll(sides)
    print(f"You rolled {roll:0{padding}} on a d{sides}")
    if not times:
        return roll

    rolls: list[int] = [roll]
    for _ in range(times - 1):
        roll = roll_dice(sides)
        if total:
            rolls.append(roll)
    if len(rolls) > 1:
        print(f"Sum of rolls: {sum(rolls)}")
    return 0


def main() -> int:
    """do it"""
    args = get_arguments()
    if args.advantage:
        advantage("advantage", args.count)
    elif args.disadvantage:
        advantage("disadvantage", args.count)
    elif args.sides:
        roll_dice(args.sides, args.count, args.total)
    return 0


if __name__ == "__main__":
    main()
