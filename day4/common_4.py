# AOC 2021 - day 4 #

from dataclasses import dataclass
from itertools import groupby


LENGTH = 5


@dataclass
class Pos:
    """This stores the horz and vert position of an element."""

    h: int
    v: int


@dataclass
class El:
    """This stores each element with different attributes.

    pos is an instance of Pos
    is_marked is to mark if an element is found in Bingo. This will be used to figure out
    if a row (horz or vert) is done.
    """

    val: str
    pos: Pos
    is_marked: bool = False


class Board:
    """The main class that holds an entire board.

    This holds elements in a dict format so that we can directly access them. And we need
    to check both horizontally and vertically both, coz of which we groupby accordingly.
    Groupby directly gives us sorted based on `pos` - this is why we had Pos, so that we
    can sort using this attribute (viz, el.pos.h).
    To check if the board wins, we just need to check the `is_marked` attribute of each
    element.
    """
    def __init__(self, elements, length):
        self.elements = self.form_elements(elements, length)
        self.length = length

    @staticmethod
    def form_elements(elements, length):
        el_elements = {}
        for index, element in enumerate(elements):
            el = El(val=element, pos=Pos(*divmod(index, length)))
            el_elements[element] = el
        return el_elements

    def group_elements(self, key):
        return groupby(sorted(self.elements.values(), key=key), key=key)

    @property
    def horz_board(self):
        horz_board = []
        for idx, g in self.group_elements(lambda x: x.pos.h):
            horz_board.append(list(g))
        return horz_board

    @property
    def vert_board(self):
        vert_board = []
        for idx, g in self.group_elements(lambda x: x.pos.v):
            vert_board.append(list(g))
        return vert_board

    def check_if_win(self, way):
        if way == "horz":
            for row in self.horz_board:
                if all(x.is_marked for x in row):
                    return row
        elif way == "vert":
            for row in self.vert_board:
                if all(x.is_marked for x in row):
                    return row
        return False

    def get_unmarked_sum(self):
        return sum(int(x.val) for x in self.elements.values() if not x.is_marked)


def parse_input(input_file):
    f_data = open(input_file)
    input_data = next(f_data).strip().split(",")
    _ = next(f_data)    # drop new line
    yield input_data
    board = []
    for each in f_data:
        if not each.strip():    # new line means end of board
            yield board
            board = []
        board += each.strip().split()
    yield board


def check_board(input_data, board_data):
    """Check when does a board wins.

    Returns the index of the input element and the board when the board wins. This index
    actually decides how quickly the board wins.
    """
    board = Board(board_data, LENGTH)
    for index, each in enumerate(input_data):
        if each not in board.elements:
            continue
        board.elements[each].is_marked = True
        if board.check_if_win("horz") or board.check_if_win("vert"):
            return index, board
    return False


def get_answer(data_gen, last_win=False):
    """Get the answer for the question.

    Here, we check how quickly each board wins. Depending on the index of the input
    element, we know if a board wins quickly or not. So, when 4.2 said to get the board
    that wins the last, we accepted this `last_win` boolean flag. So, for 4.2, where you
    need the last winner, just pass it `True` which will reverse the sorting and give you
    the last winner on the 0th index.
    """
    boards = []
    input_data = next(data_gen)
    for board_data in data_gen:
        boards.append(check_board(input_data, board_data))
    boards.sort(key=lambda x: int(x[0]), reverse=last_win)
    index, best_board_row = boards[0]
    last_elements = int(input_data[index])
    unmarked_sum = best_board_row.get_unmarked_sum()
    return unmarked_sum * last_elements
