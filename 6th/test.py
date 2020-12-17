import main
import inspect


def test_main(mocker):
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
  mock_open = mocker.mock_open(read_data=simple_mock)
  mocker.patch("builtins.open", mock_open)
  result = main.main()
  expected = 3
  assert(result == expected)

