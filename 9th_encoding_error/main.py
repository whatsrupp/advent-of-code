  
def parse_xmas_sequence(input_file_name="input.txt"):
  sequence = []
  for line in open(input_file_name, 'r'):
    sequence.append(int(line))
  
  return sequence

def get_first_encryption_mismatch(sequence, preamble):
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

def task1(preamble = 5):
  sequence = parse_xmas_sequence()
  return get_first_encryption_mismatch(sequence, preamble)
  

def task2(preamble = 5):
  sequence = parse_xmas_sequence()
  target_number =  get_first_encryption_mismatch(sequence, preamble)

  for i in range(0, len(sequence) -1):
    running_sum = 0
    contiguous_sequence = []
    for j in range(i, len(sequence) - 1):
      running_sum += sequence[j]
      contiguous_sequence.append(sequence[j])
      if running_sum == target_number:
        return max(contiguous_sequence) + min(contiguous_sequence)
      elif running_sum > target_number:
        break



# Refelection
# min and max in python ranges, although it's probably slightly better to just sort and access the first and last element as it requires less list scans.
# did this quite quickly which was nice
# there's definitely an 
# Found naming quite hard in this, lots of variants of things that are essentially numbers
# used i and j to refer to indexes which then just access things - thought it was more explicit
# There's definitely a good way to do this as we step through the numbers, but it complicates things logically
# You could keep a running sum of each number as you step through, but then you lean on memory more.
# Wonder if this is actually based on some sort of old cipher.
# No Multiline comments in python - whuuut

