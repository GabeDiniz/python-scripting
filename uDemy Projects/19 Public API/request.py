import requests   # pip install requests

# This python file simulates a request to the API created in Main.py

request = requests.get("https://gdiniz.pythonanywhere.com/")
data = request.json()

print(data)