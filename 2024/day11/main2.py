from collections import deque

stones = []
with open("input.txt") as f:
    stones = [int(s) for s in f.read().strip().split()]


class Node:
    def __init__(
        self, val: int = 0, next: "Node" = None, prev: "Node" = None, cnt: int = 1
    ):
        self.val = val
        self.cnt = cnt
        self.next = next
        self.prev = prev


def get_count_of_nodes(head: Node) -> int:
    """Prints the linked list by iterating from its head"""
    temp = head.next
    if temp is None:
        print("List is empty")

    cnt = 0
    while temp != None:
        cnt += temp.cnt
        temp = temp.next

    return cnt


def pretty_print_ll(head: Node) -> None:
    temp = head.next
    if temp is None:
        print("List is empty")

    while temp != None:
        print(f"{temp.val} (cnt={temp.cnt})", end=" -> ")
        temp = temp.next


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

            # split current node into two
            left_node = Node(left_half, cnt=curr.cnt)

            curr.val = right_half

            prev.next = left_node
            left_node.prev = prev
            left_node.next = curr

            curr.prev = left_node

            prev = left_node
        else:
            curr.val = curr.val * 2024

        prev = curr
        curr = curr.next


def merge_nodes(head: Node) -> None:
    """Merge nodes with same values and increases the count of merged node"""
    prev = head.next
    while prev != None:
        curr = prev.next
        while curr != None:
            # merge this with prev and de-link this from ll
            if curr.val == prev.val:
                prev.cnt += curr.cnt

                curr_prev = curr.prev
                curr_next = curr.next

                curr_prev.next = curr_next
                if curr_next is not None:
                    curr_next.prev = curr_prev

                curr = curr_next
            else:
                curr = curr.next

        prev = prev.next


def generate_ll_from_list(lst: list[int]) -> Node:
    head = Node(-1)
    temp = head
    for val in lst:
        new_nn = Node(val)
        temp.next = new_nn
        new_nn.prev = temp
        temp = temp.next

    return head


head = generate_ll_from_list(stones)
n = 75
for i in range(n):
    apply_rules(head)
    merge_nodes(head)
print("Count of stones = ", get_count_of_nodes(head))
