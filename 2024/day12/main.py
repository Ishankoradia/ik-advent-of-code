map: list[list[int]] = []
with open("input.txt") as f:
    i = 0
    for line in f.readlines():
        j = 0
        temp = []
        for ch in line.strip():
            temp.append(ch)
            j += 1
        map.append(temp)
        i += 1

r = len(map)
c = len(map[0])

visited = [[-1 for _ in range(c)] for _ in range(r)]


def calc_perimeter(i: int, j: int):
    neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

    p = 0
    for x, y in neighbors:
        if x < 0 or x >= r or y < 0 or y >= c:
            p += 1
            continue

        if map[x][y] != map[i][j]:
            p += 1

    return p


def coor_in_map(i: int, j: int):
    return i >= 0 and i < r and j >= 0 and j < c


def calc_perimeter_2(region_no: int):
    """Loop through visited region to figure this out"""
    global visited, r, c

    corners = 0
    for i in range(r):
        for j in range(c):
            if visited[i][j] == region_no:
                NW, W, SW, N, S, NE, E, SE = [
                    coor_in_map(i + x, j + y) and visited[i + x][j + y] == visited[i][j]
                    for x in range(-1, 2)
                    for y in range(-1, 2)
                    if x or y
                ]
                corners += sum(
                    [
                        N and W and not NW,
                        N and E and not NE,
                        S and W and not SW,
                        S and E and not SE,
                        not (N or W),
                        not (N or E),
                        not (S or W),
                        not (S or E),
                    ]
                )

    return corners


def compute_area_and_perimeter_part1(
    i: int,
    j: int,
    letter: str,
) -> None:
    global r, c, visited, map, area, perimeter
    if not coor_in_map(i, j):
        return

    if map[i][j] != letter:
        return

    if visited[i][j]:
        return

    visited[i][j] = True
    area += 1
    perimeter += calc_perimeter(i, j)

    compute_area_and_perimeter_part1(i + 1, j, letter)
    compute_area_and_perimeter_part1(i - 1, j, letter)
    compute_area_and_perimeter_part1(i, j + 1, letter)
    compute_area_and_perimeter_part1(i, j - 1, letter)

    return


def compute_area_and_mark_region_part2(
    i: int, j: int, letter: str, region_no: str
) -> None:
    global r, c, visited, map, area
    if i < 0 or i >= r or j < 0 or j >= c:
        return

    if map[i][j] != letter:
        return

    if visited[i][j] == region_no:
        return

    visited[i][j] = region_no
    area += 1

    compute_area_and_mark_region_part2(i + 1, j, letter, region_no)
    compute_area_and_mark_region_part2(i - 1, j, letter, region_no)
    compute_area_and_mark_region_part2(i, j + 1, letter, region_no)
    compute_area_and_mark_region_part2(i, j - 1, letter, region_no)

    return


total_cost = 0
region_no = 0
for i in range(r):
    for j in range(c):
        if visited[i][j] == -1:
            global area
            area = 0
            compute_area_and_mark_region_part2(i, j, map[i][j], region_no)
            perimeter = calc_perimeter_2(region_no)
            total_cost += area * perimeter
            region_no += 1

print("Total cost = ", total_cost)
