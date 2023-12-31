import qrcode
import sys
import os

#####################################################
##################  PREREQUISITES  ##################
#####################################################
'''
pip install qrcode[pil]
'''

#####################################################
######################  USAGE  ######################
#####################################################
'''
python QR-generator.py <url> <filename>

Description: 
The URL parameter is the link you would like the QR
  code to lead to, and filename is the name of 
  the image it will generate
'''


# Check that filename was passed as an argument
if len(sys.argv) != 3:
  print("Usage: python QR-generator.py <url> <filename>")
  print("Example: python QR-generator.py https://www.youtube.com/ YouTube")
  sys.exit(1)

# URL to be made into a QR
data = sys.argv[1]

# QRcode Class
qr = qrcode.QRCode(
  version=1,
  error_correction=qrcode.constants.ERROR_CORRECT_L,
  box_size=10,
  border=2,
)

# Add data to the instance 'qr'
qr.add_data(data)
qr.make(fit=True)

# Create the QR image
img = qr.make_image(fill_color="black", back_color="white")
img_name = f"{sys.argv[2]}.png"

# Check if the file already exists
while True:
  if os.path.exists(img_name):
    print(f"The file '{img_name}' already exists in this directory. Please enter a new name...")

    # Request new name to be entered
    new_name=input("New filename: ")
    img_name=new_name
  else:
    img.save(f"{img_name}.png")
    print(f"QR code saved as {img_name}")
    break # Exit code block