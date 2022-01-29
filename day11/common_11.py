# AOC 2021 - day 11 #

from collections import defaultdict
from copy import deepcopy
import math
import sys


INF = math.inf


class Octopus:

    def __init__(self, value, x, y):
        self.value = value
        self.x, self.y = x, y
        self.index = (x, y)

    def __repr__(self):
        return f"{self.x},{self.y},{self.value}"


class OctoGrid:

    def __init__(self, input_data):
        self.input_data = deepcopy(input_data)
        self.grid = defaultdict(lambda: defaultdict(lambda: None))
        self.octos = []
        self.flashes = 0
        self._make_grid()
        self.maxx = len(self.grid)
        self.maxy = len(self.grid[0])

    def __repr__(self):
        print()
        for x in self.grid:
            for y in self.grid[x]:
                print(self.grid[x][y].value, end=" ")
            print()
        return ""

    def _make_grid(self):
        for x, horz in enumerate(self.input_data):
            for y, vert in enumerate(horz):
                octo = Octopus(vert, x, y)
                self.grid[x][y] = octo
                self.octos.append(octo)
            self.grid[x] = dict(self.grid[x])
        self.grid = dict(self.grid)

    def find_adjacents(self, octo):
        x, y = octo.index
        adjacent_indexes = [
            (x-1, y),       # top
            (x+1, y),       # bottom
            (x, y-1),       # left
            (x, y+1),       # right
            (x-1, y-1),     # top-left
            (x-1, y+1),     # top-right
            (x+1, y-1),     # bottom-left
            (x+1, y+1),     # bottom-right
        ]
        return [
            self.grid[ax][ay] for ax, ay in adjacent_indexes if 0 <= ax < self.maxx and 0 <= ay < self.maxy
        ]

    @staticmethod
    def inc_octos(octos):
        for octo in octos:
            octo.value += 1
        return True

    def flash_octo(self, octo):
        octo.value = INF    # setting to INF so that any further increments will not have any effect, and we can later
        # filter out based on INF easily
        self.flashes += 1
        adjacent_octos = self.find_adjacents(octo)
        self.inc_octos(adjacent_octos)

    def reset_octos(self):
        for octo in self.octos:
            if octo.value == INF:
                octo.value = 0

    def is_all_flash(self):
        return not any(octo.value for octo in self.octos)   # all 0's

    def do_step(self):
        """Do the main step here.

        - inc all octos
        - check which ones are candidates to be flashed
        - for each of these
            - set their values to INF to make them immune to further inc's
            - inc flash count
            - get their adjacent octos
            - inc all those adjacent octos
        - check again for candidates to be flashed
        - exit when no more candidates
        """
        self.inc_octos(self.octos)
        full_octos = [octo for octo in self.octos if octo.value >= 10]
        while full_octos:
            for octo in full_octos:
                self.flash_octo(octo)
            full_octos = [octo for octo in self.octos if octo.value >= 10 and octo.value != INF]
            # >= 10 coz a field may get incremented multiple times by its adjacent octos
            # < INF coz, well, otherwise it'll be an infinite loop with just the above condition
        self.reset_octos()


def parse_input(input_file):
    data = []
    for line in open(input_file):
        row = list(map(int, list(line.strip())))
        data.append(row)
    return data
