import serial
import json
from datetime import datetime

ser = serial.Serial("/dev/ttyS1", 9600)

def read_data():
    cc=str(ser.readline())
    data = json.loads(cc[2:][:-5])
    
    data_set = {
    'TEMPERATURE': {'VALUE' : data ['temperature'], 'TIMESTAMP' : str(datetime.now().isoformat())}, 
    'HUMIDITY': {'VALUE' : data ['humidity'], 'TIMESTAMP' : str(datetime.now().isoformat())}
    }
    
    return data_set
