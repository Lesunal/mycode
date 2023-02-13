#! /usr/bin/python3
# the below is another example of commented out text
"""Alta3 Research | RZFeeser
    print() - display data to std out"""


#Practice comments, we are first defining our main function
def main():

    # pause the program and wait for the user to provide input
    user_input = input("Please enter an IPv4 IP address:")

    # we will display the input back to the user
    print("You told me the IPv4 adddress is: " + user_input)

    vendor = input("Please input the vendor name")
    print("Your vendor is" + " " + vendor)

# call the main to run the defined function
main()
