import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import AnyStr

# Fetch Credentials from local .env variables 
from decouple import config

# Email Credentials
EMAIL = config('EMAIL')
PASSWORD = config('EMAIL_PASS')

def main():
  print(EMAIL, PASSWORD)

if __name__ == "__main__":
  main()