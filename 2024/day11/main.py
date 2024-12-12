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


cnt = 0
for i in range(len(stones)):
    head = Node(-1)
    head.next = Node(stones[i])

    for i in range(25):
        apply_rules(head)

    cnt += get_count_of_nodes(head)

print("Total cnt = ", cnt)
