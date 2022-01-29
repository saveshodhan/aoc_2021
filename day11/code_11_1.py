# AOC 2021 - day 11 #

import math
import sys

from .common_11 import OctoGrid, parse_input


INF = math.inf


def main(data):
    og = OctoGrid(data)
    for step in range(100):
        og.do_step()
    return og.flashes


if __name__ == "__main__":
    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
