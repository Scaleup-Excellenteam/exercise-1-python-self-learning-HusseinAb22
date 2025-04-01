"""
Processes a text string and returns a dictionary of words (alphabetic only) with their lengths.

- Converts text to lowercase.
- Removes non-letter characters from each word.
- Ignores empty results.

Returns:
- dict: {word: length} for all cleaned words in the input text.
"""


def long_cat_is_long(text):
    text = text.lower()
    cleaned_words = [''.join(ch for ch in word if ch.isalpha()) for word in text.split()]
    return {word: len(word) for word in cleaned_words if not word == ''}


if __name__ == '__main__':
    print(long_cat_is_long("Bla bla bla tra lala 123"))
