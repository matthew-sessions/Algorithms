#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']
  outcome = []
  if n == 0:
    return([[]])
  elif n == 1:
    return([['rock'], ['paper'], ['scissors']])
  else:

    for i in rock_paper_scissors(n-1):
      outcome.append((i + [options[0]]))
      outcome.append((i + [options[1]]))
      outcome.append((i + [options[2]]))
    return outcome


print(rock_paper_scissors(2))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')