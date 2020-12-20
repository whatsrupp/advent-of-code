import copy

def parse_ops(input_file_name="8th_handheld_halting/input.txt"):
  ops = []
  lines = open(input_file_name, 'r')
  for line in lines:
    parsed = line.strip().split(" ")
    ops.append({
      "command": parsed[0],
      "value": int(parsed[1]),
      "visited": False
    })
  return ops

def run_sequence(i, acc, ops):
  visited_indexes = set()

  while True:
    has_exited = i >= len(ops)
    if has_exited:
      return (True, acc)

    is_loop = i in visited_indexes
    if is_loop:
      return (False, acc)
    
    visited_indexes.add(i)

    op = ops[i]
    
    if op["command"] == "nop":
      i += 1
    elif op["command"] == "acc":
      i += 1
      acc += op["value"]
    elif op["command"] == "jmp":
      i += op["value"]

  
def task2():
  ops = parse_ops()
  i = 0
  acc = 0 
  while True:
    op = ops[i]
    command = op["command"]
    value = op["value"]  

    if command == "acc":
      i += 1
      acc += value
    elif command == "nop":
      exits, nested_acc = run_sequence(i + value, acc, ops )
      if exits:
        return nested_acc
      i += 1
    elif command == "jmp":
      exits, nested_acc = run_sequence(i + 1, acc, ops)
      if exits:
        return nested_acc         
      i += value

def task1():
  ops = parse_ops()

  i = 0
  acc = 0

  while True:
    op = ops[i]

    if op["visited"] == True:
      return acc 
    
    op["visited"] = True

    if op["command"] == "nop":
      i += 1
    elif op["command"] == "acc":
      i += 1
      acc += op["value"]
    elif op["command"] == "jmp":
      i += op["value"]
