# defining a functions
# def greet_user():
#     """Display a simple greeting"""
#     print("Hello!")
    
# greet_user()

# --------

# passing information to a function
# def greet_username(username):
#     """Display a simple greeting by using function parameter"""
#     print(f"Hello, {username.title()}!")

# greet_username('Joe')

# --------

# positional arguments
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"I have a {animal_type}.")
#     print(f"My {animil_type}'s name is {pet_name.title()}.")
    
# describe_pet('hamster', 'harry')

# --------

# multiple function calls
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
    
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# --------

# order matters in positional arguments
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
    
# describe_pet('harry', 'hamster')

# --------

# keyword arguments
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
    
# describe_pet(animal_type='hamster', pet_name='harry')

# --------

# default values
# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet"""
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
    
# describe_pet(pet_name='harry')
# describe_pet(pet_name='harry', animal_type='cat')

# --------

# returning a simple value
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# --------

# making an argument optional
# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

# --------

# making an argument optional continued with "if" statement
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

# --------

# returning a dictionary
# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person"""
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('jimi', 'hendrix')
# print(musician)

# --------

# returning a dictionary expanded
# def build_person(first_name, last_name, age=None):
#     """Return a dictionary of information about a person"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# musician = build_person('jimi', 'hendrix')
# print(musician)

# --------

# using a function with a while loop
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("Please tell me your name: ")
#     print("(enter 'q' at any time to quit)")
    
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
    
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"Hello, {formatted_name}!")

# --------

# passing a list
# def greet_users(names):
#     """Print a simple greeting to each user in the list"""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)
        
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# --------

# modifying a list in a function
# # start with some designs that need to be printed
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # simulate printing each design, until none are left
# # move each design to completed_models after printing
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # display all completed models
# print("The following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model.title())

# --------

# modify previous example into two functions

# first function
# def print_models(unprinted_designs, completed_models):
#     """simulate printing each design, until none are left
#     move each design to completed_models after printing"""

#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# # second function
# def show_completed_models(completed_models):
#     """show all the models that were printed"""
    
#     print("The following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model.title())

# # start with some designs that need to be printed
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# --------

# passing an arbitrary number of arguments

# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested"""
#     print(toppings)
    
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# --------

# loop through arguments

# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested"""
#     print(f"Making a pizza with the following toppings: ")
#     for topping in toppings:
#         print(f"{topping}")
    
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# --------

# mixing positional and arbitrary arguments
# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make"""
#     print(f"Making a {size}-inch pizza with the following toppings: ")
#     for topping in toppings:
#         print(f"{topping}")
    
# make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# --------

# using arbitrary keyword arguments
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)

# --------

# see pizza_module.py and make_pizzas.module.py for module explanation


# -------------------------------
# Exercises

# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

# def display_message():
#     """Display a message"""
#     print("I am learning about functions in Ch8.")
    
# display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

# def favorite_book(title):
#     """Display a message"""
#     print(f"My favorite book is {title.title()}.")
    
# favorite_book('Alice in Wonderland')

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

# def make_shirt(size, text):
#     """Display t-shirt with size and text requests"""
#     print(f"The size requested is {size.upper()}. The print is {text.title()}.")
    
# make_shirt('l', 'born in the usa')

# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

# def make_shirt(size, text):
#     """Display t-shirt with size and text requests"""
#     print(f"The size requested is {size.upper()}. The print is {text.title()}.")
    
# make_shirt('l', 'born in the usa')
# make_shirt(size='l', text='born in the usa')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# def make_shirt(size='l', text='I love Python'):
#     """Display t-shirt with size and text requests"""
#     print(f"The size requested is {size.upper()}. The print is {text.title()}.")
    
# make_shirt()
# make_shirt(size='m')
# make_shirt(size='s', text='born in the America')

# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

# def describe_city(name='Reykjavik', country='Iceland'):
#     """Display city and country"""
#     print(f"{name.title()} is in the {country.title()}.")

# describe_city()
# describe_city('Washington', 'united states')
# describe_city(name='alexandria', country='united states')

# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.

# def describe_city(name='Reykjavik', country='Iceland'):
#     """Display city and country"""
#     print(f"{name.title()}, {country.title()}")

# describe_city()
# describe_city('Washington', 'united states')
# describe_city(name='alexandria', country='united states')

# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album???s dictionary. Make at least one new function call that includes the number of songs on an album.

