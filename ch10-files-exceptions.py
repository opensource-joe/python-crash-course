# import statements
# pathlib import to read contents from a file
# from pathlib import Path

# pathlib import to read contents from a large file
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
print("Give me two numbers and I'll dived them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)



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