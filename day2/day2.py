from functools import total_ordering
from typing import List, Tuple


def is_safe(numbers: List[int]):
    increase = numbers[0] < numbers[1]
    add_number = True

    for num in range(len(numbers) - 1):
        if (
            increase
            and numbers[num] < numbers[num + 1]
            and numbers[num + 1] <= numbers[num] + 3
        ) or (
            not increase
            and numbers[num] > numbers[num + 1]
            and numbers[num + 1] >= numbers[num] - 3
        ):
            continue
        else:
            add_number = False
            break

    return add_number


def star1(lines: List[str]) -> int:
    totalAmount0 = 0

    for line in lines:
        numbers: List[int] = []

        numbers = [int(num) for num in line.split()]
        if is_safe(numbers):
            totalAmount0 += 1

    return totalAmount0


def star2(lines: List[str]) -> int:
    totalAmount = 0

    for line in lines:
        numbers: List[int] = []

        numbers = [int(num) for num in line.split()]

        if is_safe(numbers):
            totalAmount += 1
            continue

        for i in range(len(numbers)):
            if is_safe(numbers[:i] + numbers[i + 1 :]):
                totalAmount += 1
                break

    return totalAmount


def day2(lines: List[str]) -> Tuple[int, int]:
    return star1(lines), star2(lines)
