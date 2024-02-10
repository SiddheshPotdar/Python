class Car:

  def turn_on(self):
    print("You start the engine.")
    return self

  def drive(self):
    print("You drive the car.")
    return self

  def brake(self):
    print("You apply the brakes")
    return self

  def turn_off(self):
    print("You turn off the car.")
    return self

car = Car()

# car.turn_on()
# car.drive()

# car.turn_on().drive().brake().turn_off()

car.turn_on()\
  .drive()\
    .brake()\
      .turn_off()