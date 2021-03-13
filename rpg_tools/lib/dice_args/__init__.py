"""parse arguments for dice.py"""
import argparse


def get_arguments() -> argparse.Namespace:
    """get arguments for the dice"""
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
    main_args.add_argument("-t", "--total", help="sum all rolls", action="store_true")

    args: argparse.Namespace = parser.parse_args()
    return args
