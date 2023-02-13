from pathlib import Path

def count_common_words(path, word):
    """Count how many times a word appears in text."""
    path = Path('ch10-files/', filename)
    
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

filename = 'alice_new.txt'
count_common_words(filename, 'the')