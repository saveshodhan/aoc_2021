# AOC 2021 - day 2 #

import sys
from collections import defaultdict, Counter


common_bits = defaultdict(lambda: {"0": 0, "1": 0})


def parse_input(input_file):
    for each in open(input_file):
        yield each.strip()


def main(data_gen):
    gamma = ""
    epsilon = ""

    for line in data_gen:
        for index, each_bit in enumerate(line):
            common_bits[index][each_bit] += 1

    for k in common_bits:
        counter = Counter(common_bits[k]).most_common()
        gamma += counter[0][0]
        epsilon += counter[1][0]

    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":

    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
