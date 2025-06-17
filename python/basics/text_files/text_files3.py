
with open("../../media/file.txt", "r") as file:
    content = file.read().split()

with open("results/file_without_blanks.txt", "w") as file:
    file.write("\n".join(content))

