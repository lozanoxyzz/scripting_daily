import myparamiko

router1 = {'hostname': '10.10.10.2', 'port': 22, 'username':'gozzki', 'password': 'cisco'}

client = myparamiko.connect(**router1)
shell = myparamiko.get_shell(client)

myparamiko.send_from_file(shell, 'commands.txt')

output = myparamiko.show(shell,10000)
print(output)

myparamiko.close(client)