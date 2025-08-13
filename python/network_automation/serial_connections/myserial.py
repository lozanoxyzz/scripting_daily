import serial
import time

def open_console(port='/tmp/ttyS2', boudrate = 9600):
    console =serial.Serial(port=port, baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=8)
    if console.isOpen():
        return console

    else:
        return False

def run_command(console, command, sleep=1):
    print(f'Sending command: {command}')
    console.write(command.encode() + b'\r\n')
    time.sleep(sleep)

def show(console):
    bytes_to_be_read = console.inWaiting()
    if bytes_to_be_read:
        output = console.read(bytes_to_be_read)
        return output.decode()
    else:
        return False


if __name__ == '__main__':
    console = open_console()
    with open('file.txt') as f:
        commands = f.read().splitlines()
        for cmd in commands:
            run_command(console, cmd)
    output = show(console)
    print(output)
