import PySimpleGUI as sg


def main():

    # Describes all window elements
    layout =   [
        ['Updateable_Map', 'Inventory_Pane'],
        ['Picture_Pane'],
        [sg.LBox([], size=(80,6), key='-Narrate-')],
        ['Action_Bar'],
    ]

    # Create the window, with the name "The Coolest Game", using the described layout
    window = ["The Coolest Game",layout,]
    
    H = None
    Narrate_list = []
    inventory = []
    Location = 'Room1'

    Room_dict = {
                'Room1':  {
                    'Location_Desc':["A stark and empty stone room with a single rotted wooden door to the North."],
                    'Move_Desc':
                            {
                        'Up':"You pull on the rotted door's handle and it moves inward just engough to allow you passage. You step through.",
                        'Down':H,
                        'Left':H,
                        'Right':H
                            },
                    'Objects':{
                        'Object1':{
                            'Object_Key': 'picture',
                            'Object_Desc':["A tattered portrait of a wolf", "hangs on the wall."],
                            'Interact_type':'standard',
                            'Interact_desc':'You carefully lift the portrait off the wall and stowe it for later.',
                            'Interact_effect': "inventory.append(Room_dict['Room1']['Objects']['Object1']) ; del(Room_dict['Room1']['Objects']['Object1'])"
                                }
                            }
                            },
                'Room2':    {
                    'Location_Desc':['Another stone room greets you, illuminated by torchlight. To the South lies the rotted door and room you came from. To the East an archway allows passage to another room, too dark to see into. To the West another door waits.'],
                    'Move_Desc':
                            {
                        'Up':H,
                        'Down':"You slip past the rotted wooden door South once more.",
                        'Left':"You walk through the archway into the darkness.",
                        'Right':"You open the door and walkthrough, careful to shut it behind you."
                            },
                    'Objects':{
                        'Object1':  {
                            'Object_Key': 'chest' ,
                            'Object_Desc': "In the room's center sits a large metal chest, closed and presumably locked.",
                            'Interact_type': 'key' ,
                            'Interact_desc': "You slide the key into the chest's lock and twist, with a loud clack, the chest unlocks and you hoist its lid open to see what's inside" 
                                    }
                            }
                            },
                'Room3':    {
                    'Location_Desc':[H],
                    'Move_Desc':
                            {
                        'Up':H,
                        'Down':H,
                        'Left':H,
                        'Right':H
                            },
                    'Objects':{
                        'Object1':{
                            'Object_Key': H,
                            'Object_Desc':H ,
                            'Interact_type':H ,
                            'Interact_desc':H 
                                }
                            }
                            },
                'Room4':    {
                    'Location_Desc':[H],
                    'Move_Desc':
                            {
                        'Up':H,
                        'Down':H,
                        'Left':H,
                        'Right':H
                            },
                    'Objects':{
                        'Object1':{
                            'Object_Key': H,
                            'Object_Desc':H ,
                            'Interact_type':H ,
                            'Interact_desc':H 
                                }
                            }
                            },
                'Room5':    {
                    'Location_Desc':[H],
                    'Move_Desc':
                            {
                        'Up':H,
                        'Down':H,
                        'Left':H,
                        'Right':H
                            },
                    'Objects':{
                        'Object1':{
                            'Object_Key': H,
                            'Object_Desc':H ,
                            'Interact_type':H ,
                            'Interact_desc': H
                                }
                            }
                            },
                'Room6':    {
                    'Location_Desc':[H],
                    'Move_Desc':
                            {
                        'Up':H,
                        'Down':H,
                        'Left':H,
                        'Right':H
                            },
                    'Objects':{
                        'Object1':{
                            'Object_Key': H,
                            'Object_Desc':H ,
                            'Interact_type':H ,
                            'Interact_desc':H 
                                }
                            }
                            }
                    }

    def Narrate( Action, Location, Object, Item, Direction):
            # Room_dict stores a dictionary for all Actions and Location descriptions which will be used in game. 
            
            # Reexamine action will state or restate current room description based on Room specific description and object specific descriptions
            if Action == 'Reexamine':
                Description_string = Room_dict[Location]['Location_Desc'][0]
                for objects in Room_dict[Location]['Objects']:
                    Description_string.append(Room_dict[Location]['Objects'][objects]['Object_Desc']) 
            
            if Action.startswith() == 'Move':
                Description_string = Room_dict[Location]['Move_Desc'][Direction]


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
