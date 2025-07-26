from netmiko import ConnectHandler
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger('netmiko')



linux = {
    'device_type': 'linux',
    'host': '192.168.1.14',
    'username': 'lozano',
    'password': 'lozano',
    'port': 22,
    'secret': 'lozano',
    'verbose': True
}

connection = ConnectHandler(**linux)

connection.enable()

output = connection.send_command('apt update && apt install -y apache2', read_timeout=30)
output = connection.read_channel()
print(output)




print('Closing connection')
connection.disconnect()

