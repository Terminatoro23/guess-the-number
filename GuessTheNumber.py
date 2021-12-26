import random
import PySimpleGUI as sg


def game():
    wanted = random.randint(0, 1000)
    layout = [[sg.Text("Enter the number (0-1000):")], [sg.InputText()], [sg.Button("OK")]]
    window = sg.Window("Guess the number", layout, margins=(70, 40))
    changes = 1
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'OK':
            if changes <= 10:
                trial = values[0]
                if trial.isdigit():
                    if int(trial) == wanted:
                        sg.Popup("Nice! You did it!")
                        break
                    elif changes == 10:
                        sg.Popup("Too many tries. The number you were looking for is " + str(wanted))
                        window.close()
                        break
                    elif int(trial) < wanted:
                        sg.PopupQuick("Too low\n Tries:" + str(changes), auto_close=False)
                        changes = changes + 1
                    elif int(trial) > wanted:
                        sg.PopupQuick("Too big\n Tries:" + str(changes), auto_close=False)
                        changes = changes + 1
                else:
                    sg.Popup("You entered something other than a number! Try again")
            else:
                sg.Popup("Too many tries. The number you were looking for is " + str(wanted))
                window.close()
                break


game()
