# AOC 2021 - day 4 #

import sys

from common import get_answer, parse_input

def main(data_gen):
    return get_answer(data_gen, last_win=True)


if __name__ == "__main__":

    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
