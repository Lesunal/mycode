import PySimpleGUI as sg

test_value = 5

def test(test_value):
    test_value = 10
    return test_value

test_value = test(test_value)
print(test_value)

global Room_dict
H = None
Room_dict = {
        'Room1':  {
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
        'Room2':    {
            'Location_Desc':[H],
            'Move_Desc':
                    {
                'Up':H,
                'Down':H,
                'Left':H,
                'Right':H
                    },
            'Objects':{
                'Object1':  {
                    'Object_Key': H,
                    'Object_Desc':H ,
                    'Interact_type':H ,
                    'Interact_desc':H 
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

def Narrate(Type, Action, Location, Item, Object):
    # Room_dict stores a dictionary for all Actions and Location descriptions which will be used in game. 
    if Type == 'Reexamine':
        Description_string = Room_dict[Location]['Location_Desc'][1]
        for objects in Room_dict[Location]['Objects']
            Description_string = Description_string +  
    
    Narrate_list.append(Description_string)
    return Narrate_list

Narrate_list = []
inventory = []
Location = 'Room1'

Narrate('Action','Reexamine','Room1')


