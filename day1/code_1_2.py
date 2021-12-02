# AOC 2021 - day 1 #

import math
import sys


def parse_input(input_file):
    for each in open(input_file):
        yield int(each.strip())


def main(data_gen):
    incs = 0
    prev = math.inf
    first = next(data_gen)
    second = next(data_gen)
    try:
        for third in data_gen:
            current = sum([first, second, third])
            if current > prev:
                incs += 1
            prev = current
            first = second
            second = third
    except StopIteration:   # explicitly expected for second and third vars' yield
        pass
    return incs


if __name__ == "__main__":

    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
