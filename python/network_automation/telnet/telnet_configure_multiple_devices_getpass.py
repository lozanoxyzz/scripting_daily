import telnetlib
import time
import getpass

router1 = {'host':'10.10.10.1'}
router2 = {'host':'10.10.10.2'}
router3 = {'host':'10.10.10.3'}

routers = [router1, router2, router3]

for router in routers:
    print(f'Connecting to {router['host']}')
    tn = telnetlib.Telnet(router['host'])

    tn.read_until(b'Username: ')
    username = getpass.getpass('Username:')
    tn.write(username.encode() + b'\n')

    tn.read_until(b'Password: ')
    password = getpass.getpass('Password: ')
    tn.write(password.encode() + b'\n')

    tn.write(b'terminal length 0\n')

    tn.write(b'enable\n')
    tn.read_until(b'Password: ')
    tn.write(password.encode() + b'\n')
    tn.write(b'show ip route\n')
    tn.write(b'exit\n')
    time.sleep(1)

    output = tn.read_all()
    print(output.decode())

    tn.close()

    print('#' * 40)