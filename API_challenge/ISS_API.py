#!/user/bin/env python3

"""Issues an api request to ISS now and outputs current ISS lat/long data and current time"""
import requests
import time

url = 'http://api.open-notify.org/iss-now.json'
def main():
    response = requests.get(url).json()
    print("CURRENT LOCATION OF THE ISS:")
    for key in response['iss_position']:
        print(key,': ', response['iss_position'][key])

    epoch = response["timestamp"]
    print(epoch)
    my_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))

    print(my_time)
main()

