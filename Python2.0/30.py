# with open('demo\\test.txt') as file:
#   print(file.read())

# print(file.closed)

#* handling file not found exception
try:
  with open('demo\\test.tt') as file:
    print(file.read())
except FileNotFoundError as error:
  print("That file was not found :(") 