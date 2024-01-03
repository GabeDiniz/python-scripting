from random import choice

def run_game():
  # Choice picks a random element from the provided list
  word: str = choice(['apple', 'secret', 'banana'])

  username: str = input("What is your name? >> ")
  print(f"Welcome to Hangman, {username}!")

  # Setup
  guessed: str = ''
  tries: int = 5

  # Game
  while tries > 0:
    blanks: int = 0

    print("Word: ", end="")   # end="" makes it so the next print isn't on a Newline
    for char in word:
      if char in guessed:
        print(char, end="")
      else:
        print("_", end="")
        blanks += 1
      
    print()   # Adds blank line

    if blanks == 0:
      print("You win!")
      break
    
    guess: str = input("Enter a letter: ")
    if len(guess) != 1:
      print("Please enter a single letter.")
      continue

    # If current guess has already been used, try again
    if guess in guessed:
      print(f'You already used: "{guess}". Please try another letter')
      continue
    guessed += guess

    if guess not in word:
      tries -= 1
      print(f"That letter is not in the word... ({tries} tries remaining)")

      if tries == 0:
        print("No more tries remaining... You lose.")
        break

if __name__ == '__main__':
  run_game()