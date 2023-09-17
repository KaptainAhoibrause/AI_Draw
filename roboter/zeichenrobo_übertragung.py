import serial
import time


arduino = serial.Serial(port = 'COM3', baudrate =115200, timeout = .1)

coordinates = [190, 300, 400,200, 500, 200, 190, 290 ]

def write_read(x):
    arduino.write(bytes(str(x), 'utf-8'))

for y in range(0, len(coordinates)//2):
    a = coordinates[2 * y]
    b = coordinates[2 * y + 1]
    print(a, b)
    write_read(a)
    write_read(b)
    time.sleep(3)
