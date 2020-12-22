def parse_adapters(input_file_name="input.txt"):
  adapters = []
  adapters.append(0)
  for line in open(input_file_name, 'r'):
    adapters.append(int(line))
  
  adapters.sort()
  adapters.append(adapters[-1] +3)

  return adapters
def task1():
  adapters = parse_adapters()
  differences = {
    1: 0,
    2: 0,
    3: 0
  }  
  for i in range(0, len(adapters)-1):
    difference = adapters[i+1] - adapters[i]
    differences[difference] += 1
  print(differences)
  return differences.get(1) * differences.get(3)

def task2_recursive():
  adapters = {}
  adapters_array = parse_adapters()
  terminator = adapters_array[-1]

  for adapter in adapters_array:
    adapters[adapter] = adapter

  def count_branches(node):
    if node == terminator:
      return 1
    count = 0
    print(node)
    for i in range (1, 4):
      child = adapters.get(node + i)
      if child:
        count += count_branches(child)
    return count
  
  return count_branches(0)

def task2():
  adapters = parse_adapters()
  chunks = []
  current_chunk = []
  for i in range(len(adapters) - 1):
    current_chunk.append(adapters[i])
    diff = adapters[i+1] - adapters[i]
    is_terminating = diff == 3
    if is_terminating:
      chunks.append(current_chunk)
      current_chunk = []
  chunks.append([adapters[-1]])

  combinations = 1
  for chunk in chunks:
    n = len(chunk)
    combinations_in_chunk = (n**2 - (3*n) + 4 )/ 2
    combinations *= combinations_in_chunk
  return combinations


# Reflection
# Part 1 absolute breeze
# Sort and count the differences. very nice
# Part 2, just went for the recursive brute force initally which worked fine for small datasets.
# This is the first one where the problem was expanded into a place where you have to consider the most efficient method which was nice
# I really a combination tree that converges at points. You can break down the problem by considering the combinations between two converged points and then multiplying together.

#     /-[]-\
# -[]-      -[]-[]-[]
#     \-[]-/
#   1 * 2 * 1 * 1 * 1

# At that point, if you can find a nice way to find out the combination for each chunk then you're good to go.
# I made a big blunder here and didn't assume that there were only gaps of 1s and 3s. 
# I was trying to find a general expression for sequences that had a combination of gaps of 2s and 3s - nightmarish
# However, for a sequence with gaps of 1 the combinatins can be simplified to a nice quadratic series
# What a real gcse throw back https://www.mytutor.co.uk/answers/1409/GCSE/Maths/How-do-you-find-the-nth-term-formula-for-a-sequence-with-non-constant-difference/
