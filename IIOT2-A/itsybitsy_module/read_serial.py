import serial
import json
from datetime import datetime

ser = serial.Serial("/dev/ttyS1", 9600)

def read_data():
    try:
        cc=str(ser.readline())
        data = json.loads(cc[2:][:-5])
        
        data_set = {
            'TEMPERATURE': {'VALUE' : data ['temperature'], 'TIMESTAMP' : str(datetime.now().isoformat())}, 
            'HUMIDITY': {'VALUE' : data ['humidity'], 'TIMESTAMP' : str(datetime.now().isoformat())}
            }
    except:
        t = str(datetime.now().isoformat())
        
        data_set = {
            'TEMPERATURE': {'VALUE' : 0, 'TIMESTAMP' : t}, 
            'HUMIDITY': {'VALUE' : 0, 'TIMESTAMP' : t}
            }
            
    return data_set
