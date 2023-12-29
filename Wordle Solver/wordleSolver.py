#####################################################
######################  USAGE  ######################
#####################################################
'''
python wordleSolver.py

Description: 
The script will ask you to enter the green letters
  and the yellow letters that are known. From that
  it will iterate through a list of valid words and
  return a list of the possible words.

Time Complexity: O(n)
1. Looping over greens: we iterate through each char
  in greens. Since the greens string of max length 5
  the loop runs 5 times, resulting in O(5) which 
  simplifies to O(1)

2. List Comprehension: Here we create a new list of
  words by iterating through each word. The time
  complexity here depends on the list of words (n). 
  Therefore, the time complexity here is O(n). 
'''

# Load the list of potential words
with open('wordlist.txt', 'r') as file:
  words = [line.strip() for line in file]

# Function for finding potential words
def find_words(words, greens, yellows, grays):

  # Filter through words based on GRAY letters
  for char in grays:
    words = [word for word in words if char not in word]
  
  print(words)

  # Filter through words based on GREEN letters
  for pos, char in enumerate(greens):
    if char != '_': # If char is not a blank/unknown
      # Append word to new listof words if current word has the green char in the same position 
      words = [word for word in words if word[pos] == char]

  print(words)
  # Filter through words based on YELLOW letters
  for pos, char in enumerate(yellows):
    if char != '_': # If char is not a blank/unknown
      # Append word to new listof words if current word DOES NOT have the yellow letter in the same position
      words = [word for word in words if char in word and word[pos] != char]
      
  return words

# User input for green and yellow letters
while True:
  green_letters = input("Enter green letters (use '_' for unknowns): ")  # e.g., _pp_e
  yellow_letters = input("Enter yellow letters (use '_' for unknowns): ")  # e.g., l__r_
  if len(green_letters) !=5 or len(yellow_letters) != 5:
    print("Error: The length of the input should be 5.\nExample: h_ll_ / _____ / etc.")
  else:
    break

gray_letters = input("Enter the gray letters (i.e., ahdfb): ")

# Finding possible words
possible_words = find_words(words, green_letters, yellow_letters, gray_letters)
print("Possible words:", possible_words)