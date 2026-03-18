from city_functions import city_country

def test_city_country():
    """Test for the function city_country()."""
    test_city = city_country('santiago', 'chile')
    assert test_city == 'Santiago, Chile'

def test_city_country_population():
    """Test for the function city_country() with population."""
    test_city = city_country('santiago', 'chile', population=5000000)
    assert test_city == 'Santiago, Chile - population 5000000'