import json
import datetime
import time

def store_data(temp, pres, hum):
    now = datetime.datetime.now()
    #letime=datetime.datetime.now()
    # Store the values in a json file
    data = {
        
        "date": str(now.strftime("%d.%m.%Y//%H:%M")),
        "temperature": temp,
        "pressure": pres,
        "humidity": hum
    }
    with open('/home/pi/Desktop/schule/software_wetter_station/main_program/data.json', 'w') as outfile:
        json.dump(data, outfile)