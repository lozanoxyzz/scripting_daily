

# with open("../../media/devices.txt") as f:
#     content = f.read().splitlines()
#     for row in content:
#         new_row = row.replace(":", " ")
#         new_row = new_row.split()
#         print(new_row)

with open("../../media/devices.txt") as file:
    content = file.read().splitlines()
    my_list = []
    for row in content:
        tmp = row.split(':')
        my_list.append(tmp)

print(my_list)