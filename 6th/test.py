import pytest
import main
import inspect

complicated_mock = inspect.cleandoc(f'''
  abc

  a
  b
  c

  ab
  ac

  a
  a
  a
  a

  b
'''
)
multi_line_mock = inspect.cleandoc(f'''
  abc

  a
  b
  c
'''
)

simple_mock = inspect.cleandoc(f'''
  abc
'''
)

test_data_task_1 = [
  (simple_mock, 3),
  (complicated_mock, 11),
  (multi_line_mock, 6)
]



@pytest.mark.parametrize('mock_file, expected', test_data_task_1)
def test_task_1(mock_file, expected, mocker):
  mock_open = mocker.mock_open(read_data=mock_file)
  mocker.patch("builtins.open", mock_open)
  result = main.task1()
  assert(result == expected)


test_data_task_2 = [
  (simple_mock, 3),
  (complicated_mock, 6),
  (multi_line_mock, 3)
]


@pytest.mark.parametrize('mock_file, expected', test_data_task_2)
def test_task_2(mock_file, expected, mocker):
  mock_open = mocker.mock_open(read_data=mock_file)
  mocker.patch("builtins.open", mock_open)
  result = main.task2()
  assert(result == expected)