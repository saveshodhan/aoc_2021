# AOC 2021 - day 10 #

from collections import defaultdict
import math
import sys


OPEN_CHARS = ["(", "[", "{", "<"]
CLOSE_CHARS = [")", "]", "}", ">"]
OPEN_CHAR_MAP = dict(zip(OPEN_CHARS, CLOSE_CHARS))
CLOSE_CHAR_MAP = dict(zip(CLOSE_CHARS, OPEN_CHARS))
POINTS = dict(zip(CLOSE_CHARS, [1, 2, 3, 4]))

def parse_input(input_file):
    for line in open(input_file):
        yield line.strip()


def get_incorrect_line(line):
    stack = []
    for each in line:
        if each in OPEN_CHAR_MAP:
            stack.append(each)
        elif each in CLOSE_CHAR_MAP:
            relative = CLOSE_CHAR_MAP[each]
            if len(stack) > 0 and stack[-1] == relative:
                stack.pop(-1)
            else:
                return None
    return stack


def get_closing_sequence(stack):
    return reversed([OPEN_CHAR_MAP[x] for x in stack])


def calc_score(closing_sequence):
    score = 0
    for each in closing_sequence:
        score *= 5
        score += POINTS[each]
    return score


def main(data):
    scores = []
    for line in data:
        incorrect_line = get_incorrect_line(line)
        if incorrect_line:
            closing_sequence = get_closing_sequence(incorrect_line)
            score = calc_score(closing_sequence)
            scores.append(score)
    scores.sort()
    return scores[len(scores)//2]


if __name__ == "__main__":
    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
