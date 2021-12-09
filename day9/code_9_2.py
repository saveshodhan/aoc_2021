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
        (i-1, j, data.get(i-1, {}).get(j, math.inf)),
        (i+1, j, data.get(i+1, {}).get(j, math.inf)),
        (i, j-1, data.get(i, {}).get(j-1, math.inf)),
        (i, j+1, data.get(i, {}).get(j+1, math.inf)),
    ]



def get_relevant_neighbourss(neighbours):
    return {
        x for x in neighbours if x[-1] < 9
    }


def get_lowest_points(data):
    for i in data:
        for j in data[i]:
            neighbours = get_neighbours(i, j, data)
            if data[i][j] < min([x[-1] for x in neighbours]):
                yield i, j, data[i][j]


def get_rec(each, data, basin):
    basin.add(each)     # add current elem so that we can exclude it while subtracting below
    relevant_neighbours = get_relevant_neighbourss(get_neighbours(each[0], each[1], data))
    if not relevant_neighbours - basin:
        return basin
    for each_child in relevant_neighbours - basin:
        each_basin = get_rec(each_child, data, basin)
    return basin


def main(data):
    basins = []
    for each in get_lowest_points(data):
        basin = set()
        basin = get_rec(each, data, basin)
        basins.append(basin)
    basins.sort(key=lambda x: len(x), reverse=True)
    return math.prod(len(x) for x in basins[:3])


if __name__ == "__main__":
    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
