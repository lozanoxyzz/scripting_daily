from netmiko import ConnectHandler
from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day

IPs = ['10.10.10.1', '10.10.10.2', '10.10.10.3']
routers = []

for ip in IPs:
    cisco_device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'gozzki',
        'password': 'cisco',
        'secret': 'cisco',
        'port': 22,
        'verbose': True
    }

    routers.append(cisco_device)


for router in routers:
    connection = ConnectHandler(**router)

    if '>' in connection.find_prompt():
        connection.enable()

    output = connection.send_command('sh ip int br')

    filename = f'{connection.find_prompt()[:-1]}-{year}_{month}_{day}.txt'
    with open(filename, 'w') as f:
        f.write(output)


    connection.disconnect()