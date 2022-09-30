import minimalmodbus
import time
import serial

def read_energy_monitor():
    instrument = minimalmodbus.Instrument('COM6', 1, 'rtu')
    #instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) conexión con LINUX
    instrument.serial.port
    instrument.serial.baudrate= 19200
    instrument.serial.parity= serial.PARITY_NONE
    instrument.serial.bytesize = 8
    instrument.serial.stopbits = 1
    instrument.close_port_after_each_call = True
    instrument.clear_buffers_before_each_transaction = True
    current_ph1 = round(instrument.read_float(0x0BB7,3,2,0),2)
    current_ph2 = round(instrument.read_float(0x0BB9,3,2,0),2)
    current_ph3 = round(instrument.read_float(0x0BBB,3,2,0),2)
    current_avg= round(instrument.read_float(0x0BC1,3,2,0),2)
    voltage_L1_L2= round(instrument.read_float(0x0BCB,3,2,0),2)
    voltage_L2_L3= round(instrument.read_float(0x0BCD,3,2,0),2)
    voltage_L3_L1= round(instrument.read_float(0x0BCF,3,2,0),2)
    active_power_L1= round(instrument.read_float(0x0BED,3,2,0),2)
    active_power_L2= round(instrument.read_float(0x0BEF,3,2,0),2)
    active_power_L3= round(instrument.read_float(0x0BF1,3,2,0),2)
    total_active_power= round(instrument.read_float(0x0BF3,3,2,0),2)
    total_reactive_power= round(instrument.read_float(0x0BFB,3,2,0),2)
    total_apparent_power= round(instrument.read_float(0x0C03,3,2,0),2)
    #power_factor= round(instrument.read_float(0x0C0B,3,2,0)-0.08,2) #para medidor de 63A
    power_factor= round(instrument.read_float(0x0C0B,3,2,0)*0.5,2) #para medidor de 125A
    frequency= round(instrument.read_float(0x0C25,3,2,0),2) 
    json_energy= {'Corriente L1: {current_ph1} A', 'Corriente L2: {current_ph2} A', 'Corriente L3: {current_ph3} A', 
                 'Corriente Promedio: {current_avg} A', 'Voltaje L1-L2: {voltage_L1_L2} V', 'Voltaje L2-L3: {voltage_L2_L3} V',
                 'Voltaje L3-L1: {voltage_L3_L1} V', 'Potencia Activa L1: {active_power_L1} kW', 'Potencia Activa L2: {active_power_L2} kW',
                 'Potencia Activa L3: {active_power_L3} kW', 'Potencia Activa Total: {total_active_power} kW', 'Potencia Reactiva Total: {total_reactive_power} kVAR',
                 'Potencia Aparente Total: {total_apparent_power} kVA', 'Factor de Potencia: {power_factor}','Frecuencia: {frequency}'}

    return json_energy

if __name__ == "__main__":
    while True:
        read_energy_monitor()
        time.sleep(2)

