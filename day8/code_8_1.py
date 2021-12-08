# AOC 2021 - day 8 #

from collections import defaultdict
import sys


COUNT_MAPPING = {   # mapping between count of segments and which numbers need that count
    2: [1],         # for e.g., the number 1 needs 2 segments
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8],
}


# which numbers use unique count of segments
UNIQUE_LENGHTS = {x for x in COUNT_MAPPING if len(COUNT_MAPPING[x]) == 1}


def parse_input(input_file):
    data_gen = []
    for each_line in open(input_file):
        input_part, output_part = [x.strip().split() for x in each_line.strip().split("|")]
        yield input_part, output_part


def main(data_gen):
    count = 0
    for each in data_gen:
        input_part, output_part = each
        each_data = list(filter(lambda x: len(x) in UNIQUE_LENGHTS, output_part))
        count += len(each_data)
    return count


if __name__ == "__main__":
    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
