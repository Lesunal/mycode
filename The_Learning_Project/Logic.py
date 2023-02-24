"""This file is where the program is executed"""

import random
from Terms import words
from Learning_Objects import python 

H = None

def main():
    H = None 

    # Creating the Learning_Objective class
    class Learning_Objective:
        def __init__(self, name, arguments, syntax, prereq):
            self.name = name
            self.arguments = arguments
            self.syntax = syntax
            self.prereq = prereq

   # Eval signal Placeholder
    targets = ["print","input"]

    target_script = ''

   # Example of print and input function as learning objectives, here before being moved to storage file
   # loop will insert elements into script for each Learning_Objective
    for target in targets:
        Target = Learning_Objective(python[target],python[target]['arguments'],python[target]['syntax'],python[target]['prereq'] )

        # Test Print
        #print(Target.syntax)

        target_script = target_script +'\n'+ Target.syntax

        # Test Print
    
    #eval(target_script)
    # Run the formulated script
    run(target_script)
   
  # Define function for running assembled script
def run(target_script):
    #print(target_script)
   # Evaluate the string to get the output
    lines = target_script.strip().splitlines()
    print(lines)
    for line in lines:
        eval(line) 
    



main()