# AOC 2021 - day 2 #

import sys


FORWARD = "forward"
DOWN = "down"
UP = "up"


def parse_input(input_file):
    for each in open(input_file):
        yield each.strip()


def main(data_gen):
    forward = 0
    down = 0
    aim = 0

    for each in data_gen:
        direction, value = each.split()
        value = int(value)
        if direction == FORWARD:
            forward += value
            down += aim * value
        elif direction == DOWN:
            aim += value
        elif direction == UP:
            aim -= value

    return forward * down


if __name__ == "__main__":

    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
