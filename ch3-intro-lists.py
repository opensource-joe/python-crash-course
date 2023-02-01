# A list is a collection of items in a particular order. Anything can be put in a list, the items in the list don't have to be related in any particular way. 
# A list usually contains more than one element, it's a good idea to make the name of your list plural. 
# Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired.

# motorcycles = ["honda", "yamaha", "suzuki"]

# list
# bicycles = ["trek", "cannondale", "redline", "specialized"]
# print(bicycles)

# access list item with variable name followed by index = bicycles[0]
# print(bicycles[0])

# access the last item in the list, second to last, and so on
# print(bicycles[-1])
# print(bicycles[-2])

# using individual values from a list
# message = f"My first bicycle was a {bicycles[0].title()}"
# print(message)

# modifying elements in a list
# motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles)
# motorcycles[0] = "ducati"
# print(motorcycles)

# add a new element to the end of a list = variable.append()
# motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles)
# motorcycles.append("ducati")
# print(motorcycles)

# append allows for populating empty lists
# motorcycles = []
# motorcycles.append("honda")
# motorcycles.append("ducati")
# motorcycles.append("harley davidson")
# print(motorcycles)

# insert new elements into a list = variable.insert(index, "item")
# motorcycles.insert(2, "triumph")
# print(motorcycles)

# remove item from list with index number (if know position, use del) = del variable[index]
# del motorcycles[2]
# print(motorcycles)

# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# With pop(), consider last in/first out
# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}.")
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")
# print(motorcycles)

# When don't know index number, use the value to remove = variable.remove("value")
# print(motorcycles)
# motorcycles.remove("yamaha")
# print(motorcycles)

# Can use the value of what's being removed
# print(motorcycles)

# too_expensive = "yamaha"
# motorcycles.remove(too_expensive)
# print(motorcycles)

# print(f"\nA {too_expensive.title()} is too expensive for me.")

# permanently sort a list alphabetically = variable.sort()
# cars = ["bmw", "audi", "toyota", "subaru"]
# cars.sort()
# print(cars)

# can sort if reverse alphabetic order too = variable.sort(reverse=True)
# cars.sort(reverse=True)
# print(cars)

# sort list temporarily with a sorted function = sorted(variable)
# print("Here is the original list")
# print(cars)
# print("\nHere is the temporary sorted list")
# print(sorted(cars))
# print("\nHere is the temporary reverse sorted list")
# print(sorted(cars, reverse=True))
# print("\nHere is the original list")
# print(cars)

# use reverse() to reverse order of list but not alphabetize
# print(cars)
# cars.reverse()
# print(cars)

# find the length of a list = len(variable)
# print(len(cars))

# -------------------------------
# Exercises

# 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

# names = ["Joe", "Anthony", "Dave", "Matt"]
# print(f"{names[0]} \n{names[1]} \n{names[2]} \n{names[3]}")

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

# names = ["Joe", "Anthony", "Dave", "Matt"]
# print(f"Good to see you, {names[0]}.", f"\nGood to see you, {names[1]}.", f"\nGood to see you, {names[2]}.", f"\nGood to see you, {names[3]}.")

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

# cars = ["Mustang", "4Runner", "Highlander"]
# print(f"I would like to have a Ford {cars[0]}. If not, then a Toyota {cars[1]}.")

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

# dinner_invites = ["stevie ray vaughn", "john mayer", "eric clapton"]
# print(f"{dinner_invites[0].title()}, please join me for dinner.")
# print(f"{dinner_invites[1].title()}, please join me for dinner.")
# print(f"{dinner_invites[2].title()}, please join me for dinner.")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

# 1. Start with your program from Exercise 3-4. 

# dinner_invites = ["stevie ray vaughn", "john mayer", "eric clapton"]
# print(dinner_invites)

# 2. Add a print() call at the end of your program, stating the name of the guest who can’t make it.

# declined_invite = dinner_invites.pop(1)
# print(declined_invite)

# 3. Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

# dinner_invites.insert(2, "buddy guy")
# print(dinner_invites)

# 4. Print a second set of invitation messages, one for each person who is still in your list.

# print(f"{dinner_invites[0].title()}, please join me for dinner.")
# print(f"{dinner_invites[1].title()}, please join me for dinner.")
# print(f"{dinner_invites[2].title()}, please join me for dinner.")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

# dinner_invites = ["stevie ray vaughn", "john mayer", "eric clapton"]
# print(dinner_invites)

# dinner_invites.insert(0, "buddy guy")
# dinner_invites.insert(2, "dave koz")
# dinner_invites.insert(5, "gary clark jr")
# print(dinner_invites)

# print(f"{dinner_invites[0].title()}, please join me for dinner.")
# print(f"{dinner_invites[1].title()}, please join me for dinner.")
# print(f"{dinner_invites[2].title()}, please join me for dinner.")
# print(f"{dinner_invites[3].title()}, please join me for dinner.")
# print(f"{dinner_invites[4].title()}, please join me for dinner.")
# print(f"{dinner_invites[5].title()}, please join me for dinner.")

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.

# 1. Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.

# print("Unfortunately, my table is too small and I can only invite two people to dinner.")

# 2. Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

# guest_six = dinner_invites.pop()
# print(dinner_invites)
# print(f"Sorry {guest_six.title()}, I have limited space.")

# guest_five = dinner_invites.pop()
# print(dinner_invites)
# print(f"Sorry {guest_five.title()}, I have limited space.")

# guest_four = dinner_invites.pop()
# print(dinner_invites)
# print(f"Sorry {guest_four.title()}, I have limited space.")

# guest_three = dinner_invites.pop()
# print(dinner_invites)
# print(f"Sorry {guest_three.title()}, I have limited space.")

# print(dinner_invites)

# 3. Print a message to each of the two people still on your list, letting them know they’re still invited.

# print(f"{dinner_invites[0].title()}, you are still invited to dinner.")
# print(f"{dinner_invites[1].title()}, you are still invited to dinner.")

# 4. Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

# del dinner_invites[1]
# del dinner_invites[0]
# print(dinner_invites)

# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.

# 1. Store the locations in a list. Make sure the list is not in alphabetical order. Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.

# locations = ["italy", "uk", "canada", "caribbean"]
# print(locations)

# 2. Use sorted() to print your list in alphabetical order without modifying the actual list. Show that your list is still in its original order by printing it.

# print(sorted(locations))
# print(locations)

# 3. Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list. Show that your list is still in its original order by printing it again.

# print(sorted(locations, reverse=True))
# print(locations)

# 4. Use reverse() to change the order of your list. Print the list to show that its order has changed.

# locations.reverse()
# print(locations)

# 5. Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

# locations.reverse()
# print(locations)

# 6. Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

# locations.sort()
# print(locations)

# 7. Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.

# locations.sort(reverse=True)
# print(locations)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42), use len() to print a message indicating the number of people you’re inviting to dinner.

# dinner_invites = ["stevie ray vaughn", "john mayer", "eric clapton"]
# print(len(dinner_invites))

# 3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

# mountains = ["blue ridge", "shed", "catoctin"]
# print(len(mountains))