
#* positional arguments
def hello(first_name, middle_name, last_name): #order of argument matters
  print("Hello", first_name, middle_name, last_name)

hello("thomas", "elva", "edison")
hello("elva", "edison", "thomas")
hello(last_name="edison", middle_name= "elva", first_name= "thomas")