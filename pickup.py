import random

def random_pickup():
  random_lines = random.choice(open("pickup_lines.txt").readlines())
  print(random_lines)
  return random_lines