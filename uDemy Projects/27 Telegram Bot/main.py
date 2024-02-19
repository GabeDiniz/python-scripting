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