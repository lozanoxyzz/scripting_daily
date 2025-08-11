import telnetlib
import time

# connecting to the remote device (telnet server)
tn = telnetlib.Telnet('10.10.10.1')

tn.read_until(b'Username: ')
tn.write(b'gozzki\n')  # sending the username

tn.read_until(b'Password: ')
tn.write(b'cisco\n')  # sending the user's password

tn.write(b'terminal length 0\n')
tn.write(b'show ip int brief\n')
tn.write(b'exit\n')
time.sleep(1)

# getting and printing the output
output = tn.read_all()
output = output.decode()
print(output)