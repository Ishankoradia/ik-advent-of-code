from dataclasses import dataclass


@dataclass
class Equation:
    ans: int
    nums: list[int]


equations: list[Equation] = []
with open("input.txt") as f:
    for line in f.readlines():
        lhs, rhs = line.strip().split(":")
        ans = int(lhs)
        nums = [int(num) for num in rhs.split()]
        equations.append(Equation(ans=ans, nums=nums))


def compute(
    nums: list[int], target: int, current_val: int = -1, index: int = 0
) -> bool:
    """All combinations of add/mul from left to right to get to the target"""

    if index == len(nums):
        return current_val == target

    # add
    if current_val == -1:
        current_val = 0
    if compute(nums, target, current_val + nums[index], index + 1):
        return True

    # multiply
    if current_val == -1:
        current_val = 1
    if compute(nums, target, current_val * nums[index], index + 1):
        return True

    # concatenate
    if current_val == -1:
        current_val = 0
    if compute(nums, target, int(str(current_val) + str(nums[index])), index + 1):
        return True

    return False


res = 0
for eq in equations:
    if compute(eq.nums, eq.ans):
        res += eq.ans


print("Total calibration val : ", res)
