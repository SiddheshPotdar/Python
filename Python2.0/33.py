import os

source = 'Copy\\third.txt'
destination = 'demo\\third.txt'

try: 
  if os.path.exists(destination):
    print("There is already a file there.")
  else :
    os.replace(source, destination)
    print("{} was moved.".format(source))

except FileNotFoundError:
  print("File not found")
