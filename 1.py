with open("day1_input.txt", "r") as f:
    data = [list(map(int, i.split("\n"))) for i in f.read().split("\n\n")]

print(max([sum(i) for i in data]))
print(sum(sorted([sum(i) for i in data])[-3:]))
