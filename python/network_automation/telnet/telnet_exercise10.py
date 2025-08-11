# Consider a topology with multiple devices like this one.
#
# For each device in the topology, you have a Python dictionary that stores the Telnet connection information (IP, username, password) but also a filename that contains the commands to be sent to that device.
#
# Example:

r1 = {'host': '10.10.10.1', 'username': 'gozzki', 'password': 'cisco', 'config':'ospf.txt'}

r2 = {'host': '10.10.10.2', 'username': 'gozzki', 'password': 'cisco', 'config':'eigrp.txt'}

r3 = {'host': '10.10.10.3', 'username': 'gozzki', 'password': 'cisco', 'config':'router3.conf'}



# Create a Python script that connects to each device using Telnet and executes the commands from the file (which is the value of the dictionary config key).
#
# Use the Telnet Class that was developed in the course or create the entire Python script from scratch.


import telnet_class

routers = [r1,r2,r3]

for router in routers:
    file = router['config']

    router = telnet_class.Device(router['host'], router['username'], router['password'])
    router.connect()
    router.authenticate()

    router.send_from_file(file)
    output = router.show()
    print(output)
    print('#' * 50)

