import telnet_class

tn = telnet_class.Device('10.10.10.1', 'gozzki', 'cisco')

tn.connect()
tn.authenticate()

tn.send_from_file('file.txt')

output = tn.show()
print(output)