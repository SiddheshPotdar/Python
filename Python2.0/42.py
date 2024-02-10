#mulitple inheritance

class Prey:
  
  def flee(self):
    print("This animal flees.")

class Predator:

  def hunt(self):
    print("Thsi animal hunts.")

class Lion(Predator):
  
  pass

class Deer(Prey):

  pass

class Fish(Predator, Prey):

  pass


deer = Deer()
lion = Lion()
fish = Fish()

deer.flee()
lion.hunt()
fish.flee()
fish.hunt()