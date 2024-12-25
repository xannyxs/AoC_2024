from typing import Tuple
from day1.day1 import day1
from day2.day2 import day2
from day3.day3 import day3
from utils.read_file import read_file

# from day4.day4 import day4
# from day5.day5 import day5


def print_solution(day: str, solution: Tuple[int, int]) -> None:
    print(day)
    print("Solution 1:", solution[0])
    print("Solution 2:", solution[1])
    print("\n")


if __name__ == "__main__":
    lines = read_file("day1/input.txt")
    print_solution("Day 1:", day1(lines))

    lines = read_file("day2/input.txt")
    print_solution("Day 2:", day2(lines))

    lines = read_file("day3/input.txt")
    print_solution("Day 3:", day3(lines))

    # lines = read_file("day4/input.txt")
    # print_solution("Day 4:", day4(lines))
    #
    # lines = read_file("day5/input.txt")
    # print_solution("Day 5:", day5(lines))
