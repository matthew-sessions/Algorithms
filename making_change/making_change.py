#!/usr/bin/python

import sys

def making_change(amount, denominations):
  combos = [0] * (amount + 1)
  combos[0] = 1
  for i in denominations:
    if amount >= i:
      for ind in range(0, len(combos)):
        if ind >= i:
          sub_index = ind - i
          new_val = combos[sub_index] + combos[ind]
          combos[ind] = new_val
  return(combos[-1])


print(making_change(300, [1, 5, 10, 25, 50]))


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")