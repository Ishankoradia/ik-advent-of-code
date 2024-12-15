map: list[list[str]] = []
moves: str = ""
curr_robot_pos = [None, None]  # initial pos of robot
with open("test_input.txt") as file:
    i = 0
    is_moves = False
    for line in file.readlines():
        if is_moves:
            moves += line.strip()
            continue

        if line.strip() == "":
            is_moves = True
            continue

        map.append([])
        for ch in line.strip():
            if ch == "#":
                map[i].append("#")
                map[i].append("#")
            elif ch == "0" or ch == "O":
                map[i].append("[")
                map[i].append("]")
            elif ch == ".":
                map[i].append(".")
                map[i].append(".")
            elif ch == "@":
                map[i].append("@")
                map[i].append(".")

        i += 1


def next_post(i: int, j: int, step: str, jump: int = 1):
    if step == "^":
        return (i - 1, j)
    elif step == "v":
        return (i + 1, j)
    elif step == "<":
        return (i, j - jump)
    elif step == ">":
        return (i, j + jump)


def move_object_by_a_step(i: int, j: int, step: str) -> bool:
    """All the points in the list will by 1 step in the direction of step"""
    global map

    x_new, y_new = next_post(i, j, step)

    if x_new < 0 or y_new < 0 or x_new >= len(map) or y_new >= len(map[0]):
        return False

    if map[x_new][y_new] == "#":
        return False

    if map[x_new][y_new] == ".":
        return True

    if map[x_new][y_new] in "[]":
        curr_block = []  # find the complete block
        if map[x_new][y_new] == "[" and map[x_new][y_new + 1] == "]":
            x1, y1 = x_new, y_new + 1
            curr_block = [[x_new, y_new], [x1, y1]]
        elif map[x_new][y_new] == "]" and map[x_new][y_new - 1] == "[":
            x1, y1 = x_new, y_new - 1
            curr_block = [[x1, y1], [x_new, y_new]]

        print("Curr block : ", curr_block)

        # figure out the point to check next so that the block can be moved

        if can_move_block():
            for x_b, y_b in curr_block:
                x_b1, y_b1 = next_post(x_b, y_b, step)
                map[x_b1][y_b1] = map[x_b][y_b]
                map[x_b][y_b] = "."

            # move the robot or the current point
            map[x_new][y_new] = map[i][j]
            map[i][j] = "."
            return True

    return False


def find_robot(map: list[list[str]]):
    # can be more optimized
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "@":
                return [i, j]


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


output_map_to_file(map)


def simulate_moves(map, moves: str):
    robot_pos = find_robot(map)
    print("Initial robot state : ", robot_pos)
    print("Moves : ", moves)
    for step in moves:
        move_object_by_a_step(robot_pos[0], robot_pos[1], step)
        robot_pos = find_robot(map)


simulate_moves(map, ["<"])
output_map_to_file(map)
print("Total gps sum : ", sum_gps_coordinate_of_boxes(map))
