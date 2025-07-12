import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

linux = {'hostname': '192.168.1.10', 'port': 22, 'username': 'lozano', 'password': 'lozano'}

print(f"Connecting to {linux['hostname']}")
ssh_client.connect(**linux, look_for_keys = False, allow_agent= False)

shell = ssh_client.invoke_shell()
shell.send('sudo cat /etc/shadow\n')
shell.send('lozano\n')
time.sleep(1)

output = shell.recv(10000)
output = output.decode('utf-8')

print(output)




if ssh_client.get_transport().is_active() == True:
    ssh_client.close()