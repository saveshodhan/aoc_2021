# AOC 2021 - day 6 #

import sys

from .common_6 import dec_all, init_dict, parse_input


RESET_VAL = 6
NEW_VAL = 8
DAYS = 80


def main(points):
    d = init_dict(points, max(NEW_VAL, RESET_VAL))

    for day in range(DAYS):
        d = dec_all(d, RESET_VAL, NEW_VAL)
    return sum(d.values())

if __name__ == "__main__":

    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
