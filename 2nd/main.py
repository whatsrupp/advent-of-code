import re

inputFile = open('input.txt', 'r') 
lines = inputFile.readlines() 
  
valid_password_count = 0
# Strips the newline character 
for line in lines: 
    first_number = int(re.search(r'^\d+', line).group(0))
    second_number = int(re.search(r'(?<=-)\d+', line).group(0))
    character = re.search(r'\w(?=\:)', line).group(0)
    password = re.search(r'\w+$', line).group(0)

    character_count = len(re.findall(character ,password))
    is_valid = first_number <= character_count and character_count <= second_number
    if( is_valid ):
      valid_password_count += 1

    print(first_number,second_number, character, password, character_count, is_valid)

print(valid_password_count)