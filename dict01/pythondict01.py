#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...} """

def main():
    """runtime function"""

    ## create a dictionary with 4 key:value pairs
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    ## display the entire dictionary
    print(switch , '1')

    ## prove that switch is indeed a dictionary
    print(type(switch), '2')

    ## display parts of the dictionary
    print( switch["hostname"] ,'3')    # displays "sw1"
    print( switch["ip"], '4')          # displays "10.0.1.1"

    ## request a 'fake' key
    print( switch.get("lynx"), '5')  # this will cause the program to FAIL  


# call our main function
if __name__ == "__main__":
    main()
