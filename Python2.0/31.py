text = "Hello!\nThis is newly created file.\n32"

with open("demo\\new.txt", 'w') as file:
  file.write(text)

#! append text to file
with open("demo\\new.txt", 'a') as file:
  file.write("This line is added later to the file.\n")