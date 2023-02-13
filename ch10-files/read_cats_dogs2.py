from pathlib import Path

def print_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        # count the appropriate number of words in the file
        words = contents.split()
        print(words)

filenames = ['cats.txt', 'dogs.txt', 'fake.txt']
for filename in filenames:
    path = Path('ch10-files/', filename)
    print_words(path)