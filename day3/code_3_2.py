# AOC 2021 - day 2 #

from copy import deepcopy
import sys
from collections import defaultdict, Counter




def parse_input(input_file):
    return [x.strip() for x in open(input_file)]


def rec(data, index, common):
    common_bits = {"0": 0, "1": 0}

    for line in data:
        common_bits[line[index]] += 1

    if common_bits["0"] > common_bits["1"]:
        mcb, mcb_val = "0", common_bits["0"]
        lcb, lcb_val = "1", common_bits["1"]
    else:
        mcb, mcb_val = "1", common_bits["1"]
        lcb, lcb_val = "0", common_bits["0"]

    bit, val = (mcb, mcb_val) if common == "most" else (lcb, lcb_val)
    new_data = [x for x in data if x[index] == bit]
    if len(new_data) == 1:
        return new_data[0]
    return rec(new_data, index+1, common)


def main(data_gen):
    oxygen = rec(data_gen, 0, "most")
    co2 = rec(data_gen, 0, "least")

    return int(oxygen, 2) * int(co2, 2)


if __name__ == "__main__":

    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
