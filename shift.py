"""
Performs a shift cipher on text from stdin.
Characters that aren't ascii letters will not be shifted.
Characters that are ascii letters will have their case preserved.
"""

import sys
import fileinput
import string

def main(argc: int, argv: list[str]) -> int:
    upper_alphabet = string.ascii_uppercase
    lower_alphabet = string.ascii_lowercase

    text = ''.join(fileinput.input(files=argv[3:]))

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

    return 0

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)

    status = main(argc, argv)

    sys.exit(status)
