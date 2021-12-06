import os


def test_day(do):
    module, day_num, part_num, expected_value, test_name = do
    input_dir = os.path.dirname(module.__file__)
    input_file = f"{input_dir}/input_{day_num}.txt"
    # func = getattr(module, f"code_{day_num}_{part_num}")
    func = module
    input_data = func.parse_input(input_file)
    assert func.main(input_data) == expected_value
