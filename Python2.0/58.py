# dictionary  = {key: expression for {key, value} in iterable}

# cities_in_F = {'Mumbai': 32, 'Delhi': 75, 'Kolkata': 100, 'Banglore': 50}

# cities_in_C = {key: round((value - 32)*(5/9)) for (key, value) in cities_in_F.items()}

# print(cities_in_C)


weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los angleles': 'sunny', 'Chicago': 'cloudy'}

sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}

print(sunny_weather) 