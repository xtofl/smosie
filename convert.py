import sys
import string

def to_caesar(text, key=('s', 12)):
    """
    >>> to_caesar("abc", key=('a', 2))
    'bcd'
    >>> to_caesar("abc", key=('b', 3))
    'bcd'
    >>> to_caesar("safe: tegen", key=('s', 23))
    'weji: xikir'
    """
    alphabet = string.ascii_lowercase
    # shifted('s') == ascii(12)
    # s + shift = 12
    # shift = 12 - ord(s)
    shift = (key[1]-1) - (ord(key[0]) - ord('a'))
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

def to_morse(text):
    """
    >>> to_morse('abc')
    '.-  -...  -.-.'
    >>> to_morse('abc abc')
    '.-  -...  -.-.  /  .-  -...  -.-.'
    """
    CODE = {
        'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
		    
    def encode(c):
        if c in CODE:
            return CODE[c]
        else:
            return c
    convert = lambda w: "  ".join([encode(c) for c in w])
    return "  /  ".join(convert(word.upper()) for word in text.split())

def convert(path):
    text = "\n".join(open(path).readlines())
    caesar = "dit is code s twaalf\n" + to_caesar(text, key=('s', 12))
    morse = to_morse(caesar)
    print(caesar)
    print(morse)


if __name__ == "__main__":
    convert(sys.argv[1])
