# generate a random starship name with a pilot/captain (dependant on size)
# ship classifications partially sourced from
# http://www.milsf.com/ship-classifications/

import argparse
from faker import Faker
from faker_starship import Provider as StarshipProvider
from lib.ship_type import give_ship_type
from random import choice, randint


def gen_names(size: str):
    """decide if ship gets a pilot or a captain and first mate"""
    if size == "medium":
        pilot = "Pilot"
        assistant = "Co-Pilot"
    elif size == "large":
        pilot = "Captain"
        assistant = "First Mate"
    else:
        pilot = "Pilot"
        if randint(1, 4) > 3:  # 25% chance for a cop-pilot in a small ship
            assistant = "Co-Pilot"
        else:
            assistant = None

    if assistant:
        print(f"- {pilot}: {fake.name()}")
        print(f"- {assistant}: {fake.name()}\n")
    else:
        print(f"- {pilot}: {fake.name()}\n")


def gen_starship(size: str, availability=None):
    """generate a starship name, class and registry"""
    name = fake.starship_name()
    print(f"\n{name} ({size} ship)")
    print("-" * int(len(size) + len(name) + 8))  # underline w the same length of chars
    # TODO redo existing ship classes when lore is more fleshed out
    # print(f"- Class: {fake.starship_class()}")
    print(f"- Type: {give_ship_type(size)}")
    print(f"- Registry: {fake.starship_registry()}")
    gen_names(size)


def parse_arguments():
    """sort through provided arguments"""
    parser = argparse.ArgumentParser()
    # group for choosing ship size (must provide one)
    size_group = parser.add_mutually_exclusive_group()
    size_group.add_argument(
        "-s", "--small", help="generate a small ship", action="store_true"
    )
    size_group.add_argument(
        "-m", "--medium", help="generate a medium ship", action="store_true"
    )
    size_group.add_argument(
        "-l", "--large", help="generate a large ship", action="store_true"
    )
    size_group.add_argument(
        "-r",
        "--random",
        help="randomly choose a ship size (default)",
        action="store_true",
    )

    civ_mil_group = parser.add_mutually_exclusive_group()
    civ_mil_group.add_argument(
        "--civ", help="choose ship class from civilian ships", action="store_true"
    )
    civ_mil_group.add_argument(
        "--mil", help="choose ship class from military ships", action="store_true"
    )

    args = parser.parse_args()

    if args.small:
        size = "small"
    elif args.medium:
        size = "medium"
    elif args.large:
        size = "large"
    else:
        size = choice(["small", "medium", "large"])

    if args.civ:
        availability = "civilian"
    elif args.mil:
        availability = "military"
    else:
        availability = None

    return size, availability


def main():
    """generate starship based off of argument given"""
    size, availability = parse_arguments()
    gen_starship(size, availability)
    exit(0)


fake = Faker("en_US")
fake.add_provider(StarshipProvider)

if __name__ == "__main__":
    main()
