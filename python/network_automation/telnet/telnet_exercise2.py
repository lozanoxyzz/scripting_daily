# Change the solution from the previous challenge so that it will prompt the user for its password without echoing
# (use getpass module). Run the script in the terminal (you can not run it in PyCharm).

import telnetlib
import time
import getpass

tn = telnetlib.Telnet('10.10.10.1')

tn.read_until(b'Username: ')
username = getpass.getpass('Username: ')
tn.write(username.encode() + b'\n')

tn.read_until(b'Password: ')
password = getpass.getpass('Password: ')
tn.write(password.encode() + b'\n')



tn.write(b'terminal length 0\n')
tn.write(b'show users\n')
tn.write(b'exit\n')
time.sleep(1)

tn.close()

output = tn.read_all()
print(output.decode())
