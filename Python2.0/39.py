from car import Car 

car_1 = Car('Skoda', 'Slavia', 2022, 'Blue')

car_2 = Car("Volksvagen", "Virtus", 2023, 'White')

# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

# car_1.drive()
# car_1.stop()

# car_2.wheels = 3
Car.wheels = 5

print(car_1.wheels)
print(car_2.wheels)