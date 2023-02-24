import PySimpleGUI as sg

layout = [
        
        [sg.Text('This example code:'),sg.Push(),sg.Text('Produces this output:')],
        [sg.Output(size=(50,10), key='-Example-'),sg.Output(size=(50,10), key='-Example_Out-')],
        [sg.Text('Ensure your code follows these parameters:'),sg.Push(), sg.Text('Craft a script that outputs this code:') ],
        [sg.Output(size=(50,10), key='-Parameters-'),sg.Output(size=(50,10), key='-Problem-')],
        [sg.Button('Input Code'), sg.Button('Exit')]
]

window = sg.Window('Learn to Code').Layout(layout).Finalize()

def code_input():
    event, values = sg.Window('Code Input',
                [[sg.T('Enter your Code Solution')],
                [sg.Multiline(size=(100,50),enter_submits=False, autoscroll=True, do_not_clear=True, key="-Solution-")],
                [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)

    solution = values['-Solution-']
    return solution

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Input Code':
        solution = code_input()

        #window['-OUTPUT-'].update('')

print(solution)
window.close()


