# generate a random starship name with a pilot/captain (dependant on size)
# ship classifications partially sourced from
# http://www.milsf.com/ship-classifications/

import argparse
from faker import Faker
from faker_starship import Provider as StarshipProvider
from random import choice, randint

# TODO immersive ship size names in another file and import them
# TODO break these into lists within lists for military and civilian
small_ships = ["cutter", "patrol boat", "yacht", "smuggler"]
medium_ships = ["destroyer", "frigate", "passenger liner", "corvette"]
large_ships = ["carrier", "battleship", "hospital ship", "freighter"]


def gen_names(title: str):
    """decide if ship gets a pilot or a captain and first mate"""
    if title == "medium":
        pilot = "Pilot"
        assistant = "Co-Pilot"
    elif title == "large":
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


def gen_starship(size: str):
    """generate a starship name, class and registry"""
    name = fake.starship_name()
    print(f"\n{name} ({size} ship)")
    print("=" * int(len(size) + len(name) + 8))  # underline w the same length of chars
    print(f"- Class: {fake.starship_class()}")
    print(f"- Registry: {fake.starship_registry()}")


def main():
    """generate starship based off of argument given"""
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

    args = parser.parse_args()

    if args.small:
        gen_starship("small")
        gen_names("small")
    elif args.medium:
        gen_starship("medium")
        gen_names("medium")
    elif args.large:
        gen_starship("large")
        gen_names("large")
    elif args.random:
        size = choice(["small", "medium", "large"])
        gen_starship(size)
        gen_names(size)
    else:
        size = choice(["small", "medium", "large"])
        gen_starship(size)
        gen_names(size)
        # parser.print_help()


fake = Faker("en_US")
fake.add_provider(StarshipProvider)

if __name__ == "__main__":
    main()
