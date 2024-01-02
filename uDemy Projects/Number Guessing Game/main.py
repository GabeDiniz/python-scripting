from random import randint

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

# Generate number between 1 and 10
random_num: int = randint(lower, higher)

print(f"Guess the number in the range from {lower} to {higher}.")

while True:
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