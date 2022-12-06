with open("day4_input.txt", "r") as f:
    data = [
        [[int(k) for k in j.split("-")] for j in i.split(",")]
        for i in f.read().splitlines()
    ]


def range_full_overlap(r1, r2):
    return (r1[0] <= r2[0] and r1[1] >= r2[1]) or (r2[0] <= r1[0] and r2[1] >= r1[1])


def range_overlap(r1, r2):
    return max(r1[0], r2[0]) <= min(r1[1], r2[1])


# Part 1
sum([range_full_overlap(*i) for i in data])

# Part 2
sum([range_overlap(*i) for i in data])
