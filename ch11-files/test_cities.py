# from name_function import get_formatted_name
from city_functions import get_formatted_city_country

def test_city_country_name():
    """Do city and country like Santiago Chile work?"""
    formatted_name = get_formatted_city_country('santiago', 'chile')
    assert formatted_name == 'Santiago Chile'