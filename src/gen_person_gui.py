from pathlib import Path
from random import choice
import PySimpleGUI as sg
import gen_person
from lib.to_output import get_output_location
# TODO turn this into a function with args for any generator


def main():
    """launch a gui for the person generator"""
    layout = [
        [
            sg.Output(
                size=(90, 25),
                pad=(0, 5),
                echo_stdout_stderr=True,
                tooltip="Characters generated",
                key="-OUTPUT-",
            )
        ],
        [
            # TODO age input box cuts off last letter of "Random"
            sg.Text("Age:"),
            sg.Combo(
                (["Young", "Middle", "Old", "Random"]),
                "Random",
                key="-AGE-",
            ),
            sg.Text("Gender:"),
            sg.Combo(
                (["Nonbinary", "Female", "Male", "Random"]),
                "Random",
                key="-GENDER-",
            ),
            # TODO move this to be a row under the args for more room
            sg.Check(
                "Output to file",
                enable_events=True,
                key="-WRITE-",
                tooltip="write generated character to file",
            ),
            # TODO find a way to align this text to the right so it shows file location
            sg.Input(
                f"{get_output_location(config_location, 'GenPerson')}",
                disabled=True,
                key="-OUTPUT_LOC-",
                tooltip="location of the output file, if enabled",
            ),
            sg.Submit("Generate!"),
        ],
    ]

    sg.theme("BlueMono")
    window = sg.Window(
        "Gen Person",
        layout,
        auto_size_text=True,
        auto_size_buttons=True,
        size=(800, 400),
        element_justification="center",
    )

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        print(event, values)
        # enable the input box ONLY if the checkbox is checked
        if values["-WRITE-"] is True:
            window.FindElement("-OUTPUT_LOC-").Update(disabled=False)
        elif values["-WRITE-"] is False:
            window.FindElement("-OUTPUT_LOC-").Update(disabled=True)
        if event == "Generate!":
            age_list = ["young", "middle", "old"]
            age_group = values["-AGE-"].lower()
            if age_group not in age_list:
                age_group = choice(age_list)

            gender_list = ["female", "nonbinary", "male"]
            gender = values["-GENDER-"].lower()
            if gender not in gender_list:
                gender = choice(gender_list)

            name, company, job, age = gen_person.gen_person(gender, age_group)
            person = gen_person.format_person(name, company, job, age, gender)
            print(person)


p = Path(__file__).absolute()
config_location = f"{p.parents[1]}/config.ini"

if __name__ == "__main__":
    main()