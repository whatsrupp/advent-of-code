import re

def main(input_file_name = "input.txt"):
    custom_forms = open(input_file_name, 'r')

    sum_of_yes_answers = 0

    set_of_answered_questions = set()
    for form in custom_forms:
      is_last_form = "\n" not in form
      is_end_of_form_group = bool(re.search('^\n$', form))

      if is_end_of_form_group:
        print(set_of_answered_questions)
        sum_of_yes_answers += len(set_of_answered_questions)
        set_of_answered_questions = set()
        continue

      for char in form.strip():
        set_of_answered_questions.add(char)

      if is_last_form:
        print(set_of_answered_questions)
        sum_of_yes_answers += len(set_of_answered_questions)
    
    return sum_of_yes_answers
  
