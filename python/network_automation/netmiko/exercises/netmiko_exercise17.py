from netmiko import ConnectHandler
import threading
import time

start = time.time()


def execute(device, command_list):
    connection = ConnectHandler(**device)
    connection.enable()
    output = connection.send_config_set(command_list)
    print(output)
    connection.disconnect()


router1 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.10.1',
    'username': 'gozzki',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
    'verbose': True
}

cmd1 = ['router ospf 1', 'network 0.0.0.0 0.0.0.0 area 0']

router2 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.10.2',
    'username': 'gozzki',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
    'verbose': True
}

cmd2 = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'sh ip int loopback 0']


router3 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.10.3',
    'username': 'gozzki',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
    'verbose': True
}

cmd3 = ['username k9 secret abck9', 'ip domain-name k9']

routers = [(router1, cmd1), (router2, cmd2), (router3, cmd3)]

threads = []

for router in routers:
    th = threading.Thread(target=execute, args=(router[0], router[1]))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

end = time.time()

print(end-start)