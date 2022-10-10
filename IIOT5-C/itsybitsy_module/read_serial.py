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
            'HUMIDITY': {'VALUE' : data ['humidity'], 'TIMESTAMP' : str(datetime.now().isoformat())},
            'VOLTAGE': {'VALUE' : data ['voltage'], 'TIMESTAMP' : str(datetime.now().isoformat())},
            'CURRENT_1': {'VALUE' : data ['current1'], 'TIMESTAMP' : str(datetime.now().isoformat())},
            'CURRENT_2': {'VALUE' : data ['current2'], 'TIMESTAMP' : str(datetime.now().isoformat())}, 
            'CURRENT_3': {'VALUE' : data ['current3'], 'TIMESTAMP' : str(datetime.now().isoformat())},
            'TOTAL_CURRENT': {'VALUE' : data ['total_current'], 'TIMESTAMP' : str(datetime.now().isoformat())}, 
            'POWER': {'VALUE' : data ['power'], 'TIMESTAMP' : str(datetime.now().isoformat())}
            }
    except:
        t = str(datetime.now().isoformat())
        
        data_set = {
            'TEMPERATURE': {'VALUE' : 0, 'TIMESTAMP' : t}, 
            'HUMIDITY': {'VALUE' : 0, 'TIMESTAMP' : t},
            'VOLTAGE': {'VALUE' : 0, 'TIMESTAMP' : t}, 
            'CURRENT_1': {'VALUE' : 0, 'TIMESTAMP' : t},
            'CURRENT_2': {'VALUE' : 0, 'TIMESTAMP' : t}, 
            'CURRENT_3': {'VALUE' : 0, 'TIMESTAMP' : t},
            'TOTAL_CURRENT': {'VALUE' : 0, 'TIMESTAMP' : t}, 
            'POWER': {'VALUE' : 0, 'TIMESTAMP' : t}
            }
            
    return data_set
