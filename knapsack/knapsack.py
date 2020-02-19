#!/usr/bin/python

import sys
from collections import namedtuple
from sortit import *

Item = namedtuple('Item', ['index', 'size', 'value'])



def knapsack_solver(items, capacity):
  value_to_weight = [i[2]/i[1] for i in items]
  sorted_values, sorted_items = merge_sort2(value_to_weight, items)
  cap_counter = 0
  value = 0
  results = []
  for i in range(len(sorted_items)-1, -1, -1):
    if sorted_items[i][1] + cap_counter <= capacity:
      results.append(sorted_items[i][0])
      value += sorted_items[i][2]
      cap_counter += sorted_items[i][1]
  results = sorted(results)
  return({'Value':value, 'Chosen':results})
  
#print(knapsack_solver([[1,2,15], [2,5,98], [3,1,54], [4,56,1000], [5, 3,20]], 6))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')