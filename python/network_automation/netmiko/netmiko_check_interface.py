from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '10.10.10.1',
    'username': 'gozzki',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
    'verbose': True
}

connection = ConnectHandler(**cisco_device)

if '>' in connection.find_prompt():
    connection.enable()

interface = input('Enter the interface you want to enable: ')
output = connection.send_command(f'sh ip int {interface}')

if 'Invalid input detected' in output:
    print("You've entered an invalid interface")
else:
    first_line = output.splitlines()[0]
    if not 'up' in first_line:
        print('The interface is down. Enabling interface ...')
        commands = ['interface ' + interface, 'no shut', 'exit']
        output = connection.send_config_set(commands)
        print(output)
        print('#' * 30)
        print('The interface has been enabled.')
    else:
        print('The interface is already enabled.')

