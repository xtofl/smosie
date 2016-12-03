import sys
import string

def to_caesar(text, key=('s', 12)):
    """
    >>> to_caesar("abc", key=('a', 1))
    'lmn'
    >>> to_caesar("abc", key=('b', 2))
    'lmn'
    >>> to_caesar("safe: tegen", key=('s', 12))
    'weji: xikir'
    """
    outer_alphabet = "abcdefghijklmnopqrstuvwxyz"
    inner_alphabet = "lmnopqrstuvwxyzabcdefghijk"
    shift = key[1] - (ord(key[0])-ord('a')+1)
    shifted_inner_alphabet = inner_alphabet[shift:] + inner_alphabet[:shift]
    table = str.maketrans(outer_alphabet, shifted_inner_alphabet)
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
    print("\n\n")
    print("("+ to_caesar("in de kamer van isaak", ('b', 7))+")")
    print(to_morse("dit is code b zeven: " + to_caesar("in de kamer van isaak", ('b', 7))))
    print("\n\n")
    print(to_morse("in de bedla van jona"))
    print("\n\n")
    print(to_morse("in de mand van de oudste"))
