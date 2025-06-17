
with open ("../../media/sample_file.txt", "r") as file:
    file_content = file.readlines()
    print(file_content)
    print("".join(file_content))
