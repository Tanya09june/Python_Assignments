cities = []
for i in range(5):
    city_name = input(f"Enter the name of city {i+1}: ")
    cities.append(city_name)
print("\nThe cities you entered are:")
for city in cities:
    print(city)