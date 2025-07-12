import paramiko
from scp import SCPClient

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = {'hostname': '192.168.1.9', 'port':22, 'username': 'lozano', 'password': 'lozano'}

client.connect(**host, look_for_keys=False, allow_agent=False)

scp = SCPClient(client.get_transport())

#copy a file
scp.put('router1-backup.txt', '/tmp/aa.txt')

#copy a directory
scp.put('../paramiko', recursive=True, remote_path='/tmp')

scp.get('/etc/passwd', '/home/gustavo-lozano/Documents/clone_projects/scripting_daily/python/network_automation/paramiko/')
scp.close()