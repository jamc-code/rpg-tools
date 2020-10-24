# -*- coding: utf-8 -*-
# give ship typing (fighter, bomber, speeder, etc.)
from random import choice


def give_ship_type(ship: str, civ_mil=None):
    """choose classification for a ship based off of size and availability"""
    if civ_mil == "civ":
        legality = "civilian"
    elif civ_mil == "mil":
        legality = "military"
    else:
        legality = choice(["civilian", "military"])

    # if ship not in ["small", "medium", "large"]:
    #    ship = choice(["small", "medium", "large"])

    if ship == "small":
        return choice(small[legality])
    elif ship == "medium":
        return choice(medium[legality])
    elif ship == "large":
        return choice(large[legality])
    else:
        return choice(
            (choice(small[legality]), choice(medium[legality]), choice(large[legality]))
        )


def main():
    """ask specifications of ship and classify ship"""
    ship = input("small, medium, large: ")
    civ_mil = input("civ or mil: ")
    classification = give_ship_type(ship, civ_mil)
    print(classification)


small = {
    "civilian": [
        "Courier",
        "Smuggler",
        "Speeder",
        "Survey Vessel",
        "Transport",
        "Yacht",
    ],
    "military": ["Bomber", "Cutter", "Fast Attack Craft", "Gun Boat", "Patrol Boat"],
}

medium = {
    "civilian": ["Cargo Ship", "Passenger Liner", "Repair Ship"],
    "military": ["Corvette", "Destroyer", "Frigate", "Light Cruiser"],
}

large = {
    "civilian": ["Colony Ship", "Cruise Ship", "Freighter"],
    "military": [
        "Battleship",
        "Battle Cruiser",
        "Carrier",
        "Heavy Cruiser",
        "Hospital Ship",
        "Light Carrier",
    ],
}

if __name__ == "__main__":
    main()
