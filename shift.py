"""
Performs a shift cipher on text from stdin.
Characters that aren't ascii letters will not be shifted.
Characters that are ascii letters will have their case preserved.
"""

import fileinput
import string
import sys

if __name__ == '__main__':
    upper_alphabet = string.ascii_uppercase
    lower_alphabet = string.ascii_lowercase

    argv = sys.argv
    argc = len(argv)

    if '--help' in argv:
        print('Usage: shift.py [SHIFT]')
        exit(0)

    if argc < 2:
        print('Usage: shift.py [SHIFT]')
        exit(0)
    
    try:
        shift = int(argv[1])
    except:
        print(f'shift.py: invalid shift, expected an integer, got "{argv[1]}" instead')
        exit(-1)

    text = ''.join(fileinput.input(files=[]))

    result = ''
    for c in text:
        alphabet = upper_alphabet
        if c in lower_alphabet:
            alphabet = lower_alphabet

        # if c isn't a letter, it won't be found in upper_alphabet anyways
        n = alphabet.find(c)
        if n != -1:
            n_shifted = (n + shift) % len(alphabet)
            c = alphabet[n_shifted]
        result += c
    
    print(result)
