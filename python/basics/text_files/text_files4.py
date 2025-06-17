#Create a Python function called tail that reads the last n lines of a text file. The function has two arguments: the file name and n (the number of lines to read). This is similar to the Linux `tail` command.

def tail(file, n):
    with open(file) as f:
        content = f.read().splitlines()
        last_line = content[len(content) - n:]
        my_str = "\n".join(last_line)
        return my_str


t = tail("../../media/sample_file.txt", 10)
print(t)
