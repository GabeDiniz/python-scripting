
def check_password(password: str):
  with open("passwords.text", "r") as file:
    common_passwords: list[str] = file.read().splitlines()
  
  for i, common_password in enumerate(common_passwords, start = 1):  # start enumeration at 1
    if password == common_password:
      print(f"{password}: ❌ (#{i})")
      return
    
  print(f"{password}: ✅ (unique)!")

def main(): 
  while True:
    user_password: str = input("Enter a password: ")
    if len(user_password) < 4:
      print("Please enter a password with a minimum of 4 character...")
      continue
    break
  check_password(user_password)

if __name__ == "__main__":
  main()