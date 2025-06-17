
def wc(file):
    with open(file) as f:
        content = f.read().splitlines()

        lines = len(content)

        words = 0
        for line in content:
            word_separator = line.split()
            words += len(word_separator)

        characters = 0
        for line in content:
            characters += len(list(line))

        return lines, words, characters



lines, words, characters = wc("../../media/sample_file.txt")
print(lines)
print(words)
print(characters)
