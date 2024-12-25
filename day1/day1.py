from typing import Tuple, List


def bonus1(l1: List[int], l2: List[int]) -> int:
    totalAmount = 0

    for num in l1:
        totalAmount += num * l2.count(num)

    return totalAmount


def day1(lines: List[str]) -> Tuple[int, int]:
    l1: List[int] = []
    l2: List[int] = []

    for line in lines:
        l1.append(int(line.split()[0]))
        l2.append(int(line.split()[1]))

    l1.sort()
    l2.sort()

    totalAmount0 = 0
    for num in range(len(l1)):
        if l1[num] > l2[num]:
            totalAmount0 += l1[num] - l2[num]
        else:
            totalAmount0 += l2[num] - l1[num]

    totalAmount1 = bonus1(l1, l2)

    return totalAmount0, totalAmount1
