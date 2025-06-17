
with open("../../media/american-english.txt") as file:
    content = file.read().splitlines()
    dictionary = {}
    for line in content:
        dictionary[line] = len(line)

    view = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    for item in view[:100]:
        print(f"{item[0]}: {item[1]}")