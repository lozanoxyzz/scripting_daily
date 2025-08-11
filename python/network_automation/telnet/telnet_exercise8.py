# Create a Python script that connects to a Cisco Router using Telnet and executes all the commands from a text file.
#
# An example of a text file with commands.

import telnetlib
import time

with open('file.txt') as f:
    commands = f.read().splitlines()

host = '10.10.10.1'
user = 'gozzki'
password = 'cisco'

tn = telnetlib.Telnet(host)

tn.read_until(b'Username: ')
tn.write(user.encode() + b'\n')

tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')

for command in commands:
    tn.write(command.encode() + b'\n')

tn.write(b'exit\n')

output = tn.read_all().decode()

print(output)