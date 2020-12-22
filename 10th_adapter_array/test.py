import pytest
import main
import inspect


input_1 = inspect.cleandoc(
  f'''
    28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''
)


input_2=inspect.cleandoc(
  f'''
    16
    10
    15
    5
    1
    11
    7
    19
    6
    12
    4'''
)


test_data_task_1 = [
  (input_1, 220),
  (input_2, 35)
]


@pytest.mark.parametrize('mock_input, expected', test_data_task_1)
def test_task_1(mock_input, expected, mocker):
  mock_open = mocker.mock_open(read_data=mock_input)
  mocker.patch("builtins.open", mock_open)
  result = main.task1()
  assert(result == expected)


test_data_task_2 = [
  (input_1, 19208),
  (input_2, 8),
]

@pytest.mark.parametrize('mock_input, expected', test_data_task_2)
def test_task_2(mock_input, expected, mocker):
  mock_open = mocker.mock_open(read_data=mock_input)
  mocker.patch("builtins.open", mock_open)
  result = main.task2()
  assert(result == expected)
