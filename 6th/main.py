import re

def task1(input_file_name = "input.txt"):
    custom_forms = open(input_file_name, 'r')

    sum_of_yes_answers = 0

    set_of_answered_questions = set()
    for form in custom_forms:
      is_last_form = "\n" not in form
      is_end_of_form_group = bool(re.search('^\n$', form))

      if is_end_of_form_group:
        sum_of_yes_answers += len(set_of_answered_questions)
        set_of_answered_questions = set()
        continue

      for char in form.strip():
        set_of_answered_questions.add(char)

      if is_last_form:
        sum_of_yes_answers += len(set_of_answered_questions)
    
    return sum_of_yes_answers
  

def task2(input_file_name = "input.txt"):
    custom_forms = open(input_file_name, 'r')

    sum_of_yes_answers = 0

    answered_questions = {}
    count_passengers = 0

    def count_answers():
      count = 0
      for value in answered_questions.values():
        if count_passengers == value:
          count += 1
      return count


    for form in custom_forms:
      is_last_form = "\n" not in form
      is_end_of_form_group = bool(re.search('^\n$', form))

      if is_end_of_form_group:
        sum_of_yes_answers += count_answers()
        count_passengers = 0
        answered_questions = {}
        continue

      count_passengers += 1

      for char in form.strip():
        if char in answered_questions:
          answered_questions[char] += 1
        else:
          answered_questions[char] = 1

      if is_last_form:
        sum_of_yes_answers += count_answers()
    
    return sum_of_yes_answers