#!/usr/bin/python

import argparse
import random
import time

def find_max_profit(prices):
  prices_enu = list(enumerate(prices))
  prices_sorted = sorted(prices_enu, key=lambda x: x[1])

  price_len = len(prices)
  
  for i in range(len(prices)//2):
    curs_left, curs_right = prices_sorted[i], prices_sorted[(-i)-1]
    if curs_left[0] < curs_right[0]:
      return curs_right[1] - curs_left[1]
    elif prices_sorted[i + 1][0] < prices_sorted[(-i)-1][0] and prices_sorted[i][0] < prices_sorted[(-i)-2][0]:
      left_slide, right_slide = prices_sorted[(-i)-1][1] - prices_sorted[i + 1][1], prices_sorted[(-i)-2][1] - prices_sorted[i][1]
      if left_slide <= right_slide:
        return right_slide
      else:
        return left_slide
    elif prices_sorted[i + 1][0] < prices_sorted[(-i)-1][0]:
      return prices_sorted[(-i)-1][1] - prices_sorted[i + 1][1]
    elif prices_sorted[i][0] < prices_sorted[(-i)-2][0]:
      return prices_sorted[(-i)-2][1] - prices_sorted[i][1]
    else:
      res = max([prices[i+1] - prices[i] for i in range(price_len - 1)])
      return res

  return(False)


def find_max_profit2(prices):

  current_min_price_so_far = float('inf')
  max_profit_so_far = float('-inf')
  

  for i in range(0, len(prices)-1):

    if prices[i] < current_min_price_so_far:

      current_min_price_so_far = prices[i]
      lowest_day_index = i
    for j in range(i+1,len(prices)):
      trade_profit = prices[j] - prices[i]
      if trade_profit > max_profit_so_far:
        max_profit_so_far = trade_profit
  return max_profit_so_far

li = [random.randint(0,5000) for i in range(5000)]
li2 = li.copy()

start_time = time.time()
print(find_max_profit(li))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(find_max_profit2(li2))
print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))