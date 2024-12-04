input: list[list[str]] = []
with open("input.txt") as f:
    for line in f.readlines():
        temp = list()
        for ch in line.rstrip():
            temp.append(ch)
        input.append(temp)


def cnt_xmax_block_3_by_3(
    input: list[list[str]], upper_left: list[int, int], lower_right: list[int, int]
) -> bool:
    x_upper_left, y_upper_left = upper_left
    x_lower_right, y_lower_right = lower_right
    corners = [
        input[x_upper_left][y_upper_left],
        input[x_upper_left][y_lower_right],
        input[x_lower_right][y_upper_left],
        input[x_lower_right][y_lower_right],
    ]

    center = input[x_upper_left + 1][y_upper_left + 1]

    cnt_M = 0
    cnt_S = 0
    for ch in corners:
        if ch == "M":
            cnt_M += 1
        elif ch == "S":
            cnt_S += 1

    # check if the corners are all M or S
    if not (cnt_M == cnt_S and cnt_M == 2):
        return False

    if center != "A":
        return False

    # opposite corners should have the diff characters
    if corners[0] == corners[3]:
        return False

    return True


r = len(input)
c = len(input[0])
total_cnt = 0

for i in range(r):
    for j in range(c):
        upper_left = [i, j]

        if i + 2 < r and j + 2 < c:
            lower_right = [i + 2, j + 2]
            if cnt_xmax_block_3_by_3(input, upper_left, lower_right):
                total_cnt += 1


print("The total count is: ", total_cnt)
