# Create a Python script that connects to a Cisco Router using Telnet and
# executes the show users command in order to display the logged-in users.
#
# Print out the output of the command.

import telnetlib
import time

router = {'host':'10.10.10.1', 'user':'gozzki', 'password':'cisco'}

tn = telnetlib.Telnet('10.10.10.1')

tn.read_until(b'Username: ')
tn.write(b'gozzki\n')


tn.read_until(b'Password: ')
tn.write(b'cisco\n')


tn.write(b'terminal length 0\n')
tn.write(b'show users\n')
tn.write(b'exit\n')
time.sleep(1)

output = tn.read_all()
print(output.decode())
