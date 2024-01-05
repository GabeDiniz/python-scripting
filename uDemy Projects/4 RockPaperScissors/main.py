import random
import sys

class RPS:
  def __init__(self):
    print("Welcome to RPS!")
    self.moves: dict = {"rock": "💎", "paper": "🧻", "scissors": "✂"}
    # Create list of keys from dictionary 
    self.valid_moves: list[str] = list(self.moves.keys())

  def play_game(self):
    user_move = input("Rock, paper, or scissors? >> ").lower()

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
  
  def display_moves(self, user_move: str, ai_move: str):
    print("-----")
    print(f"You: {self.moves[user_move]}")
    print(f"AI: {self.moves[ai_move]}")
    print("-----")

  def check_move(self, user_move: str, ai_move: str):
    if user_move == ai_move: # TIE
      print("It\'s a tie!")
    elif (user_move == "rock" and ai_move == "scissors") or (user_move == "scissors" and ai_move == "paper") or (user_move == "paper" and ai_move == "rock"):
      print("You win!")
    else:
      print("AI wins...")

if __name__ == "__main__":
  rps = RPS()
  while True:
    rps.play_game()