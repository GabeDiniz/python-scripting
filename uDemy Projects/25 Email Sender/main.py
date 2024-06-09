import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Fetch Credentials from local .env variables 
from decouple import config

# Email Credentials
EMAIL = config('EMAIL')
PASSWORD = config('EMAIL_PASS')


def create_image_attachment(path: str) -> MIMEImage:
  with open(path, "rb") as image:
    mime_image = MIMEImage(image.read())
    mime_image.add_header("Content-Disposition", f"attachment; filename={path}")
    return mime_image

def send_email(to_email: str, subject: str, body: str, image: str | None = None):
  # Host and Port for sending emails
  host: str = "smtp.gmail.com"
  port: int = 465

  with smtplib.SMTP_SSL(host, port) as server:
    print("Logging in...")
    
    server.login(EMAIL, PASSWORD)
    server.ehlo()

    # Prepare the email
    print("Attempting to send email...")
    message = MIMEMultipart()
    message["From"] = EMAIL
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    if image:
      file: MIMEImage = create_image_attachment(image)
      message.attach(file)

    server.sendmail(from_addr = EMAIL, to_addrs = to_email, msg = message.as_string())

    # Success!
    print("Email sent!")


def main():
  to: str = input("Address of who this should be sent to >> ")
  send_email(to_email="gabriel.sundiniz@gmail.com", subject="Sent from Python!", body="Hello! What's going on!")


if __name__ == "__main__":
  main()