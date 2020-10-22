# get location of file to output generation to
from configparser import ConfigParser
from datetime import datetime
from os import path
import regex


def create_option(config_file, option: str):
    """prompt for user to provide value for {option}"""
    # TODO create fp if it doesnt exist
    output_file = input("Path to output file (use relative path): ")
    save = input("Save as default location? [Y/n] ").lower()
    if save == "y":
        config = ConfigParser()
        config.read(config_file, "utf-8")
        if not config.has_section("OUTPUT"):
            config.add_section("OUTPUT")
        config.set("OUTPUT", option, output_file)
        # TODO find way to preserve comments
        #      readlines file, insert new option after OUTPUT, write to tmp file w
        #      writelines and rename
        with open(config_file, "a") as file:
            config.write(file)
    else:
        pass

    return output_file


def get_latest_edit(filename: str):
    """find latest edit in file and append new data"""
    # TODO if path doesn't exist, create full path
    if path.isfile(filename) and path.getsize(filename) > 0:
        with open(filename, "r") as file:
            text = file.read()
    else:
        return True

    # TODO group the second search for \d{2} to avoid repeating self
    # find the lastest edit with regex, then remove dashes and make int
    latest_edit = int(regex.findall("\d{4}-\d{2}-\d{2}", text)[-1].replace("-", ""))
    current_date_int = int(datetime.now().strftime("%Y%m%d"))
    if current_date_int > latest_edit:
        return True
    return


def get_output_location(config_file: str, option: str):
    """output to file and stdout using path set in config"""
    config = ConfigParser()
    config.read(config_file, "utf-8")

    if not config.has_section("OUTPUT"):  # create output section if it doesn't exist
        config.add_section("OUTPUT")
    if config.has_option("OUTPUT", option):
        # TODO check if value is relative ('./file') before stripping to avoid
        #      messing up full file paths ('/path/to/file')
        # get value from config, then append full file path to avoid path errors
        output_file = config.get("OUTPUT", option).lstrip("./")
        output_file = (
            f"{path.dirname(path.dirname(path.abspath(__file__)))}/{output_file}"
        )
    else:
        output_file = create_option(config_file, option)

    return output_file


def write_to_file(output_file: str, new_text: str, add_datestamp=False):
    """write string to specified output file"""
    get_latest_edit(output_file)
    with open(output_file, "a") as file:
        if add_datestamp == True:
            file.write(f"{current_date}\n" + "=" * 10 + "\n")
        file.write(new_text)
    return


def to_output(generator: str, new_text: str):
    """find file and write to it"""
    current_date = datetime.now().strftime("%Y-%m-%d")
    # TODO is it donkey-brained to use this to find file when '../config.ini' is same?
    config_location = f"{path.dirname(path.dirname(path.abspath(__file__)))}/config.ini"
    output_file = get_output_location(config_location, generator)
    add_datestamp = get_latest_edit(output_file)
    write_to_file(output_file, new_text, add_datestamp)


current_date = datetime.now().strftime("%Y-%m-%d")

if __name__ == "__main__":
    to_output("GenPerson", "NEWTEXT\n\n")
    exit(0)
