class Car:

  wheels = 4 #* global variable

  def __init__(self, make, model, year, color):
    #* instance variables
    self.make = make
    self.model = model
    self.year = year
    self.color = color

  def drive(self):
    print("This {} is running.".format(self.model))

  def stop(self):
    print("This {} is stopped.".format(self.model))


# car_1 = Car("Ford", "Mustang", 1996, "red")

# car_2 = Car("Honda", "City", 2023, "grey")

# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)

# car_2.drive()
# car_2.stop()