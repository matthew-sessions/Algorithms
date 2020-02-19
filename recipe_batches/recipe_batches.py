#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipe_keys = list(recipe.keys())
  batches_able = []
  for i in recipe_keys:
    if ingredients.get(i) != None:
      num = ingredients[i] // recipe[i]
      batches_able.append(num)
    else:
      return 0
  total = min(batches_able)
  return(total)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))