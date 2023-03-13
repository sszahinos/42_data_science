import math
import sys
from decimal import Decimal

def calculator(a: int, b: int):
    if b == 0:
        quotient = reminder = "ERROR: Division by 0."
    else:
        quotient = Decimal(a / float(b))
        reminder = a % b
        #if abs(quotient.as_tuple().exponent) > 3:
        #    quotient = "{:.3f}...".format(quotient)
        #else:
        #    quotient = "{:.2f}".format(quotient)
        quotient = "{:.2f}".format(quotient)
    print("""Sum:\t\t{}
Difference:\t{}
Product:\t{}
Quotient:\t{}
Remainder:\t{}""".format(a + b, a - b, a * b, quotient, reminder))

def check_int(arg):
    try:
        number = int(arg)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print()
    elif len(sys.argv) != 3:
        print("AssertionError: more than one argument are provided")
    elif not check_int(sys.argv[1]) or not check_int(sys.argv[2]):
        print("AssertionError: incorrect argument.")
    else:
        calculator(int(sys.argv[1]), int(sys.argv[2]))