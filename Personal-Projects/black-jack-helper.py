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


def get_player_cards():
  print("Card options: [A, 2-10, J, Q, K]")
  card1 = input("Enter your first card: ").lower()
  card2 = input("Enter your second card: ").lower()

  return [card1, card2]

def next_move(players_hand, dealers_hand):
  # base
  if ('8' in players_hand and '3' in players_hand) or ('8' in players_hand and '4' in players_hand):
    print("Book says HIT")
  elif ('A' in players_hand and '8' in players_hand) or ('A' in players_hand and '9' in players_hand):
    print("Book says HIT")

if __name__ == "__main__":
  players_hand =  get_player_cards()
  dealers_hand = [input("Enter dealers card: ").lower()]
  print(players_hand)
  print(dealers_hand)

  while True: 
    next_move(players_hand, dealers_hand)
    break