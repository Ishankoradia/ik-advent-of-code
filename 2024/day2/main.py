import pandas as pd
import numpy as np

reports = []
with open("input.txt") as f:
    for line in f:
        temp = []
        for i, n in enumerate(line.strip().split()):
            temp.append(int(n))
        reports.append(temp)

print("Total number of reports: ", len(reports))


def is_report_safe(levels: list[int], depth=0) -> bool:
    if len(levels) <= 1:
        return True
    else:
        prev = 0
        next = 1
        diff = levels[next] - levels[prev]

        if abs(diff) < 1 or abs(diff) > 3:
            return False

        prev = next
        next = next + 1
        while next < len(levels):
            new_diff = levels[next] - levels[prev]

            if (abs(new_diff) < 1 or abs(new_diff) > 3) or (diff * new_diff < 0):
                return False

            diff = new_diff
            prev = next
            next += 1

        return True


safe_reports = 0
for levels in reports:
    for i in range(len(levels)):
        ## very brute force
        if is_report_safe(levels[:i] + levels[(i + 1) :]):
            safe_reports += 1
            break

print("The number of safe reports is: ", safe_reports)
