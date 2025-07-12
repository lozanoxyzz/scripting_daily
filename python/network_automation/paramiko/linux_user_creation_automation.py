import myparamiko
import getpass

username = getpass.getpass('Username: ')
password = getpass.getpass('Password: ')

client = myparamiko.connect('192.168.1.9', 22, username, password)
remote_connection = myparamiko.get_shell(client)


user_to_be_created = input('Type the name of the new user: ')
myparamiko.send_command(remote_connection, f'sudo useradd -m -d /home/{user_to_be_created} -s /bin/bash {user_to_be_created}')
myparamiko.send_command(remote_connection, password)
print('New user has been created!')

answer = input('Do you want to see the current users? y/n ')
if answer == 'y':
    users = myparamiko.send_command(remote_connection, 'cat /etc/passwd')
    print(users.decode())

myparamiko.close(client)