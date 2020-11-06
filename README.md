# RPG Tools
Folder of tools I'm writing in python to make my job as a DM easier.

Currently, the generators are aimed at a sci-fi setting, but I plan on adding fantasy generators once these are polished.


## Files (all located in ./src/)
- `config.ini` is the sole config file for the project. So far, only output locations are stored there.

- `dice.py` is a dice roller, with options to: repeatedly roll a dice, roll with (dis)advantage and sum up the total of your rolls.

- `gen_person.py` is an npc generator. It takes arguments for age and gender.
  - `nonbinary_provider.py` and `lib/nonbinary_names.py` make up a Faker provider I created for generating *real* gender-neutral names, as the stock provider isn't accurate and the only community provider I found for it was lame seemed transphobic.

- `gen_ship.py` generates a spaceship using [faker-starship](https://pypi.org/project/faker-starship/) for the names and registries. It takes arguments for ship size and legality
  - `lib/ship_type.py` is a script I wrote to overwrite the default ship classes that it provides in favor of broad ship types, such as "bomber" or "freighter." It creates these labels based off of the ship's size and legality (civilian or military).

- `lib/to_output.py` provides output arguments to both generators, allowing anything created to be saved in a file. I wrote this before I realized that the `logging` module exists, but it works so for now it stays.

## TODO
- [ ] Initiative tracker
- [ ] Implement a database for game info (chars, settings, etc.)
- [ ] Write tests
- [ ] Allow output location to be passed after '-o'
- [ ] Town/location generator
  - [ ] Spacestation generator
- [ ] GUI
- [ ] Create releases for people without python installed
- [X] Better project structure
- [X] Add info to pyproject
- [x] Output flag for generators
- [x] Create config file for storing file locations
- [x] Switch to more immersive ship size names
- [x] Choose uniform ship classes and registries
- [x] Better nonbinary names
- [x] Change formatting of output with any generators to export to markdown

## Bugs
If you notice any bugs, please submit an issue. I'm self-taught and this is my first "big" project so it might be a bit buggy at times :)
