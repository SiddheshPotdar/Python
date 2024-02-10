names = ['Tommy', 'Bob', 'Rhea']
passwords = ['tom@123', 'booo', 'R333']

users = dict(zip(names, passwords))

# print(type(users))

for key, value in users.items():
  print(key + ': ' + value)