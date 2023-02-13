from pathlib import Path

def print_words(path):
    """Print out cats and dogs from txt files."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # print the names of all cats and dogs
        words = contents.split() 
        print(words)

filenames = ['cats.txt', 'dogs.txt', 'fake.txt']
for filename in filenames:
    path = Path('ch10-files/', filename)
    print_words(path)