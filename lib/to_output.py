# get location of file to output generation to
import configparser
from datetime import datetime
from os import path
import regex


def get_latest_edit(filename: str):
    """find latest edit in file and append new data"""
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


# TODO add section if it doesnt exist
def get_output_location(config_file: str, section: str, option: str):
    """output to file and stdout using path set in config"""
    config = configparser.ConfigParser()
    config.read(config_file, "utf-8")
    if config.has_option(section, option):
        output_file = f".{config.get(section, option)}"
    else:
        output_file = input("Path to output file: ")
        save = input("Save as default location? [Y/n] ").lower()
        if save == "y":
            config.set(section, option, output_file)
            config.write()
        else:
            pass

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
    output_file = get_output_location(config_location, "OUTPUT", generator)
    add_datestamp = get_latest_edit(output_file)
    write_to_file(output_file, new_text, add_datestamp)


current_date = datetime.now().strftime("%Y-%m-%d")

if __name__ == "__main__":
    to_output("GenPerson", "NEWTEXT\n\n")
    exit(0)
