import re

antennas: dict[str, list[list[int]]] = dict()  # stores location of each antenna
input: list[list[str]] = []
pattern = re.compile(r"[a-zA-Z0-9]")
with open("input.txt") as f:
    i = 0
    for line in f.readlines():
        j = 0
        temp = []
        for ch in line.strip():
            temp.append(ch)
            if pattern.match(ch):
                antennas[ch] = antennas.get(ch, [])
                antennas[ch].append([i, j])
            j += 1
        input.append(temp)
        i += 1

r = len(input)
c = len(input[0])


def location_in_map(x: int, y: int) -> bool:
    return 0 <= x and x < r and 0 <= y and y < c


unique_antinode_locs = set()
for antenna, locations in antennas.items():
    for i in range(len(locations)):
        x1, y1 = locations[i]
        for j in range(i + 1, len(locations)):
            x2, y2 = locations[j]
            if x1 == x2 and y1 == y2:  # make sure locations are different
                continue

            # consider (x1, y1) & move away from (x2, y2) in direction of slope
            x_dist = x2 - x1
            y_dist = y2 - y1

            x_new = x1 - x_dist
            y_new = y1 - y_dist

            if location_in_map(x_new, y_new):
                unique_antinode_locs.add((x_new, y_new))

            # consider (x2, y2) & move away from (x1, y1) in direction of slope
            x_dist = x1 - x2
            y_dist = y1 - y2

            x_new = x2 - x_dist
            y_new = y2 - y_dist

            if location_in_map(x_new, y_new):
                unique_antinode_locs.add((x_new, y_new))


def print_map_with_antinodes(
    input: list[list[str]], antinode_locs: set[tuple[int, int]]
):
    with open("output.txt", "w") as f:
        for i in range(r):
            for j in range(c):
                if input[i][j] == "." and (i, j) in antinode_locs:
                    f.write("#")
                else:
                    f.write(input[i][j])
            f.write("\n")


print("Total unique antinode locations : ", len(unique_antinode_locs))
# print(print_map_with_antinodes(input, unique_antinode_locs))
