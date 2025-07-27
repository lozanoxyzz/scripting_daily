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

commands = ['access-list 101 permit tcp any any eq 80', 'access-list 101 permit tcp any any eq 443',
            'access-list 101 deny ip any any']

output = connection.send_config_set(commands)
print(output)


connection.disconnect()