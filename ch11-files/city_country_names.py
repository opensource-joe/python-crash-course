from city_functions import get_formatted_city_country

print("Enter 'q' at any time to quit.")
while True:
    city = input("Please give me a city name: ")
    if city == 'q':
        break
    country = input("Please give me a country name: ")
    if country == 'q':
        break
    
formatted_name = get_formatted_city_country(city, country)
print(f"Neatly formatted name: {formatted_name}.")