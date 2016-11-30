import sys

def to_caesar(text, key=('s', 12)):
    """
    >>> to_caesar("abc", key=('a', 0))
    'abc'
    """
    return text

def to_morse(text):
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
		    
    convert = lambda w: str([CODE[c] for c in w])
    return "  ".join(convert(word.upper()) for word in text.split())

def convert(path):
    text = "\n".join(open(path).readlines())
    caesar = to_caesar(text)
    morse = to_morse(caesar)
    print(caesar)
    print(morse)


if __name__ == "__main__":
    convert(sys.argv[1])
