try: 
  numerator = int(input("Enter a number to divide : "))
  denominator = int(input("Enter a number to divide : "))
  result = numerator / denominator
except ZeroDivisionError as error:
  print(error)
  print("You cant divide by zero.")
except ValueError as error:
  print(error)
  print("Enter a number only")
else : 
  print(result)
finally:
  print("this always execute")
