import re

with open("day5_input.txt", "r") as f:
    data = f.read()

parsed_stacks, moves = data.split("move", 1)
parsed_stacks = parsed_stacks.splitlines()
parsed_stacks = [
    [stack[i] for i in range(1, len(stack), 4)]
    for stack in parsed_stacks
    if "[" in stack
]
stacks = [[k for k in j if k != " "] for j in list(zip(*parsed_stacks))]
moves = [[int(j) for j in re.findall("[0-9]+", i)] for i in moves.splitlines()]


def apply_moves(stacks, moves, reverse=False):
    for num, from_stack, to_stack in moves:
        to_move = stacks[from_stack - 1][:num]
        if reverse:
            to_move = to_move[::-1]
        stacks[to_stack - 1] = to_move + stacks[to_stack - 1]
        stacks[from_stack - 1] = stacks[from_stack - 1][num:]
    return stacks


# Part 1
"".join([stack[0] for stack in apply_moves(stacks, moves, True)])

# Part 2
"".join([stack[0] for stack in apply_moves(stacks, moves, False)])
