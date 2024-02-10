import os
import shutil

# path = 'empty_folder\\f1.txt'
# path = 'empty_folder'
path = 'complete_folder'

try:
  # os.remove(path) # To delete a file
  # os.rmdir(path) # To delete an empty folder
  shutil.rmtree(path) # to delet all files in folder and folder itself

except FileNotFoundError as error:
  print("File was not find.")