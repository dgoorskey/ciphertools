"""
Converts text from stdin to uppercase.
"""

import fileinput

if __name__ == '__main__':
    text = ''.join(fileinput.input())
    text = text.upper()
    print(text)
