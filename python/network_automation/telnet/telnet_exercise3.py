# Create a Python script that connects to a Cisco Router using Telnet, enters the enable mode,
# and then executes the show run command.
# Save the output to a file.


import telnetlib
import time

host = '10.10.10.1'
user = 'gozzki'
password = 'cisco'

tn = telnetlib.Telnet(host)

tn.read_until(b'Username: ')
tn.write(user.encode() + b'\n')

tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')

tn.write(b'terminal length 0\n')
tn.write(b'enable\n')
tn.write(b'cisco\n')
tn.write(b'sh run\n')
tn.write(b'exit\n')

time.sleep(1)

output = tn.read_all().decode()
tn.close()

print(output)
