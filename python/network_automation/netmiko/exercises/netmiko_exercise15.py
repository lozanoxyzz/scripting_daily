from netmiko_exercise14 import execute

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
    'ip': '10.10.10.2',
    'username': 'gozzki',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
    'verbose': True
}

cmd3 = ['username k9 secret abck9', 'ip domain-name k9']

routers = [(router1, cmd1), (router2, cmd2), (router3, cmd3)]

for router in routers:
    execute(router[0], router[1])
