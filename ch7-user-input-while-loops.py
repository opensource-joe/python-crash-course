# how the input() function works
# message = input("Tell me something, and I will repeat it back to you.")
# print(message)

# --------

# writing clear prompts
# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

# --------

# writing a prompt that's longer than one line
# prompt = "If you share your name, we can personalize the message you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"\nHello {name}!")

# --------

# using int() to accept numerical input
# age = input("How old are you? ")

# age = int(age)
# print(age)

# --------

# another int() example
# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# --------

# modulo operator - divides one number by another and returns remainder
# number = input("Enter a number, and I'll tell you if it's even or odd. ")
# number = int(number)

# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# --------

# while loop in action
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     # short hand for current_number = current_number + 1
#     current_number += 1

# --------

# letting the user choose when to quit
# prompt = "\nTell me something and I will repeat it back to you. "
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)
    
#     if message != 'quit':
#         print(message)

# --------

# using a flag as a variable to determine if the program is active
# prompt = "\nTell me something and I will repeat it back to you. "
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     message = input(prompt)
    
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# --------

# using a break to exit a loop
# prompt = "\nPlease enter the name of a city you have visited. "
# prompt += "\nEnter 'quit' when you are finished. "

# while True:
#     city = input(prompt)
    
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# --------

# using continue in a loop
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
    
#     print(current_number)    

# --------

# moving items from one list to another

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
    
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
    
# print(f"\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# --------

# removing all instances of specific values from a list
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# --------

# # filling a dictionary with user input
# responses = {}

# # set a flag that polling is active
# polling_active = True
# while polling_active:
#     # prompt for person's name and response
#     name = input("\nWhat is your name? ")
#     response = input("\nWhich mountain would you like to climb someday? ")
    
#     # store the response in the dictionary
#     responses[name] = response
    
#     # find out anyone else is going to take the poll
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False

# # polling is complete, show the results
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb mount {response}.")


# -------------------------------
# Exercises

# 7-1. Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”

# car = input("What kind of car would you like to drive? ")
# print(f"Let me see if I can find you a {car}.")

# 7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

# number = input("How many people are in your party? ")
# number = int(number)

# if number >= 8:
#     print("You will have to wait for your table to be ready.")
# else:
#     print("Your table is ready!")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

# number = input("Enter a number, and I'll tell you if it's a multiple of ten. ")
# number = int(number)

# if number % 10 == 0:
#     print(f"The number {number} is a multiple of ten.")
# else:
#     print(f"The number {number} is not a multiple of ten.")

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

# prompt = "\nWhich pizza toppings would you like on your pizza? "
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     topping = input(prompt)
    
#     if topping == 'quit':
#         active = False
#     else:
#         print(f"We'll add {topping} to your pizza.")

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

# under the age < 3 charge 0
# <= 3 and >= 12 charge 10
# >= 13 charge 15
# loop asking age, then tell the cost of the movie ticket

# prompt = "\nEnter your age to receive ticket price? "
# prompt += "\nEnter 'quit' to end the program. "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)

#     if age < 3:
#         print("  You get in free!")
#     elif age < 13:
#         print("  Your ticket is $10.")
#     else:
#         print("  Your ticket is $15.")

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:

# version #1 - conditional test in the while statement to stop the loop
# current_number = 1
# while current_number <= 10:
#     print(current_number)
#     # short hand for current_number = current_number + 1
#     current_number += 1

# version #2 - active variable to control how long the loop runs
# prompt = "\nWhich pizza toppings would you like on your pizza? "
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     topping = input(prompt)
    
#     if topping == 'quit':
#         active = False
#     else:
#         print(f"We'll add {topping} to your pizza.")

# version #3 - using a break statement to exit the loop when user enters a 'quit' value
# prompt = "\nEnter you height in inches by number only? "
# prompt += "\nEnter 'quit' to end the program. "

# while True:
#     height = input(prompt)
#     if height == 'quit':
#         break
#     height = int(height)
    
#     if height < 60:
#         print("You are short!")
#     else:
#         print("You are tall!")

# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press CTRL-C or close the window displaying the output.)
# current_number = 1
# while current_number <= 10:
#     print(current_number)

# missing the counter to make the previous loop stop
    # # short hand for current_number = current_number + 1
    # current_number += 1

# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

# sandwich_orders = ['turkey', 'club', 'roast beef', 'ham', 'tuna']
# finished_sandwiches = []

# while sandwich_orders:
#     order = sandwich_orders.pop()

#     print(f"I made your {order}.")
#     finished_sandwiches.append(order)

# print(f"\nThe following sandwiches have been created:")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

# sandwich_orders = ['turkey', 'pastrami', 'club', 'pastrami', 'roast beef', 'ham', 'pastrami', 'tuna']
# finished_sandwiches = []
# print(sandwich_orders)

# print("The deli has run out of pastrami.")

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print(sandwich_orders)

# while sandwich_orders:
#     order = sandwich_orders.pop()

#     print(f"I made your {order}.")
#     finished_sandwiches.append(order)

# print(f"\nThe following sandwiches have been created:")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)

# 7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

# responses = {}

# # set a flag that polling is active
# polling_active = True
# while polling_active:
#     # prompt for favorite vacation idea
#     name = input("\nWhat is your name? ")
#     response = input("\nWhat is your favorite vacation type? ")
    
#     # store the response in the dictionary
#     responses[name] = response
    
#     # find out anyone else is going to take the poll
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False

# # polling is complete, show the results
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name}'s favorite vacation type is {response}.")