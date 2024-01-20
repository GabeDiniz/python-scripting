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



# Selenium example:
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
  browser.open_page("https://www.google.ca")

  # Wait for 5 seconds
  time.sleep(5)

  # Close the browser
  driver.quit()
  