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


def find_file_location(disk: list[File], fid: int) -> tuple:
    print("finding file location of ", fid)

    end = len(disk) - 1

    while end >= 0 and disk[end].id != fid:
        end -= 1

    start = end
    while start - 1 >= 0 and disk[start - 1].id == fid:
        start -= 1

    return (start, end)


def find_leftmost_empty_space(
    disk: list[File], f_start: int, f_length: int, start: int = 0
) -> tuple:
    """Gets the left most empty space greater than or equal to f_length"""

    while start < len(disk) - 1 and disk[start].id != -1:
        start += 1

    end = start
    while end + 1 < len(disk) and disk[end + 1].id == -1:
        end += 1

    if end >= f_start:
        return None

    if end - start + 1 >= f_length:
        return (start, end)
    else:
        return find_leftmost_empty_space(disk, f_start, f_length, end + 1)


# loop over all file IDs
for f in range(fid - 1, 0, -1):
    f_start, f_end = find_file_location(disk, f)

    f_length = f_end - f_start + 1

    space = find_leftmost_empty_space(disk, f_start, f_length)

    if space:
        s_start, s_end = space

        for i in range(f_length):
            disk[s_start + i].id = disk[f_start + i].id
            disk[f_start + i].id = -1


print(compute_checksum(disk))
