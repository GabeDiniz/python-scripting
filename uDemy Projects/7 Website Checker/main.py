import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

# Grab websites from CSV
def get_websites(csv_path: str) -> list[str]:
  websites: list[str] = []

  with open(csv_path, 'r') as file:
    reader = csv.reader(file)

    for row in reader:  # Example: row = ["1,", "website.com"]
      # If website does not have https://, append it
      if "https://" not in row[1]:
        websites.append(f"https://{row[1]}")
      else:
        websites.append(row[1])
      
    return websites
  
