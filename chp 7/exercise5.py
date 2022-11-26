def describe_city(city, country='UAE'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Dubai')
describe_city('Burj khalifa', 'Dubai Mall')
describe_city('Coca Cola arena')