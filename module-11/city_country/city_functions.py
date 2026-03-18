def city_country(city, country, population=None):
    """Return a string of the form 'City, Country'."""
    city_country_string = f"{city.title()}, {country.title()}" 
    if population:
        city_country_string += f" - population {population}"

    return city_country_string

