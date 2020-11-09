from random import choice
import PySimpleGUI as sg
import gen_person


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
            # TODO output file location input to popup window if not set
            sg.Check(
                "Output to file",
                tooltip="write generated character to file",
                key="-WRITE-",
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
        size=(600, 400),
        element_justification="center",
    )

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
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


if __name__ == "__main__":
    main()
