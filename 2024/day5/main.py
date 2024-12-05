rules: list[list[str]] = []
updates: list[list[str]] = []
with open("input.txt") as f:
    input_break = False
    for line in f.readlines():
        if line.strip() == "":
            input_break = True
            continue

        if input_break:  # updates
            updates.append([int(num) for num in line.strip().split(",")])
        else:  # rules
            rules.append([int(num) for num in line.strip().split("|")])


def check_relative_order(x: int, y: int, rules: list[list[str]]) -> bool:
    """
    Checks if x comes before y in the rules
    If any of the rules are violated, return False
    """
    for rule in rules:
        if x in rule and y in rule:
            return rule.index(x) < rule.index(y)


sum_correct_mid_vals = 0
for update in updates:
    is_correct = True
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if not check_relative_order(update[i], update[j], rules):
                is_correct = False
                break
        if not is_correct:
            break

    if is_correct:
        mid = len(update) // 2
        sum_correct_mid_vals += update[mid]

print("Sum of correct mid values: ", sum_correct_mid_vals)
