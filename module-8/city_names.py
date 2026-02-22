def city_country(city, country):
    return f"{city.title()}, {country.title()}"

city = city_country("rome", "italy")
print(city)

city = city_country("london", "england")
print(city)

city = city_country("dublin", "ireland")
print(city)