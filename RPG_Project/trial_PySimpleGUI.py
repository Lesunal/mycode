import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("What's your name?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')],
          [sg.LBox([], size=(80,6), key='-Narrate-')]]

# Create the window
window = sg.Window('Window Title', layout)

Narrate_list = []

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")
    Narrate_list.append(values['-INPUT-'])
    print(values)
    print(Narrate_list)
    window['-Narrate-'].Update(Narrate_list)

# Finish up by removing from the screen
window.close()