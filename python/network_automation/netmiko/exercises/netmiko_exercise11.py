from netmiko import ConnectHandler

IPs = ['10.10.10.1', '10.10.10.2', '10.10.10.3']
routers = []

for ip in IPs:
    cisco_device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'gozzki',
        'password': 'cisco',
        'secret': 'cisco',
        'port': 22,
        'verbose': True
    }

    routers.append(cisco_device)


for router in routers:
    connection = ConnectHandler(**router)

    if '>' in connection.find_prompt():
        connection.enable()

    output = connection.send_command('sh ip int br')
    print(output + '\n' + ('#' * 50))



    connection.disconnect()