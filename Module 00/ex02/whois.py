import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
elif len(sys.argv) == 2:
    flag = True
    try:
        number = int(sys.argv[1])
    except ValueError:
        flag = False
    if not flag:
        print("AssertionError: argument is not an integer")
    else:
        if number == 0:
            print("I'm Zero.")
        elif number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
else:
    print()