topological_map: list[list[int]] = []
trail_heads: list[list[int]] = []
with open("input.txt") as f:
    i = 0
    for line in f.readlines():
        j = 0
        temp = []
        for ch in line.strip():
            temp.append(int(ch))
            if int(ch) == 0:
                trail_heads.append([i, j])
            j += 1
        i += 1

        topological_map.append(temp)

global r, c
r = len(topological_map)
c = len(topological_map[0])


def score_of_trail(
    map: list[list[int]],
    x: int,
    y: int,
    reachable_nines: set,
    curr_height: int = 0,
) -> None:
    if x < 0 or x >= r or y < 0 or y >= c:
        return

    if curr_height != map[x][y]:
        return

    if curr_height == 9:
        if (x, y) not in reachable_nines:
            reachable_nines.add((x, y))

    score_of_trail(map, x + 1, y, reachable_nines, curr_height + 1)  # right
    score_of_trail(map, x - 1, y, reachable_nines, curr_height + 1)  # left
    score_of_trail(map, x, y + 1, reachable_nines, curr_height + 1)  # up
    score_of_trail(map, x, y - 1, reachable_nines, curr_height + 1)  # down


score = 0
for x, y in trail_heads:
    reachable_nines = set()
    score_of_trail(topological_map, x, y, reachable_nines, curr_height=0)
    score += len(reachable_nines)


print(score)
