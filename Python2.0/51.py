# higher order functions = a function that either:
# 1 accepts a function as argument
# 2 return a function

#! 1
# def loud(text):
#   return text.upper()

# def quiet(text):
#   return text.lower()

# def hello(func):
#   text = func("Hello")
#   print(text)

# hello(loud)
# hello(quiet)

#! 2
def divisor(x):
  def dividend(y):
    return y / x
  return dividend

divide = divisor(4)
print(divide(40))