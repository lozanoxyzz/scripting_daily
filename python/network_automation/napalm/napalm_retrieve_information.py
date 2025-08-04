from napalm import get_network_driver
import json


driver = get_network_driver('ios')
optional_args = {'secret':'cisco'}
ios = driver('10.10.10.1', 'gozzki', 'cisco', optional_args=optional_args)

ios.open()

output = ios.get_facts()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

print('#' * 50)


output = ios.get_arp_table()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

print('#' * 50)

output = ios.get_interfaces()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

print('#' * 50)

output = ios.get_interfaces_counters()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

print('#' * 50)

output = ios.get_interfaces_ip()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)


ios.close()