import qrcode # pip install qrcode
from PIL import Image


class MyQR:
  def __init__(self, size: int, padding: int):
    self.qr = qrcode.QRCode(box_size=size, border=padding)

  def create_qr(self, file_name: str, fg: str, bg: str):
    user_input: str = input("Enter the text to be associated with the QR: ")

    try:
      self.qr.add_data(user_input)  # Add data to QR code
      qr_image = self.qr.make_image(fill_color=fg, back_color=bg)   # Create QR image with specified colors
      qr_image.save(file_name)
      print(f"Successfully created QR Code called {file_name}!")

    except Exception as e:
      print(f"Error: {e}")

def main():
  # Initialize QR Class
  myqr = MyQR(size=40, padding=1)
  # Create QR
  name = input("Enter your file/image name: ")
  if ".png" not in name and ".jpg" not in name:
    name += ".png"
  myqr.create_qr(name, fg="#BD8334", bg="#FAF3EF")

if __name__ == "__main__":
  main()