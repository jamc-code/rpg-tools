# generate a random starship name with a pilot/captain (dependant on size)
# ship classifications partially sourced from
# http://www.milsf.com/ship-classifications/

import argparse
from random import choice, randint
from faker import Faker
from faker_starship import Provider as StarshipProvider
from lib.ship_type import give_ship_type
from lib.to_output import to_output


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
        crew = f"""\r
                \r- {pilot}: {fake.name()}
                \r- {assistant}: {fake.name()}\n""".lstrip()
    else:
        crew = f"- {pilot}: {fake.name()}\n"

    return crew


def gen_starship(size: str, availability=None):
    """generate a starship name, class and registry"""
    # TODO redo existing ship classes to match typing when lore is more fleshed out
    # print(f"- Class: {fake.starship_class()}")
    name = fake.starship_name()
    crew = gen_names(size)
    ship = f"""
            \r{name} ({size} ship)
            \r{"-" * int(len(size) + len(name) + 8)}
            \r- Type: {give_ship_type(size, availability)}
            \r- Registry: {fake.starship_registry()}
            \r{crew}""".lstrip(
        "\n"
    )

    print(ship)

    return ship


def parse_arguments():
    """sort through provided arguments"""
    parser = argparse.ArgumentParser()
    civ_mil_group = parser.add_mutually_exclusive_group()
    civ_mil_group.add_argument(
        "--civ", help="choose ship class from civilian ships", action="store_true"
    )
    civ_mil_group.add_argument(
        "--mil", help="choose ship class from military ships", action="store_true"
    )
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

    # TODO if config file exists, use as default output, otherwise require arg
    parser.add_argument(
        "-o",
        "--output",
        help="""write to stdout and output file. defaults to location
                specified in config""",
        action="store_true",
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

    if args.output:
        output = True
    else:
        output = None

    return size, availability, output


def main():
    """generate starship based off of argument given"""
    size, availability, output = parse_arguments()
    ship = gen_starship(size, availability)
    if output:
        to_output("GenShip", f"{ship}\n")


fake = Faker("en_US")
fake.add_provider(StarshipProvider)

if __name__ == "__main__":
    main()
