import PySimpleGUI as sg
import gen_person


def main():
    layout = [
        [
            sg.Output(
                size=(90, 25),
                pad=(0, 5),
                echo_stdout_stderr=False,
                tooltip="Person generated",
                key="-OUTPUT-",
            ),
        ],
    ]


if __name__ == "__main__":
    main()
