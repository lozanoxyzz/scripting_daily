import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

linux = {'hostname': '192.168.1.10', 'port': 22, 'username': 'lozano', 'password': 'lozano'}

print(f"Connecting to {linux['hostname']}")
ssh_client.connect(**linux, look_for_keys = False, allow_agent= False)

stdin, stdout, stderror = ssh_client.exec_command('sudo useradd u2\n', get_pty=True)

stdin.write('lozano\n')
time.sleep(2)

stdin, stdout, stderror = ssh_client.exec_command('cat /etc/passwd\n')
output = stdout.read()
output = output.decode()
print(output)
time.sleep(1)

if ssh_client.get_transport().is_active() == True:
    print('Clossing connection')
    ssh_client.close()