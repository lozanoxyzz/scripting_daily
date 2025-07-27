from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '10.10.10.1',
    'username': 'gozzki',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
    'verbose': True
}

connection = ConnectHandler(**cisco_device)

print(connection.find_prompt()[:-1])

connection.disconnect()
