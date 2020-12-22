import pytest
import main
import inspect


input_1 = inspect.cleandoc(
  f'''
    35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576
  '''
)

test_data_task_1 = [
  (input_1, 127),
]


@pytest.mark.parametrize('mock_input, expected', test_data_task_1)
def test_task_1(mock_input, expected, mocker):
  mock_open = mocker.mock_open(read_data=mock_input)
  mocker.patch("builtins.open", mock_open)
  result = main.task1()
  assert(result == expected)


test_data_task_2 = [
  (input_1, 62),
]

@pytest.mark.parametrize('mock_input, expected', test_data_task_2)
def test_task_2(mock_input, expected, mocker):
  mock_open = mocker.mock_open(read_data=mock_input)
  mocker.patch("builtins.open", mock_open)
  result = main.task2()
  assert(result == expected)