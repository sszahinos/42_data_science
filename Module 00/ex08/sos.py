import sys

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

def to_morse(text: str):
    for word in text:
        for chr in word:
            print(MORSE_CODE[chr], end=" ")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        raw_text = ''
        for word in sys.argv[1:]:
            raw_text += word + ' '
        for ch in raw_text:
            if not ch.isalnum() and not ch.isspace():
                print("Error. Arg is not alnum.")
                exit(1)
        text = raw_text.strip().upper()
        to_morse(text)