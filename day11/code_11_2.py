# AOC 2021 - day 11 #

import math
import sys

from .common_11 import OctoGrid, parse_input


INF = math.inf


def main(data):
    og = OctoGrid(data)
    step = 1
    while True:
        og.do_step()
        all_flashes = og.is_all_flash()
        if all_flashes:
            break
        step += 1
    return step


if __name__ == "__main__":
    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
