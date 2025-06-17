
with open("../../media/american-english.txt") as file:
    content = file.read().splitlines()
    dictionary = {}
    for line in content:
        dictionary[line] = len(line)

    for item in dictionary.items():
        print(f"{item[0]}: {item[1]}")