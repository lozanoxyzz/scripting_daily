import string

letters = dict()

# initializing the dictionary with all letters as keys and zero as values
for c in string.ascii_lowercase:
    letters[c] = 0

with open("../../media/american-english.txt") as f:
    content = f.read().splitlines()
    for item in content:
        for char in string.ascii_lowercase:
            letters[char] += item.count(char)

print(letters)