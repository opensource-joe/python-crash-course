# # variables, strings
# name = "ada lovelace"
# first_name = "joe"
# last_name = "castle"
# # use f for format to replace name of variable in braces with its value
# full_name = f"{first_name} {last_name}"
# favorite_language = "python "
# nostarch_url = "https://nostarch.com"

# # title case = variable.title()
# print(name.title())

# # upper case = variable.upper()
# print(name.upper())

# # lower case = variable.lower()
# print(name.lower())

# # using variables in a string
# print(full_name)
# print(full_name.title())

# # example with f string
# print(f"Hello, {full_name.title()}!")

# # adding line breaks (\n)
# print("Languages:\nPython\nC\nJavascript")

# # adding line breaks (\n) and tabs (\t)
# print("Languages:\n\tPython\n\tC\n\tJavascript")

# # stripping whitespace, can use .rstrip(), .lstrip(), .strip()
# print(favorite_language)
# print(favorite_language.rstrip())

# # removing prefixes = .removeprefix()
# noprefix_nostarch_url = nostarch_url.removeprefix("https://")
# print(noprefix_nostarch_url.removesuffix(".com"))

# zen of python - place in interpreter
# import this

# -------------------------------
# Exercises

# 2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

# name = "Eric"
# print(f"Hello {name}, would you like to learn some Python today?")

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

# name = "eric"
# print(name.upper(), "\n" + name.lower(), "\n" + name.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:

# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

# famous_person = "albert einstein"
# famous_quote = "A person who never made a mistake never tried anything new."
# print(f'{famous_person.title()} once said, "{famous_quote}"')

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.

# famous_person = "albert einstein"
# famous_quote = "A person who never made a mistake never tried anything new."
# sentence = (f'{famous_person.title()} once said, "{famous_quote}"')
# print(sentence)

# 2-7. Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. # Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

# name = "  joe  "
# print(name.rstrip())
# print("\t" + name.lstrip())
# print("\n" + name.strip())

# 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

# filename = "python_notes.txt"
# print(filename.removesuffix('.txt'))

# 2-9. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results. You should create four lines that look like this:

# print(5+3)
# print(10-2)
# print(2*4)
# print(16/2)

# 2-10. Favorite Number: Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message.

# favorite_number = 13
# print(f"{favorite_number} is my favorite number.")