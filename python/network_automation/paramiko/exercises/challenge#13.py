import myparamiko


router1 = {'hostname': '10.10.10.1', 'port': 22, 'username': "gozzki", 'password': 'cisco', 'config': 'ospf.txt'}

router2 = {'hostname': '10.10.10.2', 'port': 22, 'username': "gozzki", 'password': 'cisco', 'config': 'eigrp.txt'}

router3 = {'hostname': '10.10.10.3', 'port': 22, 'username': "gozzki", 'password': 'cisco', 'config': 'router3.conf'}

routers = [router1, router2, router3]

for router in routers:
    client = myparamiko.connect(router['hostname'], router['port'], router['username'], router['password'])
    shell = myparamiko.get_shell(client)
    myparamiko.send_from_file(shell, router['config'])
    print(myparamiko.show(shell))
    myparamiko.close(client)