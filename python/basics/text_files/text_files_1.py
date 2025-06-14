# Create a new file that contains only unique MAC addresses. Each MAC should be on its own line.

mac_list = []
with open("../../media/macs.txt") as file:
    macs = file.read().split()
    macs = set(macs)
    print(list(macs))

with open("results/unique_mac.txt", "w", newline="") as file:
    for mac in macs:
        file.write(f"{mac}\n")
