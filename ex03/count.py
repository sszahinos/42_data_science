import sys



def text_analyzer(text=None):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
    lower = 0
    upper = 0
    sign = 0
    space = 0

    if text == None:
        print("What is the text to analyze?")
        return
    try:
        number = int(text)
        print("AssertionError: argument is not a string")
        return
    except ValueError:
        pass
    for ch in text:
        if ch.islower():
            lower += 1
        elif ch.isupper():
            upper += 1
        elif ch.isspace():
            space += 1
        elif not ch.isdigit():
            sign += 1
    print("""The text contains {} character(s):
- {} upper letter(s)
- {} lower letter(s)
- {} punctuation mark(s)
- {} space(s)
""".format(len(text), upper, lower, sign, space))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print()
    elif len(sys.argv) != 2:
        print("AssertionError: more than one argument are provided")
    else:
        text_analyzer(sys.argv[1])