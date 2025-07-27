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

connection.config_mode()

connection.send_command('username admin secret topsecret')

connection.exit_config_mode()

connection.send_command('write')


connection.disconnect()