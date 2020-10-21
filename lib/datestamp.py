# find latest date of file modification with regex and timestamp
# TODO if there are no entries under date, remove date heading

from datetime import datetime
from os import path
import regex


def add_datestamp(filename: str):
    """datestamp file"""
    with open(filename, "a") as file:
        file.write(f"{current_date}\n" + "=" * 10 + "\n")


def get_most_recent(filename: str):
    """search file for most recent additions, marked by iso-8601"""
    if path.isfile(filename) and path.getsize(filename) > 0:
        with open(filename, "r") as file:
            text = file.read()
    else:
        with open(filename, "w") as file:
            file.write(f"{current_date}\n")
            return

    # TODO group the second search for \d{2} to avoid repeating self
    # find the lastest edit with regex, then remove dashes and make int
    latest_edit = int(regex.findall("\d{4}-\d{2}-\d{2}", text)[-1].replace("-", ""))
    current_date_int = int(datetime.now().strftime("%Y%m%d"))
    if current_date_int > latest_edit:
        add_datestamp(filename)


def main():
    """search file and datestamp"""
    get_most_recent(filename)
    exit(0)


filename = "test.txt"
current_date = datetime.now().strftime("%Y-%m-%d")

if __name__ == "__main__":
    main()
