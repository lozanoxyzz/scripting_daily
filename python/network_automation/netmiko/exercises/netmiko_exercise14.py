from netmiko import ConnectHandler

def execute(device, command_list):
    connection = ConnectHandler(**device)
    connection.enable()
    output = connection.send_config_set(command_list)
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
cmd = ['no router rip', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'sh ip int loopback 0']
execute(cisco_device, cmd)

