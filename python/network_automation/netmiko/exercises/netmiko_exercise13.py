from netmiko import ConnectHandler

def execute(device, command):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    print(output)
    connection.disconnect()

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '10.10.10.1',
    'username': 'gozzki',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
    'verbose': True
}

execute(cisco_device, 'show version')

linux = {
    'device_type': 'linux',
    'ip': '192.168.1.14',
    'username': 'lozano',
    'password': 'lozano',
    'secret': 'lozano',
    'port': 22,
    'verbose': True
}

execute(linux, 'ip a')