import re

def validate_field(k, v):
  if k == "byr":
    return int(v) and len(v) == 4 and 1920 <= int(v) and int(v) <= 2002
  elif k == "iyr":
    return int(v) and len(v) == 4 and 2010 <= int(v) and int(v) <= 2020
  elif k == "eyr":
    return int(v) and len(v) == 4 and 2020 <= int(v) and int(v) <= 2030
  elif k == "hgt":
    number = int(re.search('\d+',v).group())
    if bool(re.search('^\d+cm$', v)):
      return 150 <= number and number <= 193
    elif bool(re.search('^\d+in$', v)):
      return 59 <= number and number <= 76
    else:
      return False
  elif k == "hcl":
    return bool(re.search('^#[a-f0-9]{6}$', v))
  elif k == "ecl":
    return bool(re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', v))
  elif k == "pid":
    return bool(re.search('^[0-9]{9}$', v))
  elif k == "cid":
    return True
  else:
    return False

def is_passport_valid(passport):
  is_valid = True
  for key, value in passport.items():
    is_valid = validate_field(key, value)
    print(key, value, is_valid)
    if not is_valid:
      return False 
  return is_valid

def check_passport_batch(input_file_name = "input.txt"):
  input_file = open(input_file_name, 'r')

  current_passport = {}
  valid_passport_count = 0

  i = 0
  for line in input_file:
    i += 1
    is_last_line = "\n" not in line
    is_break_line = bool(re.search('^\n$', line))

    if is_break_line:
      if is_passport_valid(current_passport):
        valid_passport_count += 1
      current_passport = {}
      print('')
      continue

    line = line.replace("\n", "")
    fields = line.split(" ")
    for field in fields:
      key = field[0:3]
      value = field[4:]
      current_passport[key] = value

    if is_last_line:
      if is_passport_valid(current_passport):
        valid_passport_count += 1
  input_file.close()
  return valid_passport_count

print(check_passport_batch())