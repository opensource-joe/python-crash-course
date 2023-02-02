# Looping is important because it's one of the most common ways a computer automates repetitive tasks.

# looping example
# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(magician)

# doing more with looping
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")

# include as many lines as you want in a loop
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")

# range makes it easy to generate a list of numbers = range()
# for value in range(1, 5):
#     print(value)
# for value in range(6):
#     print(value)

# wrap list around a call to the range() to generate a list of numbers
# numbers = list(range(1, 6))
# print(numbers)

# pass a third number in range() to designate a step
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# create almost any set of numbers using range()
# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# can also write the above range() code as the following
# squares = []
# for value in range(1, 11):
#     squares.append(value**2)
# print(squares)

# python functions are helpful when working with lists for simple statistics
# numbers = list(range(1, 6))
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# a list comprehension allows for generating a list in one line of code
# squares = [value**2 for value in range(1, 11)]
# print(squares)

# slicing a list by specifying the first and last index = variable[1:3]
# players = ["charles", "martina", "michael", "florence", "eli"]
# print(players[0:3])

# omit first value by not including before colon to start at the beginning of the list
# players = ["charles", "martina", "michael", "florence", "eli"]
# print(players[:4])

# omit last index value by not including after colon to include the end of the list
# players = ["charles", "martina", "michael", "florence", "eli"]
# print(players[2:])

# use negative numbers to identify values at the end of the list
# players = ["charles", "martina", "michael", "florence", "eli"]
# print(players[-3:])

# third value in a slice tells python how many steps to skip between items
# players = ["charles", "martina", "michael", "florence", "eli"]
# print(players[0:2:2])

# looping through a slice
# players = ["charles", "martina", "michael", "florence", "eli"]

# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())

# copying a list with slice by omitting the first and last index = ([:])
# my_foods = ["pizza", "falafal", "carrot cake"]
# friend_foods = my_foods[:]

# my_foods.append("cannoli")
# friend_foods.append("ice cream")

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
# Tuples look just like a list but instead of using [], you use (), also called dimensions.
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# looping over a tuple
# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)

# writing over a tuple: although you can't modify a tuple, you can assign a new value to a variable that represents a tuple
# dimensions = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)

# -------------------------------
# Exercises

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

# pizzas = ["cheese", "pepperoni", "sausage", "veggie"]
# for pizza in pizzas:
#     print(pizza)

# 1. Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.

# for pizza in pizzas:
#     print(f"I like {pizza} pizza.")

# 2. Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

# for pizza in pizzas:
#     print(f"I like {pizza} pizza.")
# print("I really love pizza!")

# 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

# animals = ["giraffe", "cow", "pelican"]
# for animal in animals:
#     print(animal)

# 1. Modify your program to print a statement about each animal, such as A dog would make a great pet.

# for animal in animals:
#     print(f"A {animal} would be a great pet.")

# 2. Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!

# for animal in animals:
#     print(f"A {animal} would be a great pet.")
# print("Any of these animals would be a great pet!")

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

# for value in range(1, 21):
#     print(value)

# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

# values = list(range(1, 1_000_000))
# for value in values:
#     print(value)

# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

# values = list(range(1, 1_000_001))
# print(min(values))
# print(max(values))
# print(sum(values))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

# values = list(range(1, 20, 2))
# for value in values:
#     print(value)

# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

# values = list(range(3, 30, 3))
# for value in values:
#     print(value)

# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

# cubes = []
# for value in range(1, 10):
#     cubes.append(value**3)
# print(cubes)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

# cubes = [value**3 for value in range(1, 10)]
# print(cubes)

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

# pizzas = ["cheese", "pepperoni", "sausage", "veggie", "everything"]

# 1. Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.

# print("The first three items in the list are:")
# print(pizzas[:3])

# 2. Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.

# print("Three items from the middle of the list are:")
# print(pizzas[1:4])

# 3. Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

# print("The last three items in the list are:")
# print(pizzas[2:])

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

# my_pizzas = ["cheese", "pepperoni", "sausage", "veggie", "everything"]
# friend_pizzas = my_pizzas[:]

# 1. Add a new pizza to the original list.

# my_pizzas.append("hawaiian")

# 2. Add a different pizza to the list friend_pizzas.

# friend_pizzas.append("spicy sausage")

# 3. Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

# print("My favorite pizzas are:")
# for pizza in my_pizzas:
#     print(pizza)

# print("\nMy friend's favorite pizzas are:")
# for pizza in friend_pizzas:
#     print(pizza)

# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

# pizzas = ["cheese", "pepperoni", "sausage", "veggie", "everything"]
# foods = ["pizza", "falafal", "carrot cake"]

# for pizza in pizzas:
#     print(pizza)

# for food in foods:
#     print(food)

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

# foods = ("pizza", "falafal", "hamburger", "cheeseburger", "french fries")

# 1. Use a for loop to print each food the restaurant offers.

# print("The restaurant offers the following foods:")
# for food in foods:
#     print(food)

# 2. Try to modify one of the items, and make sure that Python rejects the change.

# foods[0] = "error"

# 3. The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

# print(foods)

# foods = ("pizza", "falafal", "soda", "cheeseburger", "toast")
# for food in foods:
#     print(food)