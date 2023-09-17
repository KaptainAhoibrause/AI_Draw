import serial
import time

a = 0
b = 1

arduino = serial.Serial(port = 'COM3', baudrate =115200, timeout = .1)

coordinates = [1,2,3,4,5,6,7,8,9,10]

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

while True:
    try:
        num = coordinates[b]
        value = write_read(num)
        num = coordinates[a]
        value = write_read(num)
        print(value)
        a = a + 2
        b = b + 2
    except:
        break
    time.sleep(3)