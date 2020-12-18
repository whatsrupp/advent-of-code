
def parse_bags(input_file_name="input.txt"):
  bags = {}
  lines = open(input_file_name, 'r')

  for line in lines:
    bag_description, _, rules_description = line.strip().partition("contain")
    bag_colour = "_".join(bag_description.split(' ')[:2]) # converts to snake case eg shiny_gold
    # rule_descriptions = children_info.split(",")
    rules = []

    if "no" in rules_description:
      bags[bag_colour] = []
      continue

    for rule_description in rules_description.split(','):
      tokens = rule_description.strip().split(' ')
      amount = tokens[0]
      child_bag_colour = "_".join(tokens[1:3])
      rules.append({
        "amount": int(amount),
        "colour": child_bag_colour
      })
      
    bags[bag_colour] = rules
  
  return bags



def task1():
  bags = parse_bags()

  def can_contain_target(bag_colour):
    target_bag_colour = "shiny_gold"

    rules = bags[bag_colour]

    if len(rules) == 0:
      return False

    for rule in rules:
      if rule["colour"] == target_bag_colour:
        return True
      else:
        return can_contain_target(rule["colour"])

  bag_count = 0
  for bag_colour in bags.keys():
    if can_contain_target(bag_colour):
      bag_count += 1

    
  return bag_count



