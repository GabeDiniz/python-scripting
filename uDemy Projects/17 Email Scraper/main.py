import re
from typing import Final
import time
from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Regex used for finding e-mails in text
EMAIL_REGEX: Final[str] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

class Browser:
  def __init__(self):
    print("Starting up browser...")
    self.chrome_options = Options()
    self.chrome_options.add_argument("--headless")
    self.chrome_options.add_argument("--disable-extensions")
    self.chrome_options.add_argument("--disable-gpu")

    # self.service = Service(driver)
    self.browser = webdriver.Chrome(options=self.chrome_options)
    
  def scrape_emails(self, url: str) -> set:
    print(f"Scraping: {url} for emails")
    self.browser.get(url)
    page_source: str = self.browser.page_source

    list_of_emails: set = set()
    for re_match in re.finditer(EMAIL_REGEX, page_source):
      list_of_emails.add(re_match.group())
    
    return list_of_emails
  
  def close_browser(self):
    print("Closing browser...")
    self.browser.close()

def main():
  # Initiate browser (Chrome)
  browser = Browser()

  # User input, TEST URL: https://randomlists.com/email-addresses?qty=50
  url: str = input("Input the URL you would like to scrape: ")
  emails: set = browser.scrape_emails(url)

  # If no emails found, return message
  if len(emails) == 0:
    print("No emails were found on this site...\nExiting.")
    return
  # Else, print all the emails found
  for i, email in enumerate(emails, start=1):
    print(i, email, sep=": ")

if __name__ == "__main__":
  main()


# Selenium example:
'''
class Browser:
  def __init__(self, driver):
    print("Starting...")
    self.browser = driver  # Use the passed WebDriver instance

  def open_page(self, url):
    print(f"Opening: {url}")
    self.browser.get(url)
if __name__ == "__main__":
  # Create a single WebDriver instance
  driver = webdriver.Chrome()
  # Pass this driver to the Browser instance
  browser = Browser(driver)
  emails: set = browser.scrape_emails("https://randomlists.com/email-addresses?qty=50")
  for i, email in enumerate(emails):
    print(i, email, sep=": ")
  browser.open_page("https://www.google.ca")

  # Wait for 5 seconds
  time.sleep(5)

  # Close the browser
  driver.quit()
'''