# def make_album(artist_name, album_title, number_of_songs=None):
#     """Use dictionary to store album information, number_of_songs optional"""
#     album = {'artist_name': artist_name, 'album_title': album_title}
#     if number_of_songs:
#         album['number_of_songs'] = number_of_songs
#     return album

# album_1 = make_album('jimi hendrix', 'bold as love')
# album_2 = make_album('eric clapton', 'slowhand', 10)
# album_3 = make_album('stevie ray vaughn', 'texas flood')

# print(album_1, album_2, album_3)

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album???s artist and title. Once you have that information, call make_album() with the user???s input and print the dictionary that???s created. Be sure to include a quit value in the while loop.

# def make_album(artist_name, album_title):
#     """Use dictionary to store album information, loop for user input"""
#     album = f"{artist_name}, {album_title}"
#     return album.title()

# while True:
#     print("Please tell me your favorite artist and album: ")
#     print("(enter 'q' at any time to quit)")
    
#     artist = input("Artist: ")
#     if artist == 'q':
#         break
    
#     album = input("Album: ")
#     if album == 'q':
#         break

#     user_album = make_album(artist.title(), album.title())
#     print(user_album)

# 8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

# def show_messages(messages):
#     """Print a simple greeting to each user in the list"""
#     for message in messages:
#         msg = f"Text message: {message}."
#         print(msg)
        
# text_messages = ['hello, how are you', 'lol', 'see you tomorrow']
# show_messages(text_messages)

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it???s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

# # first function
# def print_messages(text_messages, sent_messages):
#     """print all messages until none are left - from text_messages to sent_messages"""

#     while text_messages:
#         current_message = text_messages.pop()
#         print(f"Sending message: {current_message}")
#         sent_messages.append(current_message)

# # second function
# def show_sent_messages(sent_messages):
#     """show all the messages that were printed"""

#     print("The following messages have been sent:")
#     for sent_message in sent_messages:
#         print(sent_message.title())

# text_messages = ['hello, how are you', 'lol', 'see you tomorrow']
# sent_messages = []

# print_messages(text_messages, sent_messages)
# show_sent_messages(sent_messages)
    
# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

# # first function
# def show_messages(messages):
#     """Print all messages in the list."""
#     print("Showing all messages:")
#     for message in messages:
#         print(message)

# # second function
# def send_messages(messages, sent_messages):
#     """Print each message, and then move it to sent_messages."""
#     print("\nSending all messages:")
#     while messages:
#         current_message = messages.pop()
#         print(current_message)
#         sent_messages.append(current_message)

# messages = ["hello there", "how are u?", ":)"]
# show_messages(messages)

# sent_messages = []
# send_messages(messages[:], sent_messages)

# print("\nFinal lists:")
# print(messages)
# print(sent_messages)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that???s being ordered. Call the function three times, using a different number of arguments each time.

# def make_sandwich(*toppings):
#     """Print the list of toppings that have been requested"""
#     print(f"Your sandwich includes the following toppings: {toppings}")
    
# make_sandwich('lettuce', 'tomato', 'American cheese')
# make_sandwich('lettuce', 'tomato', 'pickles')
# make_sandwich('lettuce', 'tomato', 'mustard')

# 8-13. User Profile: Start with a copy of user_profile.py from page 148. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.

# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('joseph', 'castle', location='washington', field='open source software', hobby='running')
# print(user_profile)

# 8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that???s returned to make sure all the information was stored correctly.

# def make_car(brand, model, **car_info):
#     """Build a dictionary containing everything we know about a user"""
#     car_info['brand'] = brand
#     car_info['model'] = model
#     return car_info

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)

# 8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

# see printing_functions.py and print_models.py

# 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:

# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

# see pizza_module.py and make_pizzas_module.py

# 8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.

# 1. Functions should have descriptive names, and these names should use lowercase letters and underscores. Descriptive names help you and others understand what your code is trying to do. Module names should use these conventions as well.
# 2. Every function should have a comment that explains concisely what the function does. This comment should appear immediately after the function definition and use the docstring format.
# 3. If you specify a default value for a parameter, no spaces should be used on either side of the equal sign.
# 4. The same convention should be used for keyword arguments in function calls.
# 5. PEP 8 (https://www.python.org/dev/peps/pep-0008) recommends that you limit lines of code to 79 characters so every line is visible in a reasonably sized editor window.
# 6. If your program or module has more than one function, you can separate each by two blank lines to make it easier to see where one function ends and the next one begins.
# 7. All import statements should be written at the beginning of a file. The only exception is if you use comments at the beginning of your file to describe the overall program.