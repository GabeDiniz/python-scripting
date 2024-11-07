#####################################################
######################  USAGE  ######################
#####################################################
'''
python black-jack-helper.py

Description: 
The script will ask you to enter the the dealers hand,
  along with your hand and it will tell you what the
  blackjack book recommends you to do. 
'''

card_values = {
    'a': 11,  # Ace can also be 1, we'll handle it in the function
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'j': 10, 'q': 10, 'k': 10
}

def get_card_value(card):
  """Get numeric value of a card."""
  return card_values.get(card.lower(), None)

def get_player_cards():
  """Prompt player to enter their hand and return it as a list of values."""
  print("Card options: [A, 2-10, J, Q, K]")
  card1 = input("Enter your first card: ").lower()
  card2 = input("Enter your second card: ").lower()

  if card1 not in card_values or card2 not in card_values:
    print("Invalid card entered. Please enter valid cards.")
    return get_player_cards()

  return [card1, card2]

def calculate_total(hand):
  """Calculate the total value of a hand, treating Aces as 1 or 11."""
  total = sum(get_card_value(card) for card in hand)
  aces = hand.count('a')
  # Adjust for Aces if total is above 21
  while total > 21 and aces:
    total -= 10
    aces -= 1
  return total

def next_move(players_hand, dealers_card):
  """Determine the next move based on blackjack strategy."""
  player_total = calculate_total(players_hand)
  dealer_value = get_card_value(dealers_card)

  # Check for Black Jack
  if player_total == 21:
    print("🧨 Black Jack!")
  # Hard totals
  elif player_total >= 17:
    print("Book says STAND")
  elif 13 <= player_total <= 16 and dealer_value <= 6:
    print("Book says STAND")
  elif 13 <= player_total <= 16 and dealer_value >= 7:
    print("Book says HIT")
  elif 12 == player_total and (dealer_value <= 3 or dealer_value >= 7):
    print("Book says HIT")
  elif 12 == player_total and 4 <= dealer_value <= 6:
    print("Book says STAND")
  elif player_total == 11:
    print("Book says DOUBLE DOWN")
  elif player_total == 10 and dealer_value <= 9:
    print("DOUBLE DOWN!")
  elif player_total == 10 and dealer_value >= 10:
    print("Book says HIT")
  elif player_total == 9 and 3 <= dealer_value <= 6:
    print("DOUBLE DOWN!")
  elif player_total == 9 and (dealer_value == 2 or dealer_value >= 7):
    print("Book says HIT")
  elif player_total <= 8:
    print("Book says HIT")
  else:
    print("No recommendation available for this hand.")

if __name__ == "__main__":
    players_hand = get_player_cards()
    dealers_card = input("Enter dealer's card: ").lower()

    if dealers_card not in card_values:
      print("Invalid dealer card entered. Please enter a valid card.")
    else:
      next_move(players_hand, dealers_card)