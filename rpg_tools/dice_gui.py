import PySimpleGUI as sg
import dice


def main():
    layout = [
        [
            # TODO output only stores one line, have it write like stdout
            sg.Output(
                size=(90, 25),
                echo_stdout_stderr=True,
                tooltip="Results of the dice rolled",
                key="-OUTPUT-",
            )
        ],
        [
            # TODO find way to make to auto-clear this field when clicked on
            sg.Input(
                20, size=(8, 1), tooltip="Amount of sides on the dice", key="-SIDES-"
            ),
            # TODO disable if 'repeat' chosen and vice versa
            sg.Input(
                1,
                size=(8, 1),
                tooltip="Times to roll the dice. Disabled if Repeat button enabled",
                key="-COUNT-",
            ),
            # TODO these need to be able to be unchecked
            #      but remain in radio group to be one or the other
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
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Roll!":
            sides = int(values["-SIDES-"])
            count = int(values["-COUNT-"])
            window["-OUTPUT-"].update(dice.roll_dice(sides, count))
            window.Refresh()

    window.close()


if __name__ == "__main__":
    main()
