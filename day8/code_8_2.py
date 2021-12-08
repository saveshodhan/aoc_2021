# AOC 2021 - day 8 #

from collections import defaultdict
import sys

FINAL_MAPPING = {
    "ONE": {},
    "TWO": {},
    "THREE": {},
    "FOUR": {},
    "FIVE": {},
    "SIX": {},
    "SEVEN": {},
    "EIGHT": {},
    "NINE": {},

    "T": {},    # TOP
    "TL": {},   # TOP LEFT
    "TR": {},   # TOP RIGHT
    "C": {},    # CENTRE
    "BL": {},   # BOTTOM LEFT
    "BR": {},   # BOTTOM RIGHT
    "B": {},    # BOTTOM
}


class SSD:

    def __init__(self, input_data):
        self.COUNT_MAPPING = defaultdict(list)  # similar to that in part1, except that here we store sets
        self.input_data = input_data
        for key in FINAL_MAPPING:
            setattr(self, key, {})
        for each in self.input_data:
            self.COUNT_MAPPING[len(each)].append(set(sorted(each)))
        self.ONE = self.COUNT_MAPPING[2][0]     # this is similar to UNIQUE_LENGHTS in part 1, except here it's set
        self.FOUR = self.COUNT_MAPPING[4][0]
        self.SEVEN = self.COUNT_MAPPING[3][0]
        self.EIGHT = self.COUNT_MAPPING[7][0]

    def make_t(self):
        self.T = self.SEVEN - self.ONE

    def make_b_9(self):
        TL_C = self.FOUR - self.ONE     # TL_C means TL and C
        possible_B = [(x, x - TL_C.union(self.T).union(self.ONE)) for x in self.COUNT_MAPPING[6]]
        self.NINE, self.B = list(filter(lambda x: len(x[1]) == 1, possible_B))[0]
        self.COUNT_MAPPING[6].remove(self.NINE)     # so that the last element in the list can be directly assigned

    def make_bl(self):
        BL_B = self.EIGHT - (self.FOUR.union(self.SEVEN))
        self.BL = BL_B - self.B

    def make_c_3(self):
        possible_C = [(x, x - self.ONE.union(self.T).union(self.B)) for x in self.COUNT_MAPPING[5]]
        self.THREE, self.C = list(filter(lambda x: len(x[1]) == 1, possible_C))[0]
        self.COUNT_MAPPING[5].remove(self.THREE)

    def make_tl(self):
        self.TL = self.FOUR - self.ONE.union(self.C)

    def make_1(self):
        self.ONE = self.EIGHT.intersection(self.SEVEN) - self.T

    def make_0_6(self):
        self.ZERO = [x for x in self.COUNT_MAPPING[6] if not x.intersection(self.C)][0]
        self.SIX = [x for x in self.COUNT_MAPPING[6] if x.intersection(self.C)][0]

    def make_tr_br(self):
        self.BR = self.SIX.intersection(self.ONE)
        self.TR = self.ONE - self.BR

    def make_2_5(self):
        possible_2 = [(x, x.intersection(self.TR)) for x in self.COUNT_MAPPING[5]]
        self.TWO, _ = list(filter(lambda x: len(x[1]) == 1, possible_2))[0]
        self.COUNT_MAPPING[5].remove(self.TWO)
        self.FIVE = self.COUNT_MAPPING[5][0]

    def make_numbers(self):
        self.NUMBERS = {
            tuple(self.ZERO): "0",
            tuple(self.ONE): "1",
            tuple(self.TWO): "2",
            tuple(self.THREE): "3",
            tuple(self.FOUR): "4",
            tuple(self.FIVE): "5",
            tuple(self.SIX): "6",
            tuple(self.SEVEN): "7",
            tuple(self.EIGHT): "8",
            tuple(self.NINE): "9",
        }

    def part2(self):
        self.make_t()
        self.make_b_9()
        self.make_bl()
        self.make_c_3()
        self.make_tl()
        self.make_1()
        self.make_0_6()
        self.make_tr_br()
        self.make_2_5()
        self.make_numbers()

    def get_number(self, output_data):
        o = [tuple(set(sorted(x))) for x in output_data]
        number = [self.NUMBERS[x] for x in o]
        number = "".join(number)
        return int(number)



def parse_input(input_file):
    data_gen = []
    for each_line in open(input_file):
        input_part, output_part = [x.strip().split() for x in each_line.strip().split("|")]
        yield input_part, output_part


def main(data_gen):
    total = 0
    for input_part, output_part in data_gen:
        ssd = SSD(input_part)
        ssd.part2()
        ssd.make_numbers()
        total += ssd.get_number(output_part)
    return total

if __name__ == "__main__":
    data_gen = parse_input(sys.argv[1])
    print(main(data_gen))
