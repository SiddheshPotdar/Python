
friends = [
  ('Rachel', 19),
  ('Monica', 18),
  ('Phoeba', 17),
  ('Joey', 16),
  ('Candler', 21),
  ('Ross', 20)
]


age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
  print(i)