# from netmiko import Netmiko
#
# connection = Netmiko(host='10.10.10.1', port='22', username='gozzki', password='cisco', device_type='cisco_ios')

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

if '>' in connection.find_prompt():
    connection.enable()

output = connection.send_command('sh run')
print(output)

if not connection.check_config_mode():
    connection.config_mode()

#print(connection.check_config_mode())

connection.send_command('username u3 secret cisco')



print('Closing connection')
connection.disconnect()