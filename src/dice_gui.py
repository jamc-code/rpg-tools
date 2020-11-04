import PySimpleGUI as sg


def main():
    layout = [
        [
            # TODO output only stores one line, have it write like stdout
            sg.Output(
                size=(90, 25), tooltip="Results of the dice rolled", key="-OUTPUT-"
            )
        ],
        [
            sg.Input(
                20, size=(8, 1), tooltip="Amount of sides on the dice", key="-IN-"
            ),
            sg.Input(
                "Count",
                size=(8, 1),
                tooltip="Times to roll the dice. Disabled if Repeat button enabled",
            ),
            # TODO is repeat unnecessary if you click button to roll?
            sg.Radio(
                "Repeat", "count_or_repeat", tooltip="Repeat the roll until specified"
            ),
            sg.Radio(
                "Adv.",
                "adv_or_disadv",
                tooltip="Roll two d20 and choose the higher roll",
            ),
            sg.Radio(
                "Disadv.",
                "adv_or_disadv",
                tooltip="Roll two d20 and choose the lower roll",
            ),
            sg.Check(
                "Sum rolls",
                auto_size_text=True,
                tooltip="Sum all rolls. Only valid with 'Count'",
            ),
            sg.Submit(
                "Roll!",
                auto_size_button=True,
                tooltip="Roll the dice with the parameters given",
            ),
        ],
    ]

    window = sg.Window(
        "Dice",
        layout,
        auto_size_text=True,
        auto_size_buttons=True,
        size=(600, 400),
        element_justification="center",
    )
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Roll!":
            window["-OUTPUT-"].update(values["-IN-"])

    window.close()


if __name__ == "__main__":
    main()
