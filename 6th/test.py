import main
import inspect

def test_main(mocker):

  mock_file = inspect.cleandoc(f'''
    a
    bc
    d

    e
   '''
)

  mocker.patch("builtins.open", return_value = mock_file)
  main.main()