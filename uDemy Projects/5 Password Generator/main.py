import string
import secrets # For Secure Random Numbers

# Check for upper case
def contains_upper(password: str) -> bool:
  for char in password:
    if char.isupper():
      return True
  return False

# Check for symbols
def contains_symbols(password: str) -> bool:
  for char in password:
    if char in string.punctuation:
      return True
  return False

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
  combination: str = string.ascii_lowercase + string.digits # returns alphabet + numbers (1-9)

  if symbols:
    combination += string.punctuation
  if uppercase:
    combination += string.ascii_uppercase

  combination_length = len(combination)
  new_password: str = ''

  for _ in range(length): 
    # Append a new random character (pulled from combination) based on requested password length
    new_password += combination[secrets.randbelow(combination_length)]

  return new_password

if __name__ == "__main__":
  while True:
    try:
      pass_length = int(input("Please enter the length of the password you want: "))
      break
    except ValueError:
      print("Please enter a valid number")
  
  for i in range(1, 6):
    new_pass: str = generate_password(length=pass_length, symbols=True, uppercase=True)
    specs: str = f"U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}"
    print(f"{i} >> {new_pass} ({specs})")