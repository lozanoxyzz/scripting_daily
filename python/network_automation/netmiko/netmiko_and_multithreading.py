from threading import Thread

from netmiko import ConnectHandler
from datetime import datetime
import time
import threading

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

def backup(device):
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

threads = []

for device in device_list:
    th = Thread(target=backup, args=(device,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

end = time.time()
print(end - start)