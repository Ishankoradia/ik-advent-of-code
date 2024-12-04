with open("input.txt") as f:
    input = f.read()

# input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
# """
p1 = 0
pairs: list[list[int, int]] = []
enable = True
while p1 < len(input):
    if input[p1] == "d":
        match_do = "do()"
        match_dont = "don't()"

        temp = p1
        p2 = 0
        is_match = True
        while p1 < len(input) and p2 < len(match_do):
            if input[p1] != match_do[p2]:
                is_match = False
                break
            p1 += 1
            p2 += 1

        if is_match and p2 == len(match_do):
            enable = True
        else:
            p2 = 0
            p1 = temp
            is_match = True
            while p1 < len(input) and p2 < len(match_dont):
                if input[p1] != match_dont[p2]:
                    is_match = False
                    break
                p1 += 1
                p2 += 1

            if is_match and p2 == len(match_dont):
                enable = False

    if enable and input[p1] == "m":
        match = "mul("
        p2 = 0

        cont = True
        while p1 < len(input) and p2 < len(match):
            if input[p1] != match[p2]:
                cont = False
                break
            p1 += 1
            p2 += 1

        # maybe we have number pairs available
        num1 = ""
        if cont:
            match = "0123456789"
            while p1 < len(input) and input[p1] in match:
                num1 += input[p1]
                p1 += 1

            if len(num1) > 0:
                cont = True
            else:
                cont = False

        # check for ,
        if cont:
            if p1 < len(input) and input[p1] == ",":
                cont = True
                p1 += 1
            else:
                cont = False

        num2 = ""
        if cont:
            match = "0123456789"
            while p1 < len(input) and input[p1] in match:
                num2 += input[p1]
                p1 += 1

            if len(num2) > 0:
                cont = True
            else:
                cont = False

        if cont:
            if p1 < len(input) and input[p1] == ")":
                cont = True
                p1 += 1
            else:
                cont = False

        if cont and len(num1) > 0 and len(num2) > 0:
            pairs.append([int(num1), int(num2)])
    else:
        p1 += 1

sum1 = 0
print(pairs)
for pair in pairs:
    sum1 += pair[0] * pair[1]


print("The sum is: ", sum1)
