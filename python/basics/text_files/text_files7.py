

with open("../../media/banking.txt") as f:
    content = f.read().splitlines()

    D = 0
    W = 0
    for line in content:
        if line[0] == "D":
            D += int("".join(line[2:]))

        elif line[0] == "W":
            W += int("".join(line[2:]))


    output = D - W
    print(output)