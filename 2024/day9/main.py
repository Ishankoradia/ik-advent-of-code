from collections import deque
from dataclasses import dataclass

data = ""
with open("input.txt") as file:
    data = file.read()


@dataclass
class File:
    id: int  # -1 represents space
    size: int = 1


disk: list[File] = list()

fid = 0
for i in range(len(data)):
    current_fid = -1
    if i % 2 == 0:
        current_fid = fid
        fid += 1

    size = int(data[i])
    while size > 0:
        disk.append(File(id=current_fid))
        size -= 1


def pretty_print_disk_state(disk: list[File]) -> None:
    for f in disk:
        if f.id == -1:
            print(".", end="")
        else:
            print(f.id, end="")

    print("", end="\n")


def compute_checksum(disk: list[File]) -> int:
    # checksum is the sum of the ids of the files
    checksum = 0
    for i, f in enumerate(disk):
        if f.id != -1:
            checksum += f.id * i

    return checksum


# two pointer approach
p1 = 0
p2 = len(disk) - 1

# idea is p1 will look for empty spaces while p2 will for files
while p1 < p2:

    while disk[p1].id != -1:
        p1 += 1

    while disk[p2].id == -1:
        p2 -= 1

    # move file at p2 to free space at p1
    if p1 < p2:
        disk[p1].id = disk[p2].id
        disk[p2].id = -1


print(compute_checksum(disk))
