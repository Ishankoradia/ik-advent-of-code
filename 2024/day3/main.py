import re

with open("input.txt") as f:
    input = f.read()

# Define the patterns
do_pattern = re.compile(r"do\(\)")
dont_pattern = re.compile(r"don't\(\)")
mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")

sum1 = 0
p1 = 0
pairs = []
enable = True
while p1 < len(input):
    # print("here", p1)
    if input[p1] == "d":
        do_match = do_pattern.match(input, p1, p1 + 5)  # do() => 4 characters
        if do_match:
            enable = True
            p1 += len(do_match.group(0))
            continue

        dont_match = dont_pattern.match(input, p1, p1 + 8)  # don't() => 7 characters
        if dont_match:
            enable = False
            p1 += len(dont_match.group(0))
            continue

    if enable and input[p1] == "m":
        mul_match = mul_pattern.match(
            input, p1, p1 + 13
        )  # mul(XXX,YYY) => max 12 characters
        if mul_match:
            num1, num2 = int(mul_match.group(1)), int(mul_match.group(2))
            pairs.append([num1, num2])
            p1 += len(mul_match.group(0))
            continue

    p1 += 1

for pair in pairs:
    sum1 += pair[0] * pair[1]

print("The sum is: ", sum1)
