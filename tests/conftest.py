import pytest

from day1 import code_1_1, code_1_2
from day2 import code_2_1, code_2_2
from day3 import code_3_1, code_3_2
from day4 import code_4_1, code_4_2
from day5 import code_5_1, code_5_2
from day6 import code_6_1, code_6_2
from day7 import code_7_1, code_7_2
from day8 import code_8_1, code_8_2
from day9 import code_9_1, code_9_2
from day10 import code_10_1, code_10_2


TEST_DATA = [
    # [module, day_num, part_num, expected_value, test_name],
    [code_1_1, 1, 1, 7, "code_1_1"],
    [code_1_2, 1, 2, 5, "code_1_2"],
    [code_2_1, 2, 1, 150, "code_2_1"],
    [code_2_2, 2, 2, 900, "code_2_2"],
    [code_3_1, 3, 1, 198, "code_3_1"],
    [code_3_2, 3, 2, 230, "code_3_2"],
    [code_4_1, 4, 1, 4512, "code_4_1"],
    [code_4_2, 4, 2, 1924, "code_4_2"],
    [code_5_1, 5, 1, 5, "code_5_1"],
    [code_5_2, 5, 2, 12, "code_5_2"],
    [code_6_1, 6, 1, 5934, "code_6_1"],
    [code_6_2, 6, 2, 26984457539, "code_6_2"],
    [code_7_1, 7, 1, 37, "code_7_1"],
    [code_7_2, 7, 2, 168, "code_7_2"],
    [code_8_1, 8, 1, 26, "code_8_1"],
    [code_8_2, 8, 2, 61229, "code_8_2"],
    [code_9_1, 9, 1, 15, "code_9_1"],
    [code_9_2, 9, 2, 1134, "code_9_2"],
    [code_10_1, 10, 1, 26397, "code_10_1"],
    [code_10_2, 10, 2, 288957, "code_10_2"],
]


@pytest.fixture(params=TEST_DATA, ids=[i[-1] for i in TEST_DATA])
def do(request):
    yield request.param
