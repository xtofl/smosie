import sys

def to_caesar(text, key=('s', 12)):
    return text

def to_morse(text):
    return "  ".join(word for word in text.split())

def convert(path):
    text = "\n".join(open(path).readlines())
    caesar = to_caesar(text)
    morse = to_morse(caesar)
    print(caesar)
    print(morse)


if __name__ == "__main__":
    convert(sys.argv[1])
