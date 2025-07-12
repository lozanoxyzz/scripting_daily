import paramiko


ssh_client = paramiko.SSHClient() ####this is the ssh's client
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


router = {'hostname': '10.10.10.1', 'username': 'admin', 'password' : 'cisco123'}

### CONNECTING
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)




##CLOSING
if ssh_client.get_transport().is_active():
    ssh_client.close()
    print('SSH connection closed.')

