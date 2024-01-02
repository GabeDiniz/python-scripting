from random import randint

# User input for guessing range
lower = 1
print("Enter the upper bound of the range you would like to guess to. This number should be greater than 1.")
while True:
  try:
    higher: int = int(input("Higher bound: "))
    if higher < 2: 
      print("Please enter a number greater than 1.")
      continue
  except ValueError:
    print("Please enter a valid number.")
    continue
  break

# User input for number of guessing
while True:
  try: 
    guess_attempts: int = int(input("Enter the number of guess you would like to have: "))
    if guess_attempts < 1:
      print("Please enter a number greater than 0.")
      continue
  except ValueError:
    print("Please enter a valid number.")
    continue
  break

# Generate number between 1 and 10
random_num: int = randint(lower, higher)

print(f"Guess the number in the range from {lower} to {higher}.")

while guess_attempts > 0:
  if guess_attempts > 1:
    print(f"You have {guess_attempts} guesses...")
  else: 
    print("Final guess! Make it count...")
  try: 
    user_guess: int = int(input("Guess: "))
  # if the user input is not of type int, exception is thrown
  except ValueError:
    print("Please enter a valid number.")
    continue # Goes back to the top of the loop

  if user_guess > random_num:
    print("The number is lower")
  elif user_guess < random_num:
    print("The number is higher")
  else:
    print("That's correct!")
    break # Exits loop

  guess_attempts -= 1

if guess_attempts == 0:
  print(f"You are out of guesses! The answer was {random_num}. Better luck next time ;)")