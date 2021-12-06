# AOC 2021 - day 5 #

from collections import defaultdict
from dataclasses import dataclass
import re


RE_PATTERN = "(\d+),(\d+)\s+->\s+(\d+),(\d+)"


def parse_input(input_file):
    f_data = open(input_file)
    for each in open(input_file):
        x1, y1, x2, y2 = re.match(RE_PATTERN, each.strip()).groups()
        point1 = Point(int(x1), int(y1))
        point2 = Point(int(x2), int(y2))
        yield point1, point2


@dataclass
class Point:
    """This stores the position of an element.

    x and y are the axes.
    """

    x: int
    y: int


class Board:

    def __init__(self, diagonal_support = False):
        self.board = defaultdict(lambda: defaultdict(int))     # board[x][y] == o
        self.diagonal_support = diagonal_support

    @staticmethod
    def check_if_straight(point1, point2):
        if point1.x == point2.x:
            return "y"
        elif point1.y == point2.y:
            return "x"
        return False

    @staticmethod
    def check_if_diagonal(point1, point2):
        if abs(point1.x - point2.x) == abs(point1.y - point2.y):
            return True
        return False

    def draw_straight_line(self, axis, point1, point2):
        if axis == "x":
            min_var, max_var = sorted([point1.x, point2.x])
            range_x = range(min_var, max_var+1)
            range_y = [point1.y] * len(range_x)
        elif axis == "y":
            min_var, max_var = sorted([point1.y, point2.y])
            range_y = range(min_var, max_var+1)
            range_x = [point1.x] * len(range_y)
        return range_x, range_y

    def draw_diagonal_line(self, point1, point2):
        if point1.x < point2.x:
            range_x = range(point1.x, point2.x+1, 1)
        else:
            range_x = range(point1.x, point2.x-1, -1)

        if point1.y < point2.y:
            range_y = range(point1.y, point2.y+1, 1)
        else:
            range_y = range(point1.y, point2.y-1, -1)
        return list(range_x), list(range_y)     # we want to iterate on specific elements and not all in the range

    def draw_line(self, range_x, range_y):
        for i, j in zip(range_x, range_y):
            self.board[i][j] += 1

    def draw(self, point1, point2):
        if point1 == point2:
            self.board[i][j] += 1
            return True

        if axis := self.check_if_straight(point1, point2):
            range_x, range_y = self.draw_straight_line(axis, point1, point2)
        elif self.diagonal_support and self.check_if_diagonal(point1, point2):
            range_x, range_y = self.draw_diagonal_line(point1, point2)
        else:
            return False
        self.draw_line(range_x, range_y)

        return True

    def check_dangerous_points(self, min_count):
        count = 0
        for x in self.board:
            for y in self.board[x]:
                if self.board[x][y] >= min_count:
                    count += 1
        return count


