import os
import requests

# Get IMAGE extension (i.e., png, jpg, etc.)
def get_extension(image_url: str) -> str | None:
  extensions: list[str] = [".png", ".jpeg", ".jpg", ".gif", ".svg"]

  for extension in extensions:
    if extension in image_url:
      return extension
    
def download_image(image_url: str, name: str, folder: str = None):
  if ext := get_extension(image_url):   # Check for extension in the image URL
    if folder:  # Check if the user specified a folder name
      image_name: str = f"{folder}/{name}{ext}"
    else: 
      image_name: str = f"{name}{ext}"
  else:
    raise Exception("Image extension could not be located...")
  
  if os.path.isfile(image_name):  # Check if the file already exists
    raise Exception("Image name already exists...")
  
  # Download image
  try:
    image_content: bytes = requests.get(image_url).content
    with open(image_name, "wb") as handler:   # wb = Write Bytes
      handler.write(image_content)
      print(f'Downloaded: "{image_name}" successfully!')
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  input_url: str = input("Enter a url: ")
  input_name: str = input("Image file name: ")

  print("Downloading...")
  download_image(input_url, input_name, "images")