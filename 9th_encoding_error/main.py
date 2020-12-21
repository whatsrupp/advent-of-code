  
def parse_xmas_sequence(input_file_name="input.txt"):
  sequence = []
  for line in open(input_file_name, 'r'):
    sequence.append(int(line))
  
  return sequence

def task1(preamble = 5):
  sequence = parse_xmas_sequence()

  for i in range(0, len(sequence) - preamble - 1):
    comparison_preamble = sequence[i: i + preamble]
    target = sequence[i + preamble]
    match_lookup = {}
    for number in comparison_preamble:
      match_lookup[number] = number
    
    has_pairing = False 

    for number in comparison_preamble:
      matching_number = target - number
      if (matching_number == number):
        continue
      if match_lookup.get(matching_number):
        has_pairing = True
        break
    
    if not has_pairing:
      return target

  return sequence



