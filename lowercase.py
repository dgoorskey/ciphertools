"""
Converts text from stdin to lowercase.
"""

import fileinput

if __name__ == '__main__':
    text = ''.join(fileinput.input())
    text = text.lower()
    print(text)
