import re # Regular Expression

# Load the list of potential words
with open('wordlist.txt', 'r') as file:
  words = [line.strip() for line in file if len(line.strip() == 5)]

# Function for finding potential words
def find_words(words, greens, yellows):

  # Filter thrugh words based on GREEN letters
  for pos, char in enumerate(greens):
    if char != '_': # If char is not a blank/unknown
      # Append word to new listof words if current word has the green char in the same position 
      words = [word for word in words if word[pos] == char]

  # Filter thrugh words based on YELLOW letters
  for pos, char in enumerate(yellows):
    if char != '_': # If char is not a blank/unknown
      # Append word to new listof words if current word DOES NOT have the yellow letter in the same position
      words = [word for word in words if char in word and word[pos] != char]
  
  return words

# User input for green and yellow letters
green_letters = input("Enter green letters (use '_' for unknowns): ")  # e.g., "_pp_e"
yellow_letters = input("Enter yellow letters (use '_' for unknowns): ")  # e.g., "l__r_"

# Finding possible words
possible_words = find_words(words, green_letters, yellow_letters)
print("Possible words:", possible_words)