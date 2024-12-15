map: list[list[str]] = []
moves: str = ""
curr_robot_pos = [None, None]  # initial pos of robot
with open("input.txt") as file:
    i = 0
    is_moves = False
    for line in file.readlines():
        if is_moves:
            moves += line.strip()
            continue

        if line.strip() == "":
            is_moves = True
            continue

        j = 0
        map.append([])
        for ch in line.strip():
            map[i].append(ch)

            if ch == "@":
                curr_robot_pos = [i, j]

            j += 1

        i += 1


def next_post(i: int, j: int, step: str):
    if step == "^":
        return (i - 1, j)
    elif step == "v":
        return (i + 1, j)
    elif step == "<":
        return (i, j - 1)
    elif step == ">":
        return (i, j + 1)


def move_object_by_a_step(i: int, j: int, step: str) -> bool:
    global map

    x, y = next_post(i, j, step)

    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return False

    if map[x][y] == "#":
        return False

    if map[x][y] == ".":
        map[x][y] = map[i][j]
        map[i][j] = "."
        return True

    if map[x][y] == "O":
        if move_object_by_a_step(x, y, step):
            map[x][y] = map[i][j]
            map[i][j] = "."
            return True

    return False


def find_robot(map: list[list[str]]):
    # can be more optimized
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "@":
                return (i, j)


def sum_gps_coordinate_of_boxes(map: list[list[str]]):
    """0 is a box"""
    sum = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "O":
                sum += 100 * i + j
    return sum


def output_map_to_file(map: list[list[str]]):
    with open("output.txt", "w") as file:
        for row in map:
            file.write("".join(row) + "\n")


def simulate_moves(start: list[int], moves: str):
    robot_pos = start
    for step in moves:
        move_object_by_a_step(robot_pos[0], robot_pos[1], step)
        robot_pos = find_robot(map)


simulate_moves(curr_robot_pos, moves)
print("Total gps sum : ", sum_gps_coordinate_of_boxes(map))
