import PySimpleGUI as sg


def main():

    # Describes all window elements
    layout =   [
        [Updateable_Map, Inventory_Pane],
        [Picture_Pane],
        [sg.LBox([], size=(80,6), key='-Narrate-')],
        [Action_Bar],
    ]

    # Create the window, with the name "The Coolest Game", using the described layout
    window = ["The Coolest Game",layout,]

    Narrate_list = []

    # Create function to append new items to Narrate_list
    def Narrate(Narrate_list, Action, Location, Item, Object):
        # Descriptor_dict stores a dictionary for all Actions and Location descriptions which will be used in game. 
        Descriptor_dict = {'Action': {'Move': H , 'Reexamine': H, 'Use_Item': H, 'Interact_Object': H, 'Use_Item_Object': H}, 
                           'Location_Descript': {'Room1': H, 'Room2': H, 'Room3': H,'Room4': H,'Room5': H,'Room6': H,'Room7': H,'Room8': H,'Room8': H}
                           }
        Description_string = Descriptor_dict['Action']
        Narrate_list.append(Description_string)
        return Narrate_list
    

    #The window loop
    while True:
        event, values = window.read(timeout=200)
        # If the x is pressed the window closes
        if event == sg.WINDOW_CLOSED:
            break

        #placeholder for gamestate change action

        # Move Action
        if event.startswith('Action_Move'):
            # Alter player location
            placeholder = True

        # Reexamine Action
        elif event.startswith('Action_Reexamine'):
            # Refresh Narrate_list
            placeholder = True
        
        # Use item and Select Object functions
        elif event.startswith('Select'):
            # Open relevant popup window which provides selection options
            placeholder = True


        # For every 'Action' event, add event text to the Narrate pane
        if event.startswith('Action')==True:
            # Updates the Narrate window with the new Narrate_list
            Narrate()
            window['-Narrate-'].Update(values[Narrate_list])


main()
