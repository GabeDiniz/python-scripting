from discord import Intents, Client   # pip install discord
import responses

# Fetch Credentials from local .env variables 
from decouple import config

# Constants
BOT_KEY = config('DISCORD_BOT_KEY')

def run_bot(BOT_KEY: str):
  # Basic setup
  # Gets message content
  intents = Intents.default()
  intents.message_content = True
  # Client makes the request
  client = Client(intents=intents)

  knowledge: dict = responses.load_knowledge('knowledge.json')

  @client.event
  # Perform the code as soon as the bot is started
  async def on_ready():
    print(f"{client.user} is now running!")
  
  @client.event
  # Every time a new message appears -> handle msg
  async def on_message(message):
    # Make sure the message being read is not from the bot
    if message.author == client.user:
      return
    
    # ========================================
    # Handle Responses
    # ========================================
    # Check for specific user
    # if str(message.author) == "username here":
    #   response: str = "Oh hello there... I've been expecting you"
    if message.content:
      print(f'({message.channel}) {message.author}: "{message.content}"')
      # Handle !help command
      if message.content == "!help":
        response: str = "Here are my current commands!\n```!help - List commands available```"
      else:
        response: str = responses.get_response(message.content, knowledge=knowledge)

    if response:
      await message.channel.send(response)
      '''
      WIP: Command prefix ****
      Description: Stops bot from erroring out if the message sent does not start with "!". get_response function
        will return None. The following block stops the bot from trying to send None resulting in an error
      
      '''
      
    # Potential error: i.e., missing permissions to access message.content
    else:
      print("[Error] Could not read the message. Make sure you have intents enabled!")

  client.run(token=BOT_KEY)

if __name__ == "__main__":
  run_bot(BOT_KEY=BOT_KEY)