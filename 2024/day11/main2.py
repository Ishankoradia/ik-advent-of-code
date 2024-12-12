from collections import deque

stones = []
with open("input.txt") as f:
    stones = [int(s) for s in f.read().strip().split()]


class Node:
    def __init__(self, val: int = 0, next: "Node" = None):
        self.val = val
        self.next = next


def get_count_of_nodes(head: Node) -> int:
    """Prints the linked list by iterating from its head"""
    temp = head.next
    if temp is None:
        print("List is empty")

    cnt = 0
    while temp != None:
        cnt += 1
        temp = temp.next

    return cnt


def pretty_print_ll(head: Node) -> int:
    temp = head.next
    if temp is None:
        print("List is empty")

    while temp != None:
        print(temp.val, end=" -> ")
        temp = temp.next

    return cnt


def count_digits(num: int) -> int:
    count = 0

    while num != 0:
        num //= 10
        count += 1

    return count


def split_num_into_two(num: int) -> tuple[int, int]:
    num_digits = count_digits(num)
    mid = num_digits // 2
    divisor = 10**mid
    left_half = num // divisor
    right_half = num % divisor
    return left_half, right_half


def apply_rules(head: Node) -> None:
    prev = head
    curr = head.next
    while curr != None:
        if curr.val == 0:
            curr.val = 1
        elif count_digits(curr.val) % 2 == 0:
            left_half, right_half = split_num_into_two(curr.val)

            left_node = Node(left_half)
            right_node = Node(right_half)

            # split current node into two
            right_node.next = curr.next
            curr.next = None
            prev.next = left_node

            left_node.next = right_node

            curr = right_node
            prev = left_node
        else:
            curr.val = curr.val * 2024

        prev = curr
        curr = curr.next


def count_recursively(num: int, k: int, i: int = 0, cnt: int = 1):
    if i == k:
        return cnt

    if num == 0:
        return count_recursively(1, k, i + 1, cnt)
    elif count_digits(num) % 2 == 0:
        left, right = split_num_into_two(num)
        return count_recursively(left, k, i + 1, cnt) + count_recursively(
            right, k, i + 1, cnt
        )
    else:
        return count_recursively(num * 2024, k, i + 1, cnt)


def iterative_count(num: int, k: int):
    q = deque()
    q.append(num)

    for _ in range(k):
        size = len(q)
        print("Current size , ", size)
        for _ in range(size):
            num = q.popleft()

            if num == 0:
                q.append(1)
            elif count_digits(num) % 2 == 0:
                left, right = split_num_into_two(num)
                q.append(left)
                q.append(right)
            else:
                q.append(num * 2024)

    return len(q)


cnt = 0
n = 25
for i in range(len(stones)):
    print("i = ", i)
    head = Node(-1)
    head.next = Node(stones[i])

    for i in range(n):
        apply_rules(head)

    cnt += get_count_of_nodes(head)

    pretty_print_ll(head)

    # cnt += count_recursively(stones[i], n)

    # cnt += iterative_count(stones[i], n)


print("Total cnt = ", cnt)
