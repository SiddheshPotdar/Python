import random

# x = random.randint(1,10)
# y = random.random()
# print(x)
# print(y)

# myList = ['rock', 'paper', 'scisor']
# z = random.choice(myList)
# print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)