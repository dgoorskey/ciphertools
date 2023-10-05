"""
Removes whitespace from text, read from stdin.
"""

import fileinput
import string

if __name__ == '__main__':
    text = ''.join(fileinput.input())
    for c in string.whitespace:
        text = text.replace(c, '')
    print(text)
