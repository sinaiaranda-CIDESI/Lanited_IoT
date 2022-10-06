import minimalmodbus
import time
import serial
from datetime import datetime

def read_energy_monitor():    
    try:
        instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
        instrument.serial.port
        instrument.serial.baudrate= 19200
        instrument.serial.parity= serial.PARITY_NONE
        instrument.serial.bytesize = 8
        instrument.serial.stopbits = 1
        instrument.close_port_after_each_call = True
        instrument.clear_buffers_before_each_transaction = True
        
        current_ph1 = round(instrument.read_float(0x0BB7,3,2,0),2)
        current_ph1_t = str(datetime.now().isoformat())
        current_ph2 = round(instrument.read_float(0x0BB9,3,2,0),2)
        current_ph2_t = str(datetime.now().isoformat())
        current_ph3 = round(instrument.read_float(0x0BBB,3,2,0),2)
        current_ph3_t = str(datetime.now().isoformat())
        current_avg = round(instrument.read_float(0x0BC1,3,2,0),2)
        current_avg_t = str(datetime.now().isoformat())
        voltage_L1_L2 = round(instrument.read_float(0x0BCB,3,2,0),2)
        voltage_L1_L2_t = str(datetime.now().isoformat())
        voltage_L2_L3 = round(instrument.read_float(0x0BCD,3,2,0),2)
        voltage_L2_L3_t = str(datetime.now().isoformat())
        voltage_L3_L1 = round(instrument.read_float(0x0BCF,3,2,0),2)
        voltage_L3_L1_t = str(datetime.now().isoformat())
        active_power_L1 = round(instrument.read_float(0x0BED,3,2,0),2)
        active_power_L1_t = str(datetime.now().isoformat())
        active_power_L2 = round(instrument.read_float(0x0BEF,3,2,0),2)
        active_power_L2_t = str(datetime.now().isoformat())
        active_power_L3 = round(instrument.read_float(0x0BF1,3,2,0),2)
        active_power_L3_t = str(datetime.now().isoformat())
        total_active_power = round(instrument.read_float(0x0BF3,3,2,0),2)
        total_active_power_t = str(datetime.now().isoformat())
        total_reactive_power = round(instrument.read_float(0x0BFB,3,2,0),2)
        total_reactive_power_t = str(datetime.now().isoformat())
        total_apparent_power = round(instrument.read_float(0x0C03,3,2,0),2)
        total_apparent_power_t = str(datetime.now().isoformat())
        power_factor= round(instrument.read_float(0x0C0B,3,2,0)-0.08,2)
        power_factor_t = str(datetime.now().isoformat())
        frequency = round(instrument.read_float(0x0C25,3,2,0),2)
        frequency_t = str(datetime.now().isoformat())

    except:
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

        t = str(datetime.now().isoformat())
        current_ph1_t = t
        current_ph2_t = t
        current_ph3_t = t
        current_avg_t = t
        voltage_L1_L2_t = t
        voltage_L2_L3_t = t
        voltage_L3_L1_t = t
        active_power_L1_t = t
        active_power_L2_t = t
        active_power_L3_t = t
        total_active_power_t = t
        total_reactive_power_t = t
        total_apparent_power_t = t
        power_factor_t = t
        frequency_t = t
    
    
    data_set = {
    'CURRENT_PH1': {'VALUE' : current_ph1, 'TIMESTAMP' : current_ph1_t}, 
    'CURRENT_PH2': {'VALUE' : current_ph2, 'TIMESTAMP' : current_ph2_t},
    'CURRENT_PH3': {'VALUE' : current_ph3, 'TIMESTAMP' : current_ph3_t}, 
    'CURRENT_AVG': {'VALUE' : current_avg, 'TIMESTAMP' : current_avg_t},
    'VOLTAGE_L1_L2': {'VALUE' : voltage_L1_L2, 'TIMESTAMP' : voltage_L1_L2_t}, 
    'VOLTAGE_L2_L3': {'VALUE' : voltage_L2_L3, 'TIMESTAMP' : voltage_L2_L3_t},
    'VOLTAGE_L3_L1': {'VALUE' : voltage_L3_L1, 'TIMESTAMP' : voltage_L3_L1_t}, 
    'ACTIVE_POWER_L1': {'VALUE' : active_power_L1, 'TIMESTAMP' : active_power_L1_t},
    'ACTIVE_POWER_L2': {'VALUE' : active_power_L2, 'TIMESTAMP' : active_power_L2_t}, 
    'ACTIVE_POWER_L3': {'VALUE' : active_power_L3, 'TIMESTAMP' : active_power_L3_t},
    'TOTAL_ACTIVE_POWER': {'VALUE' : total_active_power, 'TIMESTAMP' : total_active_power_t},
    'TOTAL_REACTIVE_POWER': {'VALUE' : total_reactive_power, 'TIMESTAMP' :total_reactive_power_t}, 
    'TOTAL_APPARENT_POWER': {'VALUE' : total_apparent_power, 'TIMESTAMP' : total_apparent_power_t},
    'POWER_FACTOR': {'VALUE' : power_factor, 'TIMESTAMP' : power_factor_t},
    'FREQUENCY': {'VALUE' : frequency, 'TIMESTAMP' : frequency_t}
    }

    return data_set
