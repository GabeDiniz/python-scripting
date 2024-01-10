import os
import requests

# Get IMAGE extension (i.e., png, jpg, etc.)
def get_extension(image_url: str) -> str | None:
  extensions: list[str] = [".png", ".jpeg", ".jpg", ".gif", ".svg"]

  for extension in extensions:
    if extension in image_url:
      return extension
    
  