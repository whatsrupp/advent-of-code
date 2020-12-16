import pytest
from main import get_seat_id, get_highest_seat_id

def test_get_seat_id():
  assert(get_seat_id('FBFBBFFRLR') == 357)
  assert(get_seat_id('BFFFBBFRRR') == 567)
  assert(get_seat_id('FFFBBBFRRR') == 119)
  assert(get_seat_id('BBFFBBFRLL') == 820)

def test_check_boarding_passes():
  assert(get_highest_seat_id('test_input.txt') == 820 )
