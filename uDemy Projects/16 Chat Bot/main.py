from difflib import get_close_matches

def get_best_match(user_question: str, questions: dict) -> str | None:
  questions: list[str] = [q for q in questions]
  # Gets the closest match of user_question on questions with a threshold of 60%
  matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

  # If get_close_matches finds a match -> 
  if matches:
    return matches[0]
  
def chat_bot(knowledge: dict):
  while True:
    user_input: str = input("You: ")
    best_match: str | None = get_best_match(user_input, knowledge)

    if answer := knowledge.get(best_match):
      print(f"Bot: {answer}")
    else:
      print("Bot: I do not understand...")


if __name__ == "__main__":
  # Commands the bot knows
  brain: dict = {
                 "hello": "Hey there!",
                 "how are you": "I am good, thanks!",
                 "what time is it": "How should I know?",
                 "bye": "See you later!", 
                 "whats good": "just hanging in here..."
                 }
  chat_bot(knowledge=brain)