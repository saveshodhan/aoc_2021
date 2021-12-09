# AOC 2021 - day 9 #

from collections import defaultdict
import math
import sys



def parse_input(input_file):
    input_list = open(input_file).readlines()
    input_list = [list(x.strip()) for x in input_list]
    input_list = [list(map(int, x)) for x in input_list]
    d = defaultdict(lambda: defaultdict(int))
    for i, iv in enumerate(input_list):
        for j, jv in enumerate(iv):
            d[i][j] = jv
    return dict(d)  # converting to normal dict to avoid wrong keys getting added silently


def get_neighbours(i, j, data):
    # because we need to check the least val, we put INF for places that dont exist
    # that way, we can be sure that actual valeus will always be less than this.
    return [
        data.get(i-1, {}).get(j, math.inf),
        data.get(i+1, {}).get(j, math.inf),
        data.get(i, {}).get(j-1, math.inf),
        data.get(i, {}).get(j+1, math.inf)
    ]


def get_lowest_points(data):
    for i in data:
        for j in data[i]:
            neighbours = get_neighbours(i, j, data)
            if data[i][j] < min(neighbours):
                yield i, j, data[i][j]


def main(data):
    answer = 0
    for lowest_i, lowest_j, value in get_lowest_points(data):
        answer += value + 1
    return answer


if __name__ == "__main__":
    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
