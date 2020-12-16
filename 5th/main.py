

def get_seat_id(boarding_pass):
  char_map = {
    'F': '0',
    'B': '1',
    'L': '0',
    'R': '1'
  }

  binary = "".join(list(map(lambda char : char_map[char], boarding_pass)))
  row = int(binary[0:7], 2)
  seat = int(binary[7:], 2)
  id = (row * 8) + seat
  return  id

def get_my_seat(input_file_name = "input.txt"):
  boarding_passes = open(input_file_name, 'r')
  seat_ids = []
  for boarding_pass in boarding_passes:
    seat_id = get_seat_id(boarding_pass.strip())
    seat_ids.append(int(seat_id))
  seat_ids.sort()

  for i in range(len(seat_ids)):
    current_seat = seat_ids[i]
    next_seat = seat_ids[i+1]
    if (next_seat - current_seat) != 1:
      return current_seat + 1

def get_highest_seat_id(input_file_name = "input.txt"):
  boarding_passes = open(input_file_name, 'r')
  highest_seat_id = 0
  for boarding_pass in boarding_passes:
    seat_id = get_seat_id(boarding_pass.strip())
    if (highest_seat_id < seat_id ):
      highest_seat_id = seat_id
     
  return highest_seat_id


print(get_highest_seat_id())
print(get_my_seat())
