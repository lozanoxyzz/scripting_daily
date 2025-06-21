import paramiko
from cloudinit.distros.parsers import hostname

# CONNECTING
ssh_client = paramiko.SSHClient()
#print(type(ssh_client))


print("Connecting to 10.10.10.1")
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname="10.10.10.1", port=22, username= 'gozzki', password='cisco123',
                   look_for_keys=False, allow_agent=False)

print(ssh_client.get_transport().is_active())

### SENDING






###CLOSING
print("Clossing connection")
ssh_client.close()