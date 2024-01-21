from flask import Flask, request  # pip install flask
from random import randint, choice
from datetime import datetime

# Information:
# This API is being hosted using pythonanywhere. The URL is: https://gdiniz.pythonanywhere.com/
#   This file holds the source code that the API uses. Changing the code here will not affect the API
#   as the source code is setup directly in pythonanywhere under: https://www.pythonanywhere.com/user/gdiniz/webapps/

app = Flask(__name__)

# This is the index (or Homepage)
@app.route("/")
def index():
  phrases: list[str] =[
      "What's cooking good looking?", 
      "Hey, you're not supposed to be here...", 
      "Stonk advice: remember, buy high, sell low.. never let them know your next move"
    ]
  return {"phrase": choice(phrases),
          "date": datetime.now()}

# Returns a random number to the user
@app.route("/api/random")
def random():
  number_input = request.args.get("number", type=int, default=100)
  text_input = request.args.get("text", type=str, default="default_text")
  print(number_input)
  print(text_input)

  if isinstance(number_input, int):   # checks that user's input is of type int
    return {
      "input": number_input,
      "random": randint(0, number_input),
      "text": text_input,
      "date": datetime.now()
    }



if __name__ == "__main__":
  app.run()