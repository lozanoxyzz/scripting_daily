import json

from napalm import get_network_driver

driver = get_network_driver('ios')
optional_args = {'secret': 'cisco'}
ios = driver('10.10.10.1', 'gozzki', 'cisco', optional_args=optional_args)

ios.open()

output = ios.ping(destination='10.10.10.2', count=2, source='1.1.1.1')
ping = json.dumps(output, sort_keys=True, indent=4)

print(ping)


ios.close()
