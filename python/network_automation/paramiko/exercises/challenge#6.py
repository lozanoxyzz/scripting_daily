import paramiko
import time

# creating an ssh client object
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('Connecting to 10.10.10.1')
ssh_client.connect(hostname='10.10.10.1', port='22', username='gozzki', password='cisco',
                   look_for_keys=False, allow_agent=False)


shell = ssh_client.invoke_shell()
shell.send('enable\n')
time.sleep(1)
shell.send('cisco\n')
time.sleep(1)
shell.send('terminal length 0\n')
time.sleep(1)
shell.send('show ip int brief\n')
time.sleep(1)


output = shell.recv(100000).decode()
print(output)


if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()