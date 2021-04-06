# Hieu Ngo
# 11/2/2020
# Assignment 6a - Write a function names list_max that takes as a parameter
# a list of numbers then searches for its maximum number.

def rec_list_max(list, pos=0, max_int=0):
  """Takes a list parameter and finds the max number using recursion."""
  if pos == len(list):
    return max_int

  current_max = list[pos]

  if current_max >= max_int:
    max_int = current_max

  return rec_list_max(list, pos + 1, max_int)

def list_max(list, pos=0, max_int=0):
  max_int = list[0]
  return rec_list_max(list, pos, max_int)



list = [-3, -4, -3, -2, -10]

print(list_max(list))
