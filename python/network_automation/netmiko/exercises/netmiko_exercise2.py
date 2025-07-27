from netmiko import ConnectHandler

with open('device_information.txt') as f:
    content = f.read()
    info = content.split(':')


cisco_device = {
        'device_type': 'cisco_ios',
        'ip': info[0],
        'username': info[2],
        'password': info[3],
        'secret': info[4],
        'port': info[1],
        'verbose': True
    }


connection = ConnectHandler(**cisco_device)

if '>' in connection.find_prompt():
    connection.enable()

output = connection.send_command('sh arp')
print(output)

connection.disconnect()