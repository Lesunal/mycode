import PySimpleGUI as sg

layout = [
    [sg.Canvas(size=(200,150), background_color='blue', key='canvas')],
    [sg.Text("change the circle's color to:"), sg.Button('Red'), sg.Button('Black')]
        ]

window = sg.Window('Canvas Test', layout, finalize=True)

cir = window['canvas'].TKCanvas.create_oval(0,50,200,100)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in ('Red','Black'):
        window['canvas'].TKCanvas.itemconfig(cir, fill=event)