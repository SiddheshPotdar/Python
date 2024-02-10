foods = ["pizza", "hamburger", "hotdog", "sphagetti", "cheese"]

# print(foods[0])
# foods[0] = "ice-cream"
# print(foods[0])

# for food in foods:
#   print(food)

foods.append("ice-cream")
foods.remove("hotdog")
foods.insert(1, "cake")
foods.sort()
foods.clear()

for food in foods:
  print(food)
