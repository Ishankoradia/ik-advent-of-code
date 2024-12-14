import re
import operator
from functools import reduce
from dataclasses import dataclass
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display

positions = []
velocities = []
pattern = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        match = pattern.search(line.strip())
        if match:
            p_x = int(match.group(1))
            p_y = int(match.group(2))
            positions.append((p_x, p_y))
            v_x = int(match.group(3))
            v_y = int(match.group(4))
            velocities.append((v_x, v_y))
        else:
            print("No match found")

assert len(positions) == len(velocities)


@dataclass
class Point:
    x: int
    y: int
    label: str = "."
    cnt: int = 0  # cnt of robots


total_robots = len(positions)
r = 103
# r = 7
c = 101
# c = 11
grid: list[list[Point]] = [[Point(x=x, y=y, cnt=0) for y in range(c)] for x in range(r)]


def pretty_print_grid(grid: list[list[Point]]) -> str:
    s = ""
    for row in grid:
        for point in row:
            s += point.label
        s += "\n"

    return s


def move_robots_on_grid(time: int):
    for i in range(total_robots):
        p_x, p_y = positions[i]
        v_x, v_y = velocities[i]

        new_x = (p_x + time * v_x) % c
        new_y = (p_y + time * v_y) % r

        grid[new_y][new_x].cnt += 1
        grid[new_y][new_x].label = "X"

    return grid


# cnt robots in quadrant
def safety_score(grid: list[list[Point]]):
    center = (r // 2, c // 2)
    robots_per_quad = [0, 0, 0, 0]
    for i in range(r):
        for j in range(c):
            if i < center[0] and j < center[1]:
                robots_per_quad[0] += grid[i][j].cnt
            elif i < center[0] and j > center[1]:
                robots_per_quad[1] += grid[i][j].cnt
            elif i > center[0] and j < center[1]:
                robots_per_quad[2] += grid[i][j].cnt
            elif i > center[0] and j > center[1]:
                robots_per_quad[3] += grid[i][j].cnt

    safety_factor = reduce(operator.mul, robots_per_quad, 1)
    return safety_factor


def output_grid_to_file(grid: list[list[Point]]):
    with open("output.txt", "w") as f:
        for row in grid:
            for point in row:
                f.write(point.label)
            f.write("\n")


def is_robot_positions_unique(grid: list[list[Point]]) -> bool:
    for i in range(r):
        for j in range(c):
            if grid[i][j].cnt > 1:
                return False

    return True


def reset_grid(grid: list[list[Point]]):
    for i in range(r):
        for j in range(c):
            grid[i][j].cnt = 0
            grid[i][j].label = "."


def look_at_pattern(time: int):
    move_robots_on_grid(time)
    ans = pretty_print_grid(grid)
    reset_grid(grid)
    return ans


print(look_at_pattern(0))
