import PySimpleGUI as sg
import dice


def main():
    layout = [
        [
            # TODO disable typing in output box
            sg.Output(
                size=(90, 25),
                pad=(0, 5),
                echo_stdout_stderr=True,
                tooltip="Results of the dice rolled",
                key="-OUTPUT-",
            )
        ],
        [
            sg.Text("Sides:"),
            sg.Input(
                20,
                size=(8, 1),
                tooltip="Amount of sides on the dice, defaults to 20",
                key="-SIDES-",
            ),
            sg.Text("Roll count:"),
            sg.Input(
                1,
                size=(8, 1),
                tooltip="Times to roll the dice, defaults to 1",
                key="-COUNT-",
            ),
            sg.Radio(
                "Adv.",
                "adv_or_disadv",
                tooltip="Roll two d20 and choose the higher roll",
                key="-ADV-",
            ),
            sg.Radio(
                "Disadv.",
                "adv_or_disadv",
                tooltip="Roll two d20 and choose the lower roll",
                key="-DISADV-",
            ),
            sg.Check(
                "Sum rolls",
                auto_size_text=True,
                tooltip="Sum all rolls",
                key="-SUM-",
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
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Roll!":
            if values["-ADV-"] or values["-DISADV-"]:
                if values["-ADV-"]:
                    radio = "-ADV-"
                    window["-OUTPUT-"].update(dice.advantage("adv"))
                elif values["-DISADV-"]:
                    window["-OUTPUT-"].update(dice.advantage("disadv"))
                    radio = "-DISADV-"
            else:
                radio = None
                try:
                    sides = int(values["-SIDES-"])
                except ValueError:
                    sides = 20
                try:
                    count = int(values["-COUNT-"])
                except ValueError:
                    count = 1
                if values["-SUM-"]:
                    sum_rolls = True
                else:
                    sum_rolls = None
                window["-OUTPUT-"].update(dice.roll_dice(sides, count, sum_rolls, True))
            if radio:
                window.FindElement(radio).Update(False)
            window.Refresh()

    window.close()


if __name__ == "__main__":
    main()
