import sys

def get_word_list(text: str):
    text = text.split(' ')
    for index, word in enumerate(text):
        text[index] = ''.join(ch for ch in word if ch.isalnum())
        if text[index] == "":
            text.pop(index)
    return text


def filter_words(text, char_num):
    text = get_word_list(text)
    filtered_words = [x for x in text if len(x) >= char_num]
    print(filtered_words)


if __name__ == "__main__":
    if len(sys.argv) != 3 or not sys.argv[2].isdigit():
        print("AssertionError: Arguments error.")
    else:
        get_word_list("hola! q.ue  t4l")
        filter_words(sys.argv[1], int(sys.argv[2]))