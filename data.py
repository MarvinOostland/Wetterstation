import json
import datetime
import time

def store_data(temp, pres, hum):
    # Store the values in a json file
    data = {
        "date": datetime.datetime.now(),
        "temperature": temp,
        "pressure": pres,
        "humidity": hum
    }
    with open('/home/pi/Desktop/schule/software_wetter_station/main_program/data.json', 'w') as outfile:
        json.dump(data, outfile)