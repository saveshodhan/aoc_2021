# AOC 2021 - day 7 #

import sys


def parse_input(input_file):
    data = open(input_file).read()
    data_list = data.split(",")
    data_gen = list(map(int, data_list))
    return data_gen


def main(data_gen):
    l = sorted(data_gen)
    median_index = int((len(l) / 2) - 1)
    median_value = l[median_index]
    distances = []
    for each in l:
        distances.append(abs(each - median_value))
    return sum(distances)   # one-liner: sum(list(map(lambda x: abs(x-median_value), l)))


if __name__ == "__main__":
    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
