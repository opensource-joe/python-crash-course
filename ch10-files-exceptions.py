# import statements
# pathlib import to read contents from a file
# from pathlib import Path

# -------------------------------

# reading contents from a file - pathlib import cited above
# path = Path('ch10-files/pi_digits.txt')
# # read_text() returns extra line by default, remove with rstrip()
# contents = path.read_text().rstrip()
# print(contents)

# --------

# accessing a file's lines
# path = Path('ch10-files/pi_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
#     print(line)

# --------

# working with a file's contents
# path = Path('ch10-files/pi_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line

# print(pi_string)
# print(len(pi_string))

# --------

# large files: one million digits
# path = Path('ch10-files/pi_million_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line

# print(f"{pi_string[:52]}...")
# print(len(pi_string))

# --------

# is your birthday contained in Pi?
# large files: one million digits
# path = Path('ch10-files/pi_million_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line

# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")

# --------

# writing to a file
# path = Path('ch10-files/programming.txt')
# path.write_text("I love programming.")

# --------

# writing multiple lines
# contents = "I love programming.\n"
# contents += "I love creating new games.\n"
# contents += "I also love working with data.\n"

# path = Path('ch10-files/programming.txt')
# path.write_text(contents)

# --------

# using exceptions to handle crashes
# print("Give me two numbers and I'll dived them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("First number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)

# --------

# the else block
# print("Give me two numbers and I'll dived them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("First number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

# --------

# handling the FileNotFoundError exception
# path = Path('ch10-files/alice.txt')

# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"Sorry, the file {path} does not exist.")

# --------

# analyzing text
# path = Path('ch10-files/alice_new.txt')
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"Sorry, the file {path} does not exist.")
# else:
#     # count the appropriate number of words in the file
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {path} has about {num_words} words.")

# --------

# working with multiple files
# look at word_count_multiple_texts.py and alice_new.txt

# --------

# failing silently
#look at word_count_failing_silently.py and alice_new.txt


# -------------------------------
# Exercises

# 10-1. Learning Python: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. Start each line with the phrase In Python you can. . . . Save the file as learning_python.txt in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote two times: print the contents once by reading in the entire file, and once by storing the lines in a list and then looping over each line.

# # reading entire contents
# path = Path('ch10-files/learning_python.txt')
# # read_text() returns extra line by default, remove with rstrip()
# contents = path.read_text().rstrip()
# print(contents)

# # looping over each line
# path = Path('ch10-files/learning_python.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
#     print(line)

# 10-2. Learning C: You can use the replace() method to replace any word in a string with a different word. Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:

# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# Read in each line from the file you just created, learning_python.txt, and replace the word Python with the name of another language, such as C. Print each modified line to the screen.

# path = Path('ch10-files/learning_python.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
#     line = line.replace('python', 'c')
#     print(line)

# 10-3. Simpler Code: The program file_reader.py in this section uses a temporary variable, lines, to show how splitlines() works. You can skip the temporary variable and loop directly over the list that splitlines() returns:

# for line in contents.splitlines():
# Remove the temporary variable from each of the programs in this section, to make them more concise.

# path = Path('ch10-files/learning_python.txt')
# contents = path.read_text()

# for line in contents.splitlines():
#     print(line)

# 10-4. Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.

# name_prompt = input("Please input your name: ")

# path = Path('ch10-files/guest.txt')
# path.write_text(name_prompt)

# 10-5. Guest Book: Write a while loop that prompts users for their name. Collect all the names that are entered, and then write these names to a file called guest_book.txt. Make sure each entry appears on a new line in the file.

# path = Path('ch10-files/guest.txt')

# prompt = "\nHi, what's your name? "
# prompt += "\nEnter 'quit' if you're the last guest. "

# guest_names = []
# while True:
#     name = input(prompt)
#     if name == 'quit':
#         break

#     print(f"Thanks {name}, we'll add you to the guest book.")
#     guest_names.append(name)

# # Build a string where "\n" is added after each name.
# file_string = ''
# for name in guest_names:
#     file_string += f"{name}\n"

# path.write_text(file_string)

# 10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

# try:
#     first_number = input("Give me a number: ")
#     first_number = int(first_number)

#     second_number = input("Give me another number: ")
#     second_number = int(second_number)
# except ValueError:
#     print("Sorry, I really needed a number.")
# else:
#     sum = first_number + second_number
#     print(f"The sum of {first_number} and {second_number} is {sum}.")

# 10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop so the user can continue entering numbers, even if they make a mistake and enter text instead of a number.

# print("Give me two numbers and I'll dived them.")
# print("Enter 'q' to quit.")

# while True:
#     try:
#         first_number = input("First number: ")
#         if first_number == 'q':
#             break
#         first_number = int(first_number)

#         second_number = input("Second number: ")
#         if second_number == 'q':
#             break
#         second_number = int(second_number)
        
#     except ValueError:
#         print("Only numbers")
        
#     else:
#         answer = first_number / second_number
#         print(answer)

# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.




# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail silently if either file is missing.

# 10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org) and find a few texts you’d like to analyze. Download the text files for these works, or copy the raw text from your browser into a text file on your computer.

# You can use the count() method to find out how many times a word or phrase appears in a string. For example, the following code counts the number of times 'row' appears in a string:

# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3

# Notice that converting the string to lowercase using lower() catches all appearances of the word you’re looking for, regardless of how it’s formatted.

# Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. This will be an approximation because it will also count words such as 'then' and 'there'. Try counting 'the ', with a space in the string, and see how much lower your count is.