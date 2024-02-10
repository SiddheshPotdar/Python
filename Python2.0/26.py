animal = "Cow"
item = "Moon"

# print("The {} jumped over the {}.".format(animal, item))
# print("The {} jumped over the {}.".format(item, animal))
# print("The {1} jumped over the {0}.".format(item, animal))

# print("The {animal} jumped over the {item}.".format(animal = "Cow", item = "Moon"))


# text = "The {} jumped over the {}."
# print(text.format(animal, item))

#* padding
name = 'Bro'
# print("Hello, my name is {:10}.".format(name))
# print("Hello, my name is {:<10}.".format(name))
# print("Hello, my name is {:>10}.".format(name))
# print("Hello, my name is {:^10}.".format(name))

# number = 3.2345
number = 1200
print("The number is {:.2f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number)) #binary
print("The number is {:o}".format(number)) #ocatal
print("The number is {:x}".format(number)) #hexadecimal
print("The number is {:E}".format(number)) #scientific
print("The number is {:e}".format(number)) #scientific