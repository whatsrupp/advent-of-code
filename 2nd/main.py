import re

def task_1():
  valid_password_count = [0] # hacky, you can't edit variables directly in the outer scope! an interesting python quirk
  
  def is_line_valid(first_number, second_number, character, password):
    character_count = len(re.findall(character, password))
    is_valid = first_number <= character_count and character_count <= second_number
    if(is_valid):
      valid_password_count[0] = valid_password_count[0] + 1

  read_lines(is_line_valid)
  return valid_password_count[0]

def task_2():
    valid_password_count = [0]

    def is_line_valid(first_number, second_number, character, password):
      first_char = password[first_number - 1]
      second_char = password[second_number - 1]
      is_first_char_valid =  first_char == character
      is_second_char_valid = second_char == character
      is_valid = is_first_char_valid ^ is_second_char_valid
      if is_valid:
        valid_password_count[0] = valid_password_count[0] + 1

    read_lines(is_line_valid)
    return valid_password_count[0]

def read_lines(on_line_callback):
  inputFile = open('input.txt', 'r')
  lines = inputFile.readlines()
  for line in lines:
      first_number = int(re.search(r'^\d+', line).group(0))
      second_number = int(re.search(r'(?<=-)\d+', line).group(0))
      character = re.search(r'\w(?=\:)', line).group(0)
      password = re.search(r'\w+$', line).group(0)
      on_line_callback(first_number, second_number, character, password)

print(task_1(),task_2())

# Reflection - regex on string splitting is too complicated 
# Didn't know about line.partition - could have been useful here, regex was probably too complex
# Hacky outer scope array manipulation, this is very javascripty, but not possible in python
# Maybe just read whole file in as a list, not really concerned about optimisation here

