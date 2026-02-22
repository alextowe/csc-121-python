def describe_city(city, country='The United States'):
    """Print a simple statement about a city."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('asheville')
describe_city('new york')
describe_city('dublin', 'ireland')