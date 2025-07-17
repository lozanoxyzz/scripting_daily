import paramiko
import time



def execute_command(device, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(**device, look_for_keys=False, allow_agent=False)
    shell = client.invoke_shell()
    print(f'Sending {command} to {device['hostname']}')
    shell.send('enable\n')
    shell.send('cisco\n')
    shell.send('terminal length 0\n')
    shell.send(command + '\n')
    time.sleep(1)

    output = shell.recv(10000)
    print(output.decode())

    if client.get_transport().is_active():
        print('Closing connection')
        client.close()


if __name__ == '__main__':
    router1 = {'hostname': '10.10.10.1', 'port': 22, 'username': "gozzki", 'password': 'cisco'}

    router2 = {'hostname': '10.10.10.2', 'port': 22, 'username': "gozzki", 'password': 'cisco'}

    router3 = {'hostname': '10.10.10.3', 'port': 22, 'username': "gozzki", 'password': 'cisco',}

    routers = [router1, router2, router3]

    for router in routers:
        execute_command(router, 'show ip interface brief')
