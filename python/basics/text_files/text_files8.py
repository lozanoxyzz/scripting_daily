
def file_comparator(file1, file2):

    with open(file1, 'r') as f1:
        content1 = f1.read().splitlines()

    with open(file2, 'r') as f2:
        content2 = f2.read().splitlines()

    file = list(zip(content1, content2))
    i = 0
    for item in file:
        i += 1
        if item[0] != item[1]:
            print(f'file1 ({i}): {item[0]}, file2 ({i}): {item[1]}')