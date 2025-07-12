import paramiko
import time
import getpass

# CONNECTING
ssh_client = paramiko.SSHClient()
#print(type(ssh_client))


# tells python that doesn't matter if you've never connected to this host, connect anyway.
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# ssh_client.connect(hostname="10.10.10.1", port=22, username= 'gozzki', password='cisco123',
#                    look_for_keys=False, allow_agent=False)

password = getpass.getpass('Enter your password: ')
router = {'hostname': '10.10.10.1', 'port':22, 'username': 'gozzki', 'password':password}
ssh_client.connect(**router, look_for_keys= False, allow_agent=False)

print(f"Connecting to {router['hostname']}")

shell = ssh_client.invoke_shell()

### SENDING

shell.send("terminal length 0\n")
shell.send("show version\n")
shell.send('show ip int brief\n')
time.sleep(1)
output = shell.recv(10000)
# print(type(output))
output = output.decode('utf-8')
print(output)








###CLOSING
if ssh_client.get_transport().is_active() == True:
    print("Clossing connection")
    ssh_client.close()