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

output1 = connection.send_command('sh ip int br')
print(output1 + '\n' + ('#' * 30))

output2 = connection.send_command('sh run')
print(output2 + '\n' + ('#' * 30))

hostname = connection.find_prompt()[:-1]

with open(f'{hostname}-sh_ip_int_br.txt' , 'w') as f:
    f.write(output1)

with open(f'{hostname}-sh_run.txt' , 'w') as f:
    f.write(output2)

connection.disconnect()