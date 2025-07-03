import time

import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ciscoRouter1 = {'hostname': '10.1.1.10', 'port': 22, 'username': 'gozzki', 'password': 'cisco123'}
ciscoRouter2 = {'hostname': '10.1.1.20', 'port': 22, 'username': 'gozzki', 'password': 'cisco123'}
ciscoRouter3 = {'hostname': '10.1.1.30', 'port': 22, 'username': 'gozzki', 'password': 'cisco123'}

routers = [ciscoRouter1, ciscoRouter2, ciscoRouter3]

for router in routers:
    print(f"Connecting to {router['hostname']}")
    ssh_client.connect(**ciscoRouter1, look_for_keys=False, allow_agent=False)
    shell = ssh_client.invoke_shell()

    shell.send('enable\n')
    shell.send('cisco123\n')
    shell.send('config t\n')
    shell.send('router ospf 1\n')
    shell.send('net 0.0.0.0 0.0.0.0 area 0 \n')
    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('sh ip protocols\n')

    time.sleep(2)

    output = shell.recv(10000).decode()
    print(output)



if ssh_client.get_transport().is_active() == True:
    print("Closing connection")
    ssh_client.close()


