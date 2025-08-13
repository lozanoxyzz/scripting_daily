import serial
import time


with serial.Serial(port='/tmp/ttyS2', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=8) as console:
    if console.isOpen():
        print('Console successfully opened!')
        console.write(b'\r\n')
        time.sleep(1)
        console.write(b'enable\r\n')
        time.sleep(1)
        console.write(b'terminal length 0\r\n')
        time.sleep(1)
        console.write(b'show version\r\n')
        time.sleep(3)

        bytes_to_be_read = console.inWaiting()
        output = console.read(bytes_to_be_read)
        print(output.decode('utf-8'))

    else:
        print('Error opening the console connection')