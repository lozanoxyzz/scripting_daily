from netmiko import ConnectHandler
from datetime import datetime
import time

start = time.time()

now = datetime.now()

year = now.year
month = now.month
day = now.day

with open('devices.txt') as f:
    devices = f.read().splitlines()

device_list = []

for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'gozzki',
        'password': 'cisco',
        'port':22,
        'secret':'cisco',
        'verbose':True
    }
    device_list.append(cisco_device)
for device in device_list:
    connection = ConnectHandler(**device)
    print('Entering enable mode...')
    connection.enable()

    output = connection.send_command('sh run')
    #print(output)
    prompt = connection.find_prompt()
    hostname = prompt[0:-1]
    #print(hostname)

    filename = f'{hostname}_{year}-{month}-{day}_backup.txt'

    with open(filename , 'w') as f:
        f.write(output)
        print(f'Backup of {hostname} completeted succesfully')

    print('Closing connection')
    connection.disconnect()
    print('#' * 30)

end = time.time()
print(end - start)