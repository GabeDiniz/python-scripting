# Telegram Bot
# Name: Mario
# username: GabeDini_bot
from typing import Final
# pip install python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Fetch Credentials from local .env variables 
from decouple import config

# Constants
TOKEN = config('BOT_API_KEY')
BOT_USERNAME: Final[str] = "@GabeDini_bot"

# Triggered when start command is used
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("Well hello there! Nice to meet you. Let\'s chat ;)")

# Triggered when help command is used
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("Type something, and I will respond!")

# Triggered when custom command is used
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("Custom command goes here")


def handle_response(text: str) -> str:
  processed: str = text.lower()

  if "hello" in processed:
    return "Hey there!"
  if "how are you" in processed:
    return "I am doing well, thanks!"
  if "i love python" in processed:
    return "Damn right! Its awesome"
  
  return "I do not understand"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  message_type: str = update.message.chat.type
  text: str = update.message.text

  # Log
  print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

  # If youre in a group chat and the bot is not mentioned directly
  #   -> dont respond to avoid spamming
  if message_type == "group":
    if BOT_USERNAME in text:
      new_text: str = text.replace(BOT_USERNAME, "").strip()
      response: str = handle_response(new_text)
    else: 
      return
  # Otherwise, if in a private text, respond regardless
  else:
    reponse: str = handle_response(text)

  # Reply
  print("Bot:", reponse)
  await update.message.reply_text(reponse)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
  print(f"Update {update} caused error: {context.error}")

def main():
  print("Starting up the bot...")
  app = Application.builder().token(TOKEN).build()

  # Commands
  app.add_handler(CommandHandler('start', start_command))
  app.add_handler(CommandHandler('help', help_command))
  app.add_handler(CommandHandler('custom', custom_command))

  # Messages
  app.add_handler(MessageHandler(filters.TEXT, handle_message))

  # Errors
  app.add_error_handler(error)

  # Checking for messages every x amount of seconds
  print("Polling...")
  app.run_polling(poll_interval=5)

if __name__ == "__main__":
  main()