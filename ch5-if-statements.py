# Programming often involves examining a set of conditions and deciding which action to take based on those conditions.

# if and loop example
# cars = ["audi", "bmw", "subaru", "toyota"]

# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())

# case matters in python but you can ignore case when checking for equality with making the value lowercase
# car = 'Audi'
# print(car == 'audi')
# print(car.lower() == 'audi')

# check inequality with !=
# requested_topping = 'mushroom'

# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# testing numerical comparisons
# age = 18
# print(age == 18)

# numerical inequality
# answer = 17
# if answer != 42:
#     print("That is not the correct answer!")

# using "and" to check multiple conditions
# age_0 = 22
# age_1 = 18
# print(age_0 > 21 and age_1 > 21)

# age_1 = 22
# print(age_0 >= 22 and age_1 >= 21)

# using "or" to check multiple conditions
# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 or age_1 >= 21)

# age_0 = 18
# print(age_0 >= 21 or age_1 >= 21)

# checking whether a value is in a list with "in"
# requested_toppings = ['mushrooms', 'onions', 'pineapples']
# print('mushrooms' in requested_toppings)
# print('pepporoni' in requested_toppings)

# checking whether a value is not in a list with "not in"
# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'

# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")

# the simplest kind of "if" statements have one test
# if conditional_test:
#   do something

# age = 19
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote?")

# if-else statement
# age = 17
# if age > 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")

# if-elif-else chain
# age = 12
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $25")
# else:
#     print("Your admission cost is $40.")

# if-elif-else refactored w/ one print statement
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40

# print(f"Your admission cost is ${price}.")

# you can use as many "elif" statements as needed, python does not require a final "else" statement as sometimes it's easier to read another "elif" statement
# age = 65
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age <= 64:
#     price = 40
# elif age >= 65:
#     price = 20

# print(f"Your admission cost is ${price}.")

# use "if-elif-else" if only want one condition to pass, use multiple "if" statements when want to check all conditions
# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
# print("\nFinished making your pizza!")

# In summary, if you want only one block of code to run, use an "if-elif-else" chain. If more than one block of code needs to run, use a series of independent "if" statements.

# checking for special items - using "loop" and "if"
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")
        
# print("\nFinished making your pizza!")

# checking that a list is not empty with "loop" and "if"
# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# using multiple lists
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry, we don't have {requested_topping}.")

# print("\nFinished making your pizza!")

# -------------------------------
# Exercises

# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:

# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')

# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

# 1. Look closely at your results, and make sure you understand why each line evaluates to True or False.
# 2. Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

# True tests
# animal = 'cat'
# print(animal == 'cat')

# number = 5
# print(number > 4)
# print(number >= 4)

# pizza = ['pepperoni', 'cheese', 'sausage']
# print('pepperoni' in pizza)
# print('veggie' != pizza)

# False tests
# animal = 'cat'
# print(animal == 'dog')

# number = 5
# print(number > 6)
# print(number >= 6)

# pizza = ['pepperoni', 'cheese', 'sausage']
# print('veggie' in pizza)
# print('pepperoni' == pizza)

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:

# Tests for equality and inequality with strings

# statement = "this is a statement"
# if statement == "this is a statement":
#     print("the statement is True")
    
# statement = "this is a statement"
# if statement != "this is a statement":
#     print("the statement is True")
# else:
#     print("the statement is False")

# Tests using the lower() method

# car = 'Audi'
# print(car.lower() == 'audi')
# print(car == 'audi')

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to

# guess = 1
# answer = 5
# if guess == answer:
#     print("you guessed it")
# else:
#     print("guess again")

# Tests using the and keyword and the or keyword

# age_0 = 18
# age_1 = 24
# print(age_0 > 17 and age_1 > 21)

# age_1 = 21
# print(age_0 >= 22 and age_1 >= 21)

# Test whether an item is in a list

# requested_toppings = ['mushrooms', 'onions', 'pineapples']
# print('mushrooms' in requested_toppings)
# print('pepporoni' in requested_toppings)

# Test whether an item is not in a list

# requested_toppings = ['mushrooms', 'onions', 'pineapples']
# print('onions' not in requested_toppings)
# print('pepperoni' not in requested_toppings)

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

# alien_color = 'green'

# 1. Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.

# if alien_color == 'green':
#     print("You earned 5 points.")
    
# 2. Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

# if alien_color == 'green':
#     print("You earned 5 points.")
# if alien_color == 'red':
#     print("You earned zero points.")

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
# If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# Write one version of this program that runs the if block and another that runs the else block.

# alien_color = 'green'
# if alien_color == 'green':
#     print("You just earned 5 points for shooting the alien.")
# else:
#     print("You just earned 10 points.")

# alien_color = 'red'
# if alien_color == 'green':
#     print("You just earned 5 points for shooting the alien.")
# else:
#     print("You just earned 10 points.")

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.
# Write three versions of this program, making sure each message is printed for the appropriate color alien.

# alien_color = 'red'
# if alien_color == 'green':
#     print("You just earned 5 points.")
# elif alien_color == 'yellow':
#     print("You just earned 10 points.")
# elif alien_color == 'red':
#     print("You just earned 15 points.")
# else:
#     print("You earned 0 points.")
    
# refactored solution

# alien_color = 'red'
# if alien_color == 'green':
#     points = 5
# elif alien_color == 'yellow':
#     points = 10
# elif alien_color == 'red':
#     points = 15
# else:
#     points = 0

# print(f"You earned {points} points.")

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

# If the person is less than 2 years old, print a message that the person is a baby.
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# If the person is age 65 or older, print a message that the person is an elder.

# age = 40
# if age < 2:
#     stage = 'baby'
# elif age == 2 or age < 4:
#     stage = 'toddler'
# elif age == 4 or age < 13:
#     stage = 'kid'
# elif age == 13 or age < 20:
#     stage = 'teenager'
# elif age == 20 or age < 65:
#     stage = 'adult'
# else: 
#     stage = 'elder'

# print(f"You are a {stage}.")

# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

# Make a list of your three favorite fruits and call it favorite_fruits.
# Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

# favorite_fruits = ['banana', 'star fruit', 'plum']

# if 'banana' in favorite_fruits:
#     print("You really like bananas!")
# if 'orange' in favorite_fruits:
#     print("You really like oranges!")
# if 'plum' in favorite_fruits:
#     print("You really like plums!")

# 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user. If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report? Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.

# usernames = ['sue', 'joseph', 'admin', 'rose', 'dave']

# for username in usernames:
#     if username == 'admin':
#         print(f"Hello {username}, would you like to see a status report?")
#     else:
#         print(f"Hello {username.title()}, thank you for logging in again.")

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty. If the list is empty, print the message We need to find some users! Remove all of the usernames from your list, and make sure the correct message is printed.

# usernames = []

# if usernames:
#     for username in usernames:
#         print(f"Here is {username}.")
# else:
#     print("We need to find some users!")

# 5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# 1. Make a list of five or more usernames called current_users.

# current_users = ['joe', 'alyson', 'jonathan', 'melissa', 'roland']

# 2. Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.

# new_users = ['Roland', 'AMY', 'joe', 'gloria']

# Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available. Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print(f"{new_user.title()} will need to enter a new username.")
#     else:
#         print(f"{new_user.title()} username is still available.")

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

# 1. Store the numbers 1 through 9 in a list.

# values = list(range(1, 10))
# print(values)

# Loop through the list. Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

# for value in values:
#     if value == 1:
#         print(f"{value}st")
#     elif value == 2:
#         print(f"{value}nd")
#     elif value == 3:
#         print(f"{value}rd")
#     else:
#         print(f"{value}th")