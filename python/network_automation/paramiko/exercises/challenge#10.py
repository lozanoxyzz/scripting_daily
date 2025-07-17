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

with open('commands.txt', 'r') as f:
    commands = f.read().splitlines()

for command in commands:
    shell.send(f'{command}\n')
    time.sleep(1)


output = shell.recv(10000)
print(output.decode())

if client.get_transport().is_active():
    client.close()
    print('Closing connection')