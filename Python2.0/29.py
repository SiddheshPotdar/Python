import os

path = "D:\\codes\\Python2.0\\demo"
# path = "D:\\codes\\Python2.0\\demo\\test.txt"

if os.path.exists(path):
  print("this path exists")
  if os.path.isfile(path):
    print("this is file")
  elif os.path.isdir(path):
    print("this is a directory")
else: 
  print("This path does not exist")