from netmiko import ConnectHandler, file_transfer
from netmiko import FileTransfer


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

transfer_output = file_transfer(connection, source_file='ospf.txt', dest_file='ospf1.txt', file_system='disk0:',
                                direction='put', overwrite_file=True)

print(transfer_output)

connection.disconnect()