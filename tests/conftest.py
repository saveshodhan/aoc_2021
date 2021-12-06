import pytest

from day1 import code_1_1, code_1_2
from day2 import code_2_1, code_2_2
from day3 import code_3_1, code_3_2
from day4 import code_4_1, code_4_2
from day5 import code_5_1, code_5_2


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
]


@pytest.fixture(params=TEST_DATA, ids=[i[-1] for i in TEST_DATA])
def do(request):
    yield request.param