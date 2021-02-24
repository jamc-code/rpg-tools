# get location of file to output generation to
from configparser import ConfigParser
from datetime import datetime
from os import makedirs, name
from pathlib import Path, PosixPath
import regex


def create_option(config_file: str, option: str, gui=None) -> str:
    """prompt for user to provide value for {option}"""
    output_file: str = input(f"Path to output file (base dir is {p.parents[2]}): ")
    if output_file[0:2] == "./":
        output_file = output_file.lstrip("./")
        output_file = f"{p.parents[2]}/{output_file}"
    save: str = input("Save as default location? [Y/n] ").lower()
    if save == "y":
        config = ConfigParser()
        config.read(config_file, "utf-8")
        if not config.has_section("OUTPUT"):
            config.add_section("OUTPUT")
        config.set("OUTPUT", option, output_file)
        # TODO find way to preserve comments
        #      readlines() file, insert new option after OUTPUT, write to tmp file with
        #      writelines and rename
        with open(config_file, "a") as file:
            config.write(file)
    else:
        pass

    return output_file


def get_latest_edit(filename: str):
    """find latest edit in file and append new data"""
    filepath: PosixPath = Path(filename)
    if filepath.is_file() and filepath.stat().st_size > 0:
        with open(filename, "r") as file:
            text: str = file.read()
    else:
        return True

    # TODO group the second search for \d{2} to avoid repeating self
    # find the latest edit with regex, then remove dashes and make int
    latest_edit: int = int(
        regex.findall("\d{4}-\d{2}-\d{2}", text)[-1].replace("-", "")
    )
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
        # get value from config, then append full file path to avoid path errors
        # if it starts with a relative path, expand it
        output_file = config.get("OUTPUT", option)
        if output_file[0:2] == "./":
            output_file = output_file.lstrip("./")
            output_file = f"{p.parents[2]}/{output_file}"
    else:
        output_file = create_option(config_file, option)

    return output_file


def home_dir_convert(filepath: str, use: str) -> str:
    """convert '/home/user' to '~' and vice versa (returns a string)"""
    # TODO test this
    while True:
        try:
            if str(filepath)[0] == "~":
                new_fp = PosixPath(filepath).expanduser()
                if PosixPath(new_fp).exists():
                    pass
                else:
                    raise IOError("Filepath does not exist!\nProvide valid path.")
            elif str(filepath)[0:6] == "/home/":
                if PosixPath(filepath).exists():
                    new_fp = filepath.replace(str(p.home()), "~")
                else:
                    raise IOError("Filepath does not exist!\nProvide valid path.")
            return str(new_fp)
        except (IOError, UnboundLocalError):
            print("Filepath must exist and be a string starting with '~' or '/home/'")
            filepath = input(f"Provide a filepath to {use}: ")


def write_to_file(
    option: str, output_file: str, new_text: str, add_datestamp=False, gui=None
):
    """write string to specified output file"""
    get_latest_edit(output_file)
    while True:
        try:
            with open(output_file, "a") as file:
                if add_datestamp:
                    file.write(f"{current_date}\n" + "=" * 10 + "\n")
                file.write(new_text)
            return

        except FileNotFoundError:
            if name == "posix":
                out_fp = output_file.split("/")[:-1]
                out_fp = "/".join(out_fp)
                proceed = input(f"Create '{out_fp}'? [Y/n] ").lower()
                if proceed == "y":
                    makedirs(str(out_fp))
                else:
                    output_file = create_option(config_location, option)
                    pass
            else:
                out_fp = output_file.split("\\")[:-1]
                out_fp = "\\".join(out_fp)
                proceed = input(f"Create '{out_fp}'? [Y/n] ").lower()
                if proceed == "y":
                    makedirs(str(out_fp))
                else:
                    output_file = create_option(config_location, option)
                    pass


def to_output(generator: str, new_text: str):
    """find file and write to it"""
    try:
        output_file = get_output_location(config_location, generator)
        add_datestamp = get_latest_edit(output_file)
        write_to_file(generator, output_file, new_text, add_datestamp)
    except KeyboardInterrupt:
        print("\nCtrl-C entered. Exiting.")
    exit(0)


current_date = datetime.now().strftime("%Y-%m-%d")
p = Path(__file__).absolute()
config_location = f"{p.parents[2]}/config.ini"

if __name__ == "__main__":
    # new_fp = home_dir_convert("/home/jam/programming", "config file")
    # print(new_fp)
    # new_fp = home_dir_convert("~/programming", "config file")
    # print(new_fp)
    # new_fp = home_dir_convert(str(2), "config file")
    # print(new_fp)
    # new_fp = home_dir_convert("/home/jam/thing", "config file")
    # print(new_fp)
    # new_fp = home_dir_convert("~/thing", "config file")
    # print(new_fp)
    to_output("GenPerson", "NEW TEXT\n\n")
    exit(0)
