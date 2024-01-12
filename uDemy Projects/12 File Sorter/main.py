import os
import shutil

# Create a folder named after the extension of the file passed in
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
      extension: str = os.path.splitext(filename)[1]  # Splits the extension

      if extension:
        target_folder: str = create_folder(source_path, extension)
        target_path: str = os.path.join(target_folder, filename)

        shutil.move(file_path, target_path)

# Removes all empty folders
def remove_empty_folders(source_path: str):
  for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
    for current_dir in sub_dir:
      folder_path: str = os.path.join(root_dir, current_dir)

      if not os.listdir(folder_path):   # If this path is empty -> remove it
        os.rmdir(folder_path)

def main():
  user_input: str = "Please input the file path you would like to be sorted: "
  if os.path.exists(path=user_input):
    sort_files(user_input)
    remove_empty_folders(user_input)
    print("Files sorted successfully!")
  else:
    print("Invalid path, please provide a valid file path.")

if __name__ == "__main__":
  main()