import json
import datetime
import time

def store_data(temp, pres, hum):
    now = datetime.datetime.now()
    #letime=datetime.datetime.now()
    # Store the values in a json file
    data = {
        
        "Date/Time": str(now.strftime("%d.%m.%Y//%H:%M")),
        "Temperature": int(temp),
        "Pressure": int(pres),
        "Humidity": int(hum)
    }
    with open('/home/pi/Desktop/schule/software_wetter_station/main_program/data.json', 'w') as outfile:
        json.dump(data, outfile)