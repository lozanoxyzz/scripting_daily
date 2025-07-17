import paramiko
import time
import getpass
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
password = getpass.getpass('Password: ')

router1 = {'hostname': '10.10.10.1', 'port': 22, 'username':'gozzki', 'password': password}
router2 = {'hostname': '10.10.10.2', 'port': 22, 'username':'gozzki', 'password': password}
router3 = {'hostname': '10.10.10.3', 'port': 22, 'username':'gozzki', 'password': password}

client.connect(**router1, look_for_keys=False, allow_agent=False)

shell = client.invoke_shell()

shell.send('enable\n')
time.sleep(1)
shell.send('cisco\n')
time.sleep(1)
shell.send('terminal length 0\n')
time.sleep(1)
shell.send('show users\n')
time.sleep(1)

output = shell.recv(10000)

with open('users_file.txt' , 'w') as f:
    f.write(output.decode())

if client.get_transport().is_active():
    client.close()
    print('Closing connection')