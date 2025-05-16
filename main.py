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
   
      return os.path.splitext(file_name)[1]


def move_file(file_name, destination_folder):
      import os
      import shutil
      source = os.path.join(folder_path, file_name)
      destination = os.path.join(destination_folder, file_name)
      shutil.move(source, destination)

print("Enter the folder path: ")
folder_path = input()
print("Listing files in the folder:")
print(folder_path)
print("Files:")
files = list_files(folder_path)
   #print(get_file_extension(file))





# Add CLI with argparse