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

if '>' in connection.find_prompt():
    connection.enable()

output = connection.send_command('sh arp')
print(output)

connection.disconnect()