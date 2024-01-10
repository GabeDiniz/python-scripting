import itertools
import string
import time

def common_guess(word: str) -> str | None:
  with open("words.txt", "r") as words:
    word_list: list[str] = words.read().splitlines()

  # Iterate through common words 
  for i, match in enumerate(word_list, start = 1):
    if match == word:
      return f"Common match: {match} (#{i})"
    
def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
  chars: str = string.ascii_lowercase

  if digits:
    chars += string.digits
  if symbols:
    chars += string.punctuation
  
  attempts: int = 0
  for guess in itertools.product(chars, repeat=length): # Itertools will brute force possible combinations
    attempts += 1
    guess: str = ''.join(guess)

    if guess == word:
      return f'"{word}" was cracked in {attempts:,} guesses.'
    
    # print(guess, attempts)

def main():
  print("Searching...")
  password: str = "abc1"

if __name__ == "__main__":
  print(common_guess("car"))