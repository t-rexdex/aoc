import csv
from pprint import pprint as pp

"""The goal of part 1 of day 2 is go through an array and find the largest and smallest numbers then finding the difference
between them, and finally summing those difference values."""


def parse_input_file(file: str) -> list[list[str]]:
    with open(file, encoding="utf-8") as f:
        new_list = []
        for row in csv.reader(f):
            line_str = row[0].split("\t")
            line_int = list(map(int, line_str))
            new_list.append(line_int)

    return new_list


def find_max(lst: list[str]) -> int:
    max_int = 0
    return max_int


if __name__ == "__main__":
    file = "./inputs/day_02.csv"
    parsed_list = parse_input_file(file)

    # pp(len(new_list))
