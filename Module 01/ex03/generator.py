from random import randint

def shuffle_list(lst: list):
    new_list = []
    while (len(lst) != 0):
        new_list.append(lst.pop(randint(0, len(lst) - 1)))
    return new_list

def get_unique_list(lst: list):
    unique_set = set(lst)
    return list(unique_set)
    
def order_list(lst: list):
    lst.sort()
    return lst

def generator(text: str, sep=" ", option=None):
    """Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
option especifica si una acción se realizará sobre las sub-strings antes de ser producidas."""
    if not text.isprintable():
        print("ERROR: Text has non printable characters.")
        return None
    if option != None and option != "shuffle" and option != "unique" and option != "ordered":
        print("ERROR: Wrong option.")
        return None
    text = text.split(sep)
    if option == "shuffle":
        text = shuffle_list(text)
    elif option == "unique":
        text = get_unique_list(text)
    elif option == "ordered":
        text = order_list(text)
    return text

def test():
    #print(shuffle_list(["hola", "que", "tal", "asdf", "prueba"]))
    #print(get_unique_list(["hola", "que", "tal", "tal", "asdf", "hola", "prueba"]))
    #print(order_list(["hola", "que", "hasta", "tal", "asdf", "prueba", "arbol", "pescado"]))
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" "):
        print(word)
    print("------")
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, option="shuffle"):
        print("shuffle> ", word)
    print("------")
    for word in generator(text, option="ordered"):
        print("ordered> ",word)
    print("------")
    text = "Lorem Ipsum Lorem Ipsum test"
    for word in generator(text, option="unique"):
        print("unique> ",word)
    print("------")

if __name__ == "__main__":
    test()