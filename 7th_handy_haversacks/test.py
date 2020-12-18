import pytest
import main
import inspect


input_1 = inspect.cleandoc(f'''
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    '''
)

input_2 = inspect.cleandoc(f'''
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    '''
)

input_3 = inspect.cleandoc(f'''
    vibrant plum bags contain no other bags.
    dark olive bags contain no other bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    '''
)

input_4 = inspect.cleandoc(f'''
    dark olive bags contain 1 tasty pink bag.
    silky bronze bags contain 1 shiny gold bag.
    off teal bag contain no other bags.
    tasty pink bags contain 1 shiny gold bag, 2 silky bronze bags.
    shiny gold bags contain 1 off teal bag.
    '''
)

test_data_task_1 = [
  (input_1, 4),
  (input_2, 0),
  (input_3, 0),
  (input_4, 3)
]


@pytest.mark.parametrize('mock_input, expected', test_data_task_1)
def test_task_1(mock_input, expected, mocker):
  mock_open = mocker.mock_open(read_data=mock_input)
  mocker.patch("builtins.open", mock_open)
  result = main.task1()
  assert(result == expected)

input_5 = inspect.cleandoc(f'''
    shiny gold bags contain 2 dark red bags.
    dark red bags contain 2 dark orange bags.
    dark orange bags contain 2 dark yellow bags.
    dark yellow bags contain 2 dark green bags.
    dark green bags contain 2 dark blue bags.
    dark blue bags contain 2 dark violet bags.
    dark violet bags contain no other bags.
    '''
)

test_data_task_2 = [
  (input_1, 32),
  (input_5, 126),
]

@pytest.mark.parametrize('mock_input, expected', test_data_task_2)
def test_task_2(mock_input, expected, mocker):
  mock_open = mocker.mock_open(read_data=mock_input)
  mocker.patch("builtins.open", mock_open)
  result = main.task2()
  assert(result == expected)