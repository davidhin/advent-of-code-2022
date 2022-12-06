with open("day3_input.txt", "r") as f:
    data = f.read().splitlines()


def priority_sum(rucksacks):
    diff_letter = set.intersection(*map(set, rucksacks)).pop()
    return ord(diff_letter) - (96 if diff_letter.islower() else 38)


sum(
    [
        priority_sum([rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]])
        for rucksack in data
    ]
)

sum(
    [
        priority_sum(rucksacks)
        for rucksacks in [data[i : i + 3] for i in range(0, len(data), 3)]
    ]
)
