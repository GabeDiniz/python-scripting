import requests   # pip install requests
from bs4 import BeautifulSoup   # pip install beautifulsoup4

# Get content we scrape through
def get_soup() -> BeautifulSoup:
  headers: dict = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                   }
  request = requests.get("https://www.bbc.com/news", headers=headers)
  html: bytes = request.content
  
  # Create soup
  soup = BeautifulSoup(html, "html.parser")
  return soup

def get_headlines(soup: BeautifulSoup) -> list[str]:
  headlines: set = set()

  # Soup Find All returns a list of headlines
  for hl in soup.findAll("h2", class_="sc-99f698d2-3"):
    headline: str = hl.contents[0].lower()
    headlines.add(headline)

  return sorted(headlines)

def check_headlines(headlines: list[str], term: str):
  term_list: list[str] = []
  terms_found: int = 0

  # Scrape through each headline, if the term is in the headline -> append headline to list
  for i, headline in enumerate(headlines, start=1):
    if term.lower() in headline:
      terms_found += 1
      term_list.append(headline)
      print(f'{i}: {headline.capitalize()} <-------------- "{term}"')
    else:
      print(f'{i}: {headline.capitalize()}')
    
  print("-"*30)
  if terms_found:
    print(f'"{term}" was mentioned {terms_found} times...')
    print("-"*30)

    for i, headline in enumerate(term_list, start=1):
      print(f'{i}: {headline.capitalize()}')
  
  else: 
    print(f'No matches found for "{term}"')
    print("-"*30)



def main():
  soup: BeautifulSoup = get_soup()
  headlines: list[str] = get_headlines(soup=soup)

  user_input: str = input("Enter the key word you want to scrape for >> ")
  check_headlines(headlines, user_input)

if __name__ == "__main__":
  main()