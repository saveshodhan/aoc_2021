# AOC 2021 - day 7 #


from itertools import accumulate
import statistics
import sys


def parse_input(input_file):
    data = open(input_file).read()
    data_list = data.split(",")
    data_gen = list(map(int, data_list))
    return data_gen


def get_accumulated_value(mean, val):
    iter_range = range(abs(mean - val) + 1)
    for val in accumulate(iter_range):
        continue
    return val  # need the last value from the generator (accumulate returns a generator)


def get_sum_of_distances(mean, l):
    distances = []
    for each in l:
        distances.append(get_accumulated_value(mean, each))
    return sum(distances)


def main(data_gen):
    l = sorted(data_gen)
    max_mean = statistics.math.ceil(statistics.mean(l))
    min_mean = statistics.math.floor(statistics.mean(l))
    return min(get_sum_of_distances(max_mean, l), get_sum_of_distances(min_mean, l))

if __name__ == "__main__":
    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
