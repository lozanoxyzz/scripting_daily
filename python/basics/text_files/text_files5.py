import time


def tail(file, n):
    while True:
        with open(file) as f:
            content = f.read().splitlines()
            last_line = content[len(content) - n:]
            my_str = "\n".join(last_line)
            return my_str

while True:
    t = tail("../../media/sample_file.txt", 10)
    print(t)
    time.sleep(3)
