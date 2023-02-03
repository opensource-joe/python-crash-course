# dictionary example
# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# --------

# adding new key-value pairs
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# --------

# starting with an empty dictionary
# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

# --------

# modifying values in a dictionary
# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")

# --------

# modifying values - a more interesting example
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# # the new position is the old position plus one increment
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")

# --------

#  removing key-value pairs, "del" permanently deletes the key-value pair
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)

# --------

# a dictionary of similar objects
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# --------

# using get() to access values
# alien_0 = {'color': 'green', 'speed': 'slow'}

# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }

# for key, value in user_0.items():
#     print(f"Key/value: {key} {value}")

# --------

# looping through a dictionary's keys in a particular order

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# --------

# looping through all values in a dictionary with values()
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

# --------

# using set() to remove repetitive values
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for language in set(favorite_languages.values()):
#     print(language.title())

# --------

# nesting - can nest dictionaries inside dictionaries and lists
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': '15'}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# --------

# using code to automatically generate dictionary values - range()

# make an empty list for storing aliens
# aliens = []

# make 30 green aliens
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# # show the first 5 aliens
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# # show how many aliens have been created
# print(f"Total number of aliens: {len(aliens)}.")

# --------

# changing values in the list that is generated with range()

# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10

# for alien in aliens[:5]:
#     print(alien)
# print("...")

# print(f"Total number of aliens: {len(aliens)}.")

# --------

# add an elif to account for red alien values

# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15

# for alien in aliens[:5]:
#     print(alien)
# print("...")

# print(f"Total number of aliens: {len(aliens)}.")

# --------

# a list in a dictionary
# store information about a pizza being ordered
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }

# # summarize the order, notice the line break - space w/ quote
# print(f"You ordered a {pizza['crust']}-crust pizza "
#       "with the following toppings:")

# for topping in pizza['toppings']:
#     print(f"\t{topping}")

# --------

# another example of lists within a dictionary
# favorite_languages = {
#     'jen': ['python', 'rust'],
#     'sarah': ['c'],
#     'edward': ['rust', 'go'],
#     'phil': ['python', 'haskell'],
#     'abe': ['python'],
# }

# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite language are:")
#     for language in languages:
#         print(f"\t{language.title()}")

# develop an "if" statement to print "{name}'s favorite languages are" or "{name}'s favorite language is" depending on language value length

# --------

# dictionary in a dictionary


# -------------------------------
# Exercises

# 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

# person = {
#     'first_name': 'joe',
#     'last_name': 'castle',
#     'age': 47,
#     'city': 'dc',
# }

# print(person['first_name'].title(), person['last_name'].title(), person['age'], person['city'].upper())

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

# favorite_numbers = {
#     'steve': 4,
#     'joe': 13,
#     'melissa': 7,
#     'amy': 5,
#     'alyson': 2,
# }

# print(favorite_numbers['steve'], favorite_numbers['joe'], favorite_numbers['melissa'], favorite_numbers['amy'], favorite_numbers['alyson'])

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

# glossary = {
#     'concatenation': 'and',
#     'comment': 'hash',
#     'get': 'missing value',
#     'float': 'decimal',
#     'integer': 'number',
# }

# can use glossary.keys() and glossary.values() to print specific key and value elements
# print(glossary)

# for value in glossary.keys():
#     print(value, "==", glossary[value])

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

# glossary = {
#     'concatenation': 'and',
#     'comment': 'hash',
#     'get': 'missing value',
#     'float': 'decimal',
#     'integer': 'number',
#     'number' : 'value',
# }

# for key, value in glossary.items():
#     print(f"Key/value: {key} : {value}")

# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

# rivers = {
#     'nile': 'egypt',
#     'mississippi': 'america',
#     'panama': 'south america',
# }

# for key, value in rivers.items():
#     print(f"The {key.title()} runs through {value.title()}.")
    
# for key in rivers.keys():
#     print(f"These are the rivers: {key.title()}.")

# for value in rivers.values():
#     print(f"These are the countries: {value.title()}.")

# 6-6. Polling: Use the code in favorite_languages.py (page 96).
# Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# need_languages = ['steve', 'jen']

# for user in need_languages:
#     if user.lower() in favorite_languages.keys():
#         print(f"Thank you for responding, {user.title()}.")
#     else:
#         print(f"Please take the favorite language poll, {user.title()}") 