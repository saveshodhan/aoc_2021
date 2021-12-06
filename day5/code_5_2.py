# AOC 2021 - day 5 #

import sys

from .common_5 import Board, parse_input


MIN_COUNT = 2


def main(data_gen):
    board = Board(diagonal_support = True)
    for point1, point2 in data_gen:
        board.draw(point1, point2)
    return board.check_dangerous_points(MIN_COUNT)


if __name__ == "__main__":

    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
