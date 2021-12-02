# AOC 2021 - day 1 #

import sys

def parse_input(input_file):
    for each in open(input_file):
        yield int(each.strip())


def main(data_gen):
    incs = 0
    prev = next(data_gen)
    for each in data_gen:
        if each > prev:
            incs += 1
        prev = each
    return incs


if __name__ == "__main__":

    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
