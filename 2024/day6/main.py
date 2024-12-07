input: list[list[str]] = []
guard_pos = (None, None)
with open("input.txt") as f:
    i = 0
    for line in f.readlines():
        temp = []
        j = 0
        for ch in line.strip():
            temp.append(ch)
            if ch in "^<>v":
                guard_pos = (i, j)
            j += 1
        input.append(temp)
        i += 1

assert guard_pos != (None, None)
r = len(input)
c = len(input[0])


def is_pos_in_map(p: tuple, grid_r: int, grid_c: int) -> bool:
    return p[0] >= 0 and p[0] < grid_r and p[1] >= 0 and p[1] < grid_c


cnt_x = 0
curr_dir = input[guard_pos[0]][guard_pos[1]]
while is_pos_in_map(guard_pos, r, c):
    x, y = guard_pos

    # mark visited if already not
    if input[x][y] != "X":
        cnt_x += 1
        input[x][y] = "X"

    if curr_dir == ">":
        guard_pos = (x, y + 1)
    elif curr_dir == "<":
        guard_pos = (x, y - 1)
    elif curr_dir == "^":
        guard_pos = (x - 1, y)
    elif curr_dir == "v":
        guard_pos = (x + 1, y)

    # handle obstacle
    if is_pos_in_map(guard_pos, r, c) and input[guard_pos[0]][guard_pos[1]] == "#":
        # reset the guard position
        guard_pos = (x, y)

        # change the direction
        if curr_dir == ">":
            curr_dir = "v"
        elif curr_dir == "<":
            curr_dir = "^"
        elif curr_dir == "^":
            curr_dir = ">"
        elif curr_dir == "v":
            curr_dir = "<"

print("Unique positions visited by the guard:", cnt_x)
print("Last position of the guard:", guard_pos)
