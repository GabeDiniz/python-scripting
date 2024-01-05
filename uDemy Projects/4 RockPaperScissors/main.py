import random
import sys

class RPS:
  def __init__(self):
    print("Welcome to RPS!")
    self.moves: dict = {"rock": "💎", "paper": "🧻", "scissors": "✂"}
    # Create list of keys from dictionary
    self.valid_moves: list[str] = list(self.moves.keys())

  def play_game(self):
    user_move: str = input("Rock, paper, or scissors? >>").lower()

    if user_move == "exit":
      print("Thanks for playing!")
      sys.exit()

      if user_move not in self.valid_moves:
        print("Invalid moves...")
        return self.play_game
      
      # Give AI raandom move
      ai_move: str = random.choice(self.valid_moves)

      self.display_moves(user_move, ai_move)
      self.check_move(user_move, ai_move)
  
  def display_moves(self):
    ...

  def check_move(self):
    ...

def RPS():
  print


if __name__ == "__main__":
  rps = RPS()