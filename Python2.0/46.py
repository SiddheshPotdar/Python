from abc import ABC, abstractmethod

class Vehicle(ABC):
  
  @abstractmethod
  def go(self):
    pass

class Car:

  def go(self):
    print("You are driving a car.")

class Bike:

  def go(self):
    print("You are riding a bike.")

# vehicle = Vehicle()

car = Car()
bike = Bike()