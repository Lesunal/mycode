#! /usr/bin/python3

"""Dictionary Challenge Script!"""
# Define main function

def main():
# Save a user's input to the variable char_name
    char_name = input('Which character do you want to know about? (Starlord, Mystique, Hulk)\n>')

# Save a user's input to the variable char_stat
    char_stat = input('What statistic do you want to know about? (real name, powers, archenemy)\n>')

# Establish Dictionary
    marvelchars= {
    "Starlord":
    {"real name": "peter quill",
    "powers": "dance moves",
    "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
    "powers": "shape shifter",
    "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner",
    "powers": "super strength",
    "archenemy": "adrenaline"}
             }

    print(f"{char_name}'s {char_stat} is: {marvelchars.get(char_name).get(char_stat)}")

# Call main function
main()
