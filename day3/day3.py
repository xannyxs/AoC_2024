from typing import List, Tuple
from math import prod


def find_last_control(line: str, start: int, end: int) -> bool:
    last_do = line.rfind("do()", start, end)
    last_dont = line.rfind("don't()", start, end)

    if last_do == -1 and last_dont == -1:
        return True

    return last_do > last_dont


def star2(lines: List[str]) -> int:
    totalAmount = 0
    do = True

    for line in lines:
        lastFind = 0
        while line.find("mul(", lastFind) is not -1:

            fchar = line.find("mul(", lastFind)
            schar = line.find(")", fchar)

            last_do = line.rfind("do()", lastFind, fchar)
            last_dont = line.rfind("don't()", lastFind, fchar)

            if last_do is not -1 or last_dont is not -1:
                do = last_do > last_dont

            lastFind = fchar + 1

            try:
                if do:
                    totalAmount += prod(
                        [int(num) for num in line[fchar + 4 : schar].split(",")]
                    )
            except ValueError:
                continue

    return totalAmount


def star1(lines: List[str]) -> int:
    totalAmount = 0
    lastFind = 0

    for line in lines:
        while line.find("mul(", lastFind) is not -1:
            fchar = line.find("mul(", lastFind)
            schar = line.find(")", fchar)
            lastFind = fchar + 1

            try:
                totalAmount += prod(
                    [int(num) for num in line[fchar + 4 : schar].split(",")]
                )
            except ValueError:
                continue

        lastFind = 0

    return totalAmount


def day3(lines: List[str]) -> Tuple[int, int]:
    return star1(lines), star2(lines)
