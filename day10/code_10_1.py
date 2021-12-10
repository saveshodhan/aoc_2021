# AOC 2021 - day 10 #

from collections import defaultdict
import math
import sys


OPEN_CHARS = ["(", "[", "{", "<"]
CLOSE_CHARS = [")", "]", "}", ">"]
OPEN_CHAR_MAP = dict(zip(OPEN_CHARS, CLOSE_CHARS))
CLOSE_CHAR_MAP = dict(zip(CLOSE_CHARS, OPEN_CHARS))
POINTS = dict(zip(CLOSE_CHARS, [3, 57, 1197, 25137]))

def parse_input(input_file):
    for line in open(input_file):
        yield line.strip()


def get_corrupted_line_score(line):
    stack = []
    for each in line:
        if each in OPEN_CHAR_MAP:
            stack.append(each)
        elif each in CLOSE_CHAR_MAP:
            relative = CLOSE_CHAR_MAP[each]
            if len(stack) > 0 and stack[-1] == relative:
                stack.pop(-1)
            else:
                return POINTS[each]
    return 0


def main(data):
    score = 0
    for line in data:
        score += get_corrupted_line_score(line)
    return score


if __name__ == "__main__":
    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
