import serial
import time

ser = serial.Serial('/tmp/ttyS2', 9600, timeout=1)
time.sleep(1)

ser.write(b'\n')
time.sleep(0.5)
print(ser.read(500).decode(errors='ignore'))

ser.write(b'show version\n')
time.sleep(1)

output = b''

while True:
    data = ser.read(100)
    if not data:
        break
    output+= data

print(output.decode())
ser.close()
