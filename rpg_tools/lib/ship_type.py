# -*- coding: utf-8 -*-
# give ship typing (fighter, bomber, speeder, etc.)
from __future__ import annotations
from random import choice


def give_ship_type(ship: str, civ_mil=None) -> str:
    """choose classification for a ship based off of size and availability"""
    if not civ_mil:
        civ_mil: str = choice(["civilian", "military"])

    # accesses dict by name of {ship} with key of {civ_mil}
    return choice(globals()[ship][civ_mil])


def main():
    """ask specifications of ship and classify ship"""
    ship: str = input("small, medium, large: ")
    civ_mil: str = input("civ or mil: ")
    classification: str = give_ship_type(ship, civ_mil)
    print(classification)


small: dict[str, list[str]] = {
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

medium: dict[str, list[str]] = {
    "civilian": ["Cargo Ship", "Passenger Liner", "Repair Ship"],
    "military": ["Corvette", "Destroyer", "Frigate", "Light Cruiser"],
}

large: dict[str, list[str]] = {
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
