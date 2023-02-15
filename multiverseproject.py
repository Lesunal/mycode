#!/usr/bin/python3
"""This script will evaluate the number of multiverses you've created today, judge you for your lifestyle choices, and find your anti-person!!!"""




def main():
    #initialization statement, creates count value
    print("Welcome to your window into the multiverse! Did you know that existential dread is free? Now you do! Let's begin.")
    global choice_count
    global question_count
    global choice_dict
    global anti_dict
    global user_name
    global user_invert

    choice_count = 1
    question_count = 1
    

    while True:
        user_name = input("What is your true name?\n>").title()
        choice_count += 1
        if user_name.strip() != '':
            print(f"Very well {user_name}, if that is actually your name.")
            break
        else:
            print("I see you have chosen chaos, but I must insist on a name.")

    while True:
        choice = input('You must have already awakened, but have you yet gotten up? yes or no? \n>').lower().strip()
        if choice == 'yes':
            print('A good start!')
            choice_dict = {'in_bed':'no'}
            anti_dict = {'in_bed':'yes'}
            break
        elif choice == 'no':
            print("Well there's always tomorrow...")
            choice_dict = {'in_bed':'yes'}
            anti_dict = {'in_bed':'no'}
            break
        else:
            print("It's one or the other, say yes or say no")

    question()
    conclude()


def question():
    global choice_count
    global question_count
    global choice_dict
    global anti_dict
    global user_name
    global user_invert

    while True:
        choice_bool = input("Have you made any other choices today? yes or no?\n>").lower().strip()
        if choice_bool == 'no':
            break
        elif choice_bool == 'yes':
            question_count += 1
            choice_dict['choice'+ question_count.__str__()]=input("What did you choose? example: To swim in the pool\n>")
            anti_dict['choice'+ question_count.__str__()]=input("What did you not choose? example: To stay out of the water\n>")
            choice_count += 1
        else:
            print("Speak clearly, noone knows what you're talking about!\n")

def conclude():
    global choice_count
    global question_count
    global choice_dict
    global anti_dict
    global user_name
    global user_invert

    multiverses = 2 ** choice_count
    if choice_count <= 2:
        print(f"{user_name}, you are too boring to have made any new realities, your anti-persona is anyone who does something. Come back when you decide to start breathing!\n")
        exit()
    elif choice_count >= 7:
        print("The bifurcations of reality in your wake are incredible!\n")
        choice_count = 7
    elif choice_count >= 3 and choice_count <= 6:
        fill = None
    else:
        print(f"{user_name} are an agent of chaos, the test is ended.\n")
        exit()
    choice_count -= 3
    titles = ["somewhat boring." , "quite interesting." , "certainly intriguing." , "absolutely fascinating!" , "brilliantly fractalline!"]
    anti_titles = [ "fairly dull" , "frankly rotten" , "definitely malevolent" , "horrifically villainous" , "mind-numbingly catastrophic" ]
    
    print(f"In your travels today, you have spawned {multiverses} multiverses! {user_name}, you are {titles[choice_count]}\n")
    user_list = [*user_name]
    list_invert=[]
    for element in user_list:
        list_invert.insert(0,element)
    user_invert=''.join(list_invert).title()
    print(f"But wait! While {user_name}",end='')
    # concatenating all choices
    start = 0
    for choice in choice_dict:
        if choice == 'in_bed':
            fill = None
        elif start != 1:
            print(f" chose {choice_dict[choice]}",end='')
            start = 1
        else:
            print(f" and chose {choice_dict[choice]}",end='')
    print("...\n")
    countdown(int(t))
    print("There was another.\n")
    countdown(int(t))
    print(f"They are...\n")
    countdown(int(t))
    print(f"The {anti_titles[choice_count]} {user_invert}!")
    print(f"{user_invert}",end='')
    start = 0
    for choice in anti_dict:
        if choice == 'in_bed':
            fill = None
        elif start != 1:
            print(f" chose {anti_dict[choice]}",end='')
            start = 1
        else:
            print(f" and chose {anti_dict[choice]}",end='')

    print(".\nBut fear not!")
    if choice_dict['in_bed'] == 'yes':
        print(f"You never got out of bed and so are safe from {user_invert}'s machinations!")
    elif choice_dict['in_bed'] == 'no':
        print(f"{user_invert} paradoxically never got out of bed today, you're saved!")
    else:
        print("The end times have arrived!")

    print("Remember to be careful when thinking existentially.\nGood Luck, and Good Night!")
    exit()
# import the time module
import time

# define the countdown func.
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1

# input time in seconds
t = 7

main()    
