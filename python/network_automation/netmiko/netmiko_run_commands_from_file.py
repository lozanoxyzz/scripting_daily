from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.10.10.1',
    'username': 'gozzki',
    'password': 'cisco',
    'port':22,
    'secret':'cisco',
    'verbose':True
}

connection = ConnectHandler(**cisco_device)

print('Enabling enable mode...')
connection.enable()

# with open('ospf.txt', 'r') as f:
#     commands = f.read().splitlines()
#
# output = connection.send_config_set(commands)
# print(output)

connection.send_config_from_file('ospf.txt')

print('Closing connection')
connection.disconnect()