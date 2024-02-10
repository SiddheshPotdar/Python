# map() = applies a function to each item in iterable

store = [
  ('Shirt', 300),
  ('Jeans', 550),
  ('Saree', 1000),
  ('Sweatshirt', 675)
]

to_dollars = lambda data: (data[0], data[1] * 80)

store_dollars = list(map(to_dollars, store))

price = lambda prices: prices[1]
sorted_store = sorted(store_dollars, key = price)

for i in sorted_store:
  print(i)