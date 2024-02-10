# utensils = {"spoon", "fork", "dish"}
utensils = {"spoon", "fork", "knife"}
dishes = {"plate", "bowl", "cup", "knife"}

# utensils.add("knife")
# utensils.remove("spoon")
# utensils.clear()

# utensils.update(dishes)

# for x in utensils:
  # print(x)

dinner_table = utensils.union(dishes)

# for x in dinner_table:
  # print(x)

print(dishes.intersection(utensils))
print(dishes.difference(utensils))

