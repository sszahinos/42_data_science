import sys

phrase = ' '.join(sys.argv[1:])
print(phrase.swapcase()[::-1])