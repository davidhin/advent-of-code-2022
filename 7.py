from collections import defaultdict

cmds = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()

with open("day7_input.txt", "r") as f:
    cmds = f.read().splitlines()

dir_sizes = defaultdict(int)
curr_path = []

for cmd in cmds:
    if cmd.startswith("$ cd"):
        to_path = cmd.split()[-1]
        if to_path == "..":
            curr_path.pop(-1)
        else:
            curr_path.append(to_path)
    elif cmd[0].isdigit():
        filesize = int(cmd.split()[0])
        for dir_idx in range(1, len(curr_path) + 1):
            dir_sizes[tuple(curr_path[:dir_idx])] += filesize

# Part 1
sum(i for i in dir_sizes.values() if i <= 100000)

# Part 2
target = max(dir_sizes.values()) - 40000000
min(dir_sizes.values(), key=lambda x: abs(target - x))
