import myparamiko

router = {'hostname': '10.10.10.1', 'port': 22, 'username': 'gozzki', 'password': 'cisco' }

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
print(output)

from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

file_name = f'{router['hostname']}_{year}-{month}-{day}.txt'



with open(file_name, 'w') as f:
    f.write(output)



myparamiko.close(client)