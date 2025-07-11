import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router1 = {'hostname': '10.10.10.1', 'port':22, 'username':'gozzki', 'password': 'cisco'}
router2 = {'hostname': '10.10.10.2', 'port':22, 'username':'gozzki', 'password': 'cisco'}
router3 = {'hostname': '10.10.10.3', 'port':22, 'username':'gozzki', 'password': 'cisco'}

routers = [router1, router2, router3]

for router in routers:
    print(f"Connecting to {router['hostname']}")
    client.connect(**router, look_for_keys=False, allow_agent=False)
    shell = client.invoke_shell()
    shell.send("terminal length 0\n")
    time.sleep(1)
    shell.send("enable\n")
    time.sleep(1)
    shell.send("cisco\n")
    time.sleep(1)
    shell.send("show run\n")
    time.sleep(1)

    output = shell.recv(10000).decode()
    output_list = output.splitlines()
    output_list = output_list[10:-1]
    output = '\n'.join(output_list)

    from datetime import datetime

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    file_name = f'{router['hostname']}_{year}-{month}-{day}.txt'

    with open(file_name, 'w') as f:
        f.write(output)




if client.get_transport().is_active():
    print("Closing connection")
    client.close()
