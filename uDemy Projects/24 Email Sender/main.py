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


def create_image_attachment(path: str) -> MIMEImage:
  raise NotImplementedError()

def send_email(to_email: str, subject: str, body: str, image: str | None = None):
  # Host and Port for sending emails
  host: str = "smtp-mail.outlook.com"
  port: int = 587

  context = ssl.create_default_context()

  with smtplib.SMTP(host, port) as server:
    print("Logging in...")
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(EMAIL, PASSWORD)

    # Prepare the email
    print("Attempting to send email")
    message = MIMEMultipart()
    message["From"] = EMAIL
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    if image:
      file: MIMEImage = create_image_attachment()
      message.attach(file)

    server.sendmail(from_addr = EMAIL, to_addrs = to_email, msg = message.as_string())

    # Success!
    print("Email sent!")


def main():
  print(EMAIL, PASSWORD)


if __name__ == "__main__":
  main()