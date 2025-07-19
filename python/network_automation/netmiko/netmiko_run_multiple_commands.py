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
print('Entering the enable mode...')
connection.enable()

#commands = ['int lo0', 'ip add 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret cisco']
#cmd = 'ip ssh version 2; access-list 1 permit any; ip domain-name network-automation.io'
cmd = '''ip ssh version 2
access-list 1 permit any
ip domain-name net-auto.io
'''
print(connection.send_config_set(cmd.split('\n')))
print(connection.find_prompt())

connection.send_command('wr memo')

print('Closing connection')
connection.disconnect()