import re

puzzle: list[dict] = []
bt_pattern = re.compile(r"Button (\w+): X\+(\d+), Y\+(\d+)")
price_pattern = re.compile(r"Prize: X=(\d+), Y=(\d+)")
with open("input.txt") as f:
    lines = f.readlines()

    cnt = 0
    temp = {}
    for line in lines:
        match = bt_pattern.search(line.strip())
        if match:
            button = match.group(1)
            x = int(match.group(2))
            y = int(match.group(3))
            temp[button] = (x, y)

        match = price_pattern.search(line.strip())
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            temp["target"] = (x, y)
            puzzle.append(temp)
            temp = {}


def target_part2(target: tuple[int, int]) -> tuple[int, int]:
    return (target[0] + 10000000000000, target[1] + 10000000000000)


threshold = 100
total_tokens = 0
for p in puzzle:
    xA, yA = p["A"]
    xB, yB = p["B"]
    # X, Y = p["target"]
    X, Y = target_part2(p["target"])

    nA = 0
    if ((X * yB - Y * xB) % (xA * yB - xB * yA) == 0) and (
        (X * yA - Y * xA) % (xB * yA - xA * yB) == 0
    ):
        nA = (X * yB - Y * xB) // (xA * yB - xB * yA)
        nB = (X * yA - Y * xA) // (xB * yA - xA * yB)

        total_tokens += 3 * nA + 1 * nB


print("Tokens used:", total_tokens)
