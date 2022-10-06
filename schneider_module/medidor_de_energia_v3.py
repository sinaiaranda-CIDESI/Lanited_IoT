import minimalmodbus
import time
import serial
from datetime import datetime

def read_energy_monitor():
    current_ph1=0
    current_ph2=0
    current_ph3=0 
    current_avg=0 
    voltage_L1_L2=0 
    voltage_L2_L3=0 
    voltage_L3_L1=0 
    active_power_L1=0 
    active_power_L2=0 
    active_power_L3=0 
    total_active_power=0 
    total_reactive_power=0 
    total_apparent_power=0 
    power_factor=0
    frequency=0
    
    #instrument = minimalmodbus.Instrument('COM6', 1, 'rtu')
    #instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
    #instrument.serial.port
    #instrument.serial.baudrate= 19200
    #instrument.serial.parity= serial.PARITY_NONE
    #instrument.serial.bytesize = 8
    #instrument.serial.stopbits = 1
    #instrument.close_port_after_each_call = True
    #instrument.clear_buffers_before_each_transaction = True
    #current_ph1 = round(instrument.read_float(0x0BB7,3,2,0),2)
    #current_ph2 = round(instrument.read_float(0x0BB9,3,2,0),2)
    #current_ph3 = round(instrument.read_float(0x0BBB,3,2,0),2)
    #current_avg= round(instrument.read_float(0x0BC1,3,2,0),2)
    #voltage_L1_L2= round(instrument.read_float(0x0BCB,3,2,0),2)
    #voltage_L2_L3= round(instrument.read_float(0x0BCD,3,2,0),2)
    #voltage_L3_L1= round(instrument.read_float(0x0BCF,3,2,0),2)
    #active_power_L1= round(instrument.read_float(0x0BED,3,2,0),2)
    #active_power_L2= round(instrument.read_float(0x0BEF,3,2,0),2)
    #active_power_L3= round(instrument.read_float(0x0BF1,3,2,0),2)
    #total_active_power= round(instrument.read_float(0x0BF3,3,2,0),2)
    #total_reactive_power= round(instrument.read_float(0x0BFB,3,2,0),2)
    #total_apparent_power= round(instrument.read_float(0x0C03,3,2,0),2)
    #power_factor= round(instrument.read_float(0x0C0B,3,2,0)-0.08,2) #para medidor de 63A
    #power_factor= round(instrument.read_float(0x0C0B,3,2,0)*0.5,2) #para medidor de 125A
    #frequency= round(instrument.read_float(0x0C25,3,2,0),2) 
    
    
    data_set = {
    'CURRENT_PH1': {'VALUE' : current_ph1, 'TIMESTAMP' : str(datetime.now().isoformat())}, 
    'CURRENT_PH2': {'VALUE' : current_ph2, 'TIMESTAMP' : str(datetime.now().isoformat())},
    'CURRENT_PH3': {'VALUE' : current_ph3, 'TIMESTAMP' : str(datetime.now().isoformat())}, 
    'CURRENT_AVG': {'VALUE' : current_avg, 'TIMESTAMP' : str(datetime.now().isoformat())},
    'VOLTAGE_L1_L2': {'VALUE' : voltage_L1_L2, 'TIMESTAMP' : str(datetime.now().isoformat())}, 
    'VOLTAGE_L2_L3': {'VALUE' : voltage_L2_L3, 'TIMESTAMP' : str(datetime.now().isoformat())},
    'VOLTAGE_L3_L1': {'VALUE' : voltage_L3_L1, 'TIMESTAMP' : str(datetime.now().isoformat())}, 
    'ACTIVE_POWER_L1': {'VALUE' : active_power_L1, 'TIMESTAMP' : str(datetime.now().isoformat())},
    'ACTIVE_POWER_L2': {'VALUE' : active_power_L2, 'TIMESTAMP' : str(datetime.now().isoformat())}, 
    'ACTIVE_POWER_L3': {'VALUE' : active_power_L3, 'TIMESTAMP' : str(datetime.now().isoformat())},
    'TOTAL_ACTIVE_POWER': {'VALUE' : total_active_power, 'TIMESTAMP' : str(datetime.now().isoformat())},
    'TOTAL_REACTIVE_POWER': {'VALUE' : total_reactive_power, 'TIMESTAMP' : str(datetime.now().isoformat())}, 
    'TOTAL_APPARENT_POWER': {'VALUE' : total_apparent_power, 'TIMESTAMP' : str(datetime.now().isoformat())},
    'POWER_FACTOR': {'VALUE' : power_factor, 'TIMESTAMP' : str(datetime.now().isoformat())},
    'FREQUENCY': {'VALUE' : frequency, 'TIMESTAMP' : str(datetime.now().isoformat())}
    }

    return data_set
