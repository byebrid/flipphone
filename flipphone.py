"""flipphone.py.

Simple script to encode/decode text based on old flipphone keyboard layouts.
"""

NUMPAD = {
    "2": ("A", "B", "C"),
    "3": ("D", "E", "F"),
    "4": ("G", "H", "I"),
    "5": ("J", "K", "L"),
    "6": ("M", "N", "O"),
    "7": ("P", "Q", "R", "S"),
    "8": ("T", "U", "V"),
    "9": ("W", "X", "Y", "Z"),
}

def decode(encoded, char_sep=" ", word_sep=None):
    """Decode phrase from numpad code into alphabetical text
    
    Parameters
    ----------
    encoded: str
        Words should be separated by a '-'. Whitespace should be placed between
        new characters.
    char_sep: str; default=" "
        String that separates each 'character' of `encoded`
    word_sep: str or None: default=None
        String that separates the words in `encoded`. If we don't know how the
        words are separated, it is set to None.
    
    Example
    -------
    >>>decode("444 2 6")
    IAM
    >>>decode("444-2 6", word_sep="-")
    I AM
    """
    if word_sep is not None:
        words = encoded.split(word_sep)
    else:
        words = [encoded]
    
    decoded_words = []
    for word in words:
        decoded_chars = []
        chars = word.split(char_sep)
        for char in chars:
            num_key = char[0]
            decoded_char = NUMPAD[num_key][len(char) - 1]
            decoded_chars.append(decoded_char)
        decoded_word = ''.join(decoded_chars)
        decoded_words.append(decoded_word)

    return ' '.join(decoded_words)

def encode(phrase, input_sep=" ", output_sep="-"):
    """Encode phrase into numpad code
    
    Parameters
    ----------
    phrase: str
        Allowable characters will be A-Z alphabet (upper or lower-case) and
        whitespace
    input_sep: str; default=" "
        String that `phrase`'s words will be separated by.
    word_sep: str; default="-" 
        String that will separate words in the output. I.e. (444-2 6)

    Example
    -------
    >>> encode(phrase="I AM")
    444-2 6
    >>> encode(phrase="I AM", output_sep="\n")
    444
    2 6
    """
    encoded_words = []
    words = phrase.split(input_sep)
    for word in words:
        encoded_chars = []
        for char in word:
            char = char.upper()
            for num_key, letters in NUMPAD.items():
                if char in letters:
                    encoded_char = num_key * (letters.index(char) + 1)
                    encoded_chars.append(encoded_char)

        encoded_word = ' '.join(encoded_chars)
        encoded_words.append(encoded_word)
    
    return output_sep.join(encoded_words)


# print(encode("AS BLACK AS NIGHT"))
# print(decode("2 7777-22 555 2 222 55-2 7777-66 444 4 44 8", word_sep="-"))
# print(encode("YOU ARE AN ABSOLUTE POOHEAD", output_sep='\n'))
# print(decode("""999 666 88
# 2 777 33
# 2 66
# 2 22 7777 666 555 88 8 33
# 7 666 666 44 33 2 3""", word_sep='\n'))
