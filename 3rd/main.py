def toboggan(x_delta, y_delta):

  inputFile = open('input.txt', 'r')
  lines = inputFile.readlines()

  def is_tree(char):
    return char == '#'

  x = 0
  y = 0 
  wrap_x = None
  
  tree_count = 0

  for line in lines:
    if wrap_x is None:
      wrap_x = len(line) -1 

    if(y % y_delta != 0):
      y += 1
      continue

    char = line[x % wrap_x]
    if is_tree(char):
      tree_count += 1
    x += x_delta
    y += 1

  return tree_count

answer = toboggan(1,1) * toboggan(3,1) * toboggan(5,1) * toboggan(7,1) * toboggan(1,2)
print(answer)