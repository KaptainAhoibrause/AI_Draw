import serial
import time


arduino = serial.Serial(port = 'COM3', baudrate =115200, timeout = .1)

coordinates = [1,2,3,4,5,6,7,8,9,10]

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

for y in range(0, len(coordinates)//2):
    a = coordinates[2 * y]
    b = coordinates[2 * y + 1]
    print(a, b)
    write_read(a)
    write_read(b)
    time.sleep(3)