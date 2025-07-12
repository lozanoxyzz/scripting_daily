import paramiko
import time


linux = {'hostname': '192.168.1.10', 'port': 22, 'username': 'lozano', 'password': 'lozano'}

def connect(hostname, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {hostname}')
    ssh_client.connect(hostname, port, username, password, look_for_keys= False, allow_agent= False)

    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timeout=1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timeout)
    return shell.recv(10000)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active():
        print('Clossing connection')
        ssh_client.close()

if __name__ == '__main__':
    client = connect(**linux)
    shell = get_shell(client)
