import myparamiko
import threading

def backup(router):
    client = myparamiko.connect(**router)
    shell = myparamiko.get_shell(client)

    myparamiko.send_command(shell, 'terminal length 0')
    myparamiko.send_command(shell, 'enable')
    myparamiko.send_command(shell, 'cisco')
    myparamiko.send_command(shell, 'show run')

    output = myparamiko.show(shell)

    output_list = output.splitlines()
    output_list = output_list[10:-1]
    output = '\n'.join(output_list)

    from datetime import datetime

    now = datetime.now()

    year = now.year
    month = now.month
    day = now.day

    file_name = f"{router['hostname']}_{year}-{month}-{day}.txt"

    with open(file_name, 'w') as f:
        f.write(output)

    myparamiko.close(client)

router1 = {'hostname': '10.10.10.1', 'port':22, 'username':'gozzki', 'password': 'cisco'}
router2 = {'hostname': '10.10.10.2', 'port':22, 'username':'gozzki', 'password': 'cisco'}
router3 = {'hostname': '10.10.10.3', 'port':22, 'username':'gozzki', 'password': 'cisco'}

routers = [router1, router2, router3]
threads = []


for router in routers:
    th = threading.Thread(target=backup, args=(router,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()