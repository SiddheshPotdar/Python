# Duck typing

class Duck:

  def walk(self):
    print("This duck is walking.")

  def talk(self):
    print("This duck is quaking.")


class Chicken:

  def walk(self):
    print("This chickeen is walking.")

  def talk(self):
    print("This chicken is cluking.")


class Person:

  def catch(self, duck):
    duck.walk()
    duck.talk()
    print("You caught the duck.")


duck = Duck()
chicken = Chicken() 

person = Person()

person.catch(duck)
person.catch(chicken)