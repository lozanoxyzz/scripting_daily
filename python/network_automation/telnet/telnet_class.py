import time
import telnetlib

from python.network_automation.paramiko.exercises.myparamiko import send_from_file


class Device:
    def __init__(self, host, user, password,tn=None):
        self.host = host
        self.user = user
        self.password = password
        self.tn = tn

    def connect(self):
        self.tn = telnetlib.Telnet(self.host)

    def authenticate(self):
        self.tn.read_until(b'Username: ')
        self.tn.write(self.user.encode() + b'\n')
        print('USER READY')

        self.tn.read_until(b'Password: ')
        self.tn.write(self.password.encode() + b'\n')
        print('PASSWORD READY')

    def send(self, command, timeout=0.5):
        print(f'Sending command: {command}')
        self.tn.write(command.encode() + b'\n')
        time.sleep(timeout)

    def show(self):
        output = self.tn.read_all().decode('utf-8')
        return output

    def send_from_list(self, commands_list):
        for command in commands_list:
            self.send(command)

    def send_from_file(self,file):
        with open(file) as f:
            commands = f.read().splitlines()

        self.send_from_list(commands)



if __name__ == '__main__':
    router1 = Device('10.10.10.1', 'gozzki', 'cisco')
    router2 = Device('10.10.10.2', 'gozzki', 'cisco')
    router3 = Device('10.10.10.3', 'gozzki', 'cisco')

    commands = ['enable', 'cisco', 'conf t', 'int lo0', 'ip add 1.1.1.1 255.255.255.255', 'exit', 'router ospf 1',
                'network 0.0.0.0 0.0.0.0 area 0', 'end', 'terminal length 0', 'show ip protocols', 'exit']

    # routers = [router1, router2, router3]
    # for router in routers:
    #     router.connect()
    #     router.authenticate()
    #     router.send('enable')
    #     router.send('cisco')
    #     router.send('conf t')
    #     router.send('int lo0')
    #     router.send('ip address 1.1.1.1 255.255.255.255')
    #     router.send('exit')
    #     router.send('router ospf 1')
    #     router.send('network 0.0.0.0 0.0.0.0 area 0')
    #     router.send('end')
    #     router.send('terminal length')
    #     router.send('sh ip protocols')
    #     router.send('exit')
    #
    #     output = router.show()
    #     print(output)
    router1.connect()
    router1.authenticate()
    router1.send_from_list(commands)
    router1.show()