import telnetlib
import time

host = '10.10.10.1'
port = 23
user = 'gozzki'
password = 'cisco'

tn = telnetlib.Telnet(host=host, port=port)

tn.read_until(b'Username: ')
tn.write(user.encode() + b'\n')

tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')

tn.write(b'terminal length 0\n')
tn.write(b'sh ip int br\n')
tn.write(b'sh run\n')
tn.write(b'exit\n')
time.sleep(1)

output = tn.read_all().decode()
print(output)
