import os
import shutil
from tkinter import filedialog
from tkinter import *

# Create a folder named after the extension of the file passed in -> return folder path
def create_folder(path: str, extension: str) -> str:
  '''
  path -> Path specified by the user that holds the random files
  extension -> Extension of the file being looked at
  '''
  extension: str = extension[1:]  # Remove . from .extension
  folder_path: str = os.path.join(path, extension)  # Create new folder path (i.e., ...\png)

  # If the folder path has not been created -> mkdir
  if not os.path.exists(folder_path):
    os.makedirs(folder_path)

  return folder_path

# Sort the files based on the given path
def sort_files(source_path: str):
  for root_dir, sub_dir, filenames in os.walk(source_path):   # os.walk goes through every directory in the specified path
    for filename in filenames:
      file_path: str = os.path.join(root_dir, filename)
      extension: str = os.path.splitext(filename)[1]  # Splits the extension (i.e., .png -> png)

      if extension:
        target_folder: str = create_folder(source_path, extension)  # Create the folder using create_folder function -> return folder_path
        target_path: str = os.path.join(target_folder, filename)  # Set target path to folder_path/filename (i.e., the destination of the file)

        shutil.move(file_path, target_path)   # Move the file

# Removes all empty folders
def remove_empty_folders(source_path: str):
  for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
    for current_dir in sub_dir:
      folder_path: str = os.path.join(root_dir, current_dir)

      if not os.listdir(folder_path):   # If this path is empty -> remove it
        os.rmdir(folder_path)

def main():
  root = Tk()
  root.withdraw()
  selected_folder = filedialog.askdirectory()
  if os.path.exists(path=selected_folder):
    sort_files(selected_folder)
    remove_empty_folders(selected_folder)
    print("Files sorted successfully!")
  else:
    print("Invalid path, please provide a valid file path.")

if __name__ == "__main__":
  main()