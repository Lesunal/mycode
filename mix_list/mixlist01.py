#! /usr/bin/env python3

#This is is a script dealing with lists with mixed element attributes
#Each statement references a list item identified by its place in the list counting from 0-2
my_list = [ "192.168.0.5", 5060, "UP" ] 
print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + my_list[1].__str__() )
print("The third item in the list (state): " + my_list[2] )

