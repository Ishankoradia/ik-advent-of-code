input: list[list[str]] = []
with open("input.txt") as f:
    for line in f.readlines():
        temp = list()
        for ch in line.rstrip():
            temp.append(ch)
        input.append(temp)


def cnt_xmas_in_string(s: list[str]):
    """
    Count the number of XMAS in the string and the reverse of the string
    """
    cnt = 0
    p1 = 0
    while p1 < len(s):
        if s[p1] == "X":
            match = "XMAS"
            p2 = 0
            cont = True
            while p1 < len(s) and p2 < len(match):
                if s[p1] != match[p2]:
                    cont = False
                    break
                p1 += 1
                p2 += 1

            if cont and p2 == len(match):
                cnt += 1
        else:
            p1 += 1

    # reverse the string and run it again
    p1 = 0
    s = s[::-1]
    while p1 < len(s):
        if s[p1] == "X":
            match = "XMAS"
            p2 = 0
            cont = True
            while p1 < len(s) and p2 < len(match):
                if s[p1] != match[p2]:
                    cont = False
                    break
                p1 += 1
                p2 += 1

            if cont and p2 == len(match):
                cnt += 1
        else:
            p1 += 1

    return cnt


r = len(input)
c = len(input[0])

cnt_xmas = 0

# count horizontally
for row in input:
    cnt_xmas += cnt_xmas_in_string(row)

# count vertically
for j in range(c):
    col = []
    for i in range(r):
        col.append(input[i][j])

    cnt_xmas += cnt_xmas_in_string(col)


# count diagonally (including the main diagonal)
# will include all diagonals in the upper half
row = 0
for j in range(c):
    ii = row
    jj = j
    diag = []
    while ii < r and jj < c:
        diag.append(input[ii][jj])
        ii += 1
        jj += 1

    cnt_xmas += cnt_xmas_in_string(diag)
# right to left diagonal
row = 0
for j in range(c - 1, -1, -1):
    ii = row
    jj = j
    diag = []
    while ii < r and jj >= 0:
        diag.append(input[ii][jj])
        ii += 1
        jj -= 1

    cnt_xmas += cnt_xmas_in_string(diag)


# count diagonally (excluding the main diagonal)
# will include all diagonals in the lower half
col = 0
for i in range(1, r):
    ii = i
    jj = col
    diag = []
    while ii < r and jj < c:
        diag.append(input[ii][jj])
        ii += 1
        jj += 1

    cnt_xmas += cnt_xmas_in_string(diag)
# right to left diagonal
col = c - 1
for i in range(1, r):
    ii = i
    jj = col
    diag = []
    while ii < r and jj >= 0:
        diag.append(input[ii][jj])
        ii += 1
        jj -= 1

    cnt_xmas += cnt_xmas_in_string(diag)

print("Total count of XMAS: ", cnt_xmas)
