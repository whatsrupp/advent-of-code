import pytest
import main
import inspect


input_1 = inspect.cleandoc(f'''
  nop +0
  acc +1
  jmp +4
  acc +3
  jmp -3
  acc -99
  acc +1
  jmp -4
  acc +6'''
)


test_data_task_1 = [
  (input_1, 5),
]


@pytest.mark.parametrize('mock_input, expected', test_data_task_1)
def test_task_1(mock_input, expected, mocker):
  mock_open = mocker.mock_open(read_data=mock_input)
  mocker.patch("builtins.open", mock_open)
  result = main.task1()

  assert(result == expected)


input_2 = inspect.cleandoc(f'''
  nop +0
  acc +5
  nop +4
  jmp +0
  '''
)

test_data_task_2 = [
  (input_1, 8),
  (input_2, 5)
]

@pytest.mark.parametrize('mock_input, expected', test_data_task_2)
def test_task_2(mock_input, expected, mocker):
  mock_open = mocker.mock_open(read_data=mock_input)
  mocker.patch("builtins.open", mock_open)
  result = main.task2()

  assert(result == expected)