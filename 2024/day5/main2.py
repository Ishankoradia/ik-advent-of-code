from collections import deque

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


def topological_sort(update: list[str], rules: list[list[str]]) -> list[int]:
    # will store node => [list of node it points to;basically these will come after the node]
    graph: dict[int, list] = {}

    for node in update:
        graph[node] = []

    for edge in rules:
        u, v = edge
        graph[u].append(v)

    # compute the indgree basically no of incoming edges
    indegree = dict()
    for node in update:
        for neighbor in graph[node]:
            indegree[neighbor] = indegree.get(neighbor, 0) + 1

    q = deque()

    for node in update:
        if indegree.get(node, 0) == 0:
            q.append(node)

    ans = []

    while len(q) > 0:
        ele = q.popleft()
        ans.append(ele)
        for neighbor in graph[ele]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return ans


sum_mid_vals = 0
for i in range(len(updates)):
    update = updates[i]

    is_correct = True
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if not check_relative_order(update[i], update[j], rules):
                is_correct = False
                break
        if not is_correct:
            break

    if not is_correct:
        concerned_rules = []
        for rule in rules:
            x, y = rule
            if x in update and y in update:
                concerned_rules.append(rule)

        corrected_arr = topological_sort(update, concerned_rules)

        assert len(corrected_arr) == len(update)

        mid = len(corrected_arr) // 2
        sum_mid_vals += corrected_arr[mid]

print("Sum of mid values: ", sum_mid_vals)
