#hardcode test folder path 
#folder_path = "users/sade/desktop/test"
def list_files(folder_path):
   import os
   files = os.listdir(folder_path) 
   for file in files:
      print(file)
   return files

def get_file_extension(file_name):
      import os
      files = os.listdir(folder_path)
      extensions = set()
      for file in files:
          file_name = file
          file_name = file_name.lower()
          file_extension = os.path.splitext(file_name)[1]
          if file_extension:
            extensions.add(file_extension)
      return extensions
# Create folders based on the file extensions in the set 
def create_folders(folder_path, extensions):
    import os
    for ext in extensions:
        folder_name = ext[1:]  # Remove the dot from the extension
        new_folder_path = os.path.join(folder_path, folder_name)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print(f"Created folder: {new_folder_path}")

# Move files to the corresponding folders
def move_files(folder_path, extensions):
    import os
    for ext in extensions:
        folder_name = ext[1:]  # Remove the dot from the extension
        new_folder_path = os.path.join(folder_path, folder_name)
        for file in os.listdir(folder_path):
            if file.endswith(ext):
                old_file_path = os.path.join(folder_path, file)
                new_file_path = os.path.join(new_folder_path, file)
                os.rename(old_file_path, new_file_path)



# Main function to execute the script
print("Enter the folder path: ")
folder_path = input()
print("Listing files in the folder: " + folder_path)
print("Files:")
files = list_files(folder_path)
print("Extensions:")
extensions = get_file_extension(folder_path)
print(extensions)
print("Creating folders for each extension...")
create_folders(folder_path, extensions)
print("Moving files to their respective folders...")
move_files(folder_path, extensions)
