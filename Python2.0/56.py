import functools

letters = ['H', 'E', 'L', 'L', 'O']

word = functools.reduce(lambda x, y: x + y, letters)

# print(word)

nums = [5, 4, 3, 2, 1]
factorial = functools.reduce(lambda x, y: x * y, nums)

print(factorial)