import random

# Function for rolling the dice
# Default input is 2, returns list of integers
def roll_dice(amount: int = 2) -> list[int]:
  if amount <= 0:
    raise ValueError
  
  rolls: list[int] = []
  for i in range(amount):
    random_roll: int = random.ranint(1, 6)
    rolls.append(random_roll)

  return rolls