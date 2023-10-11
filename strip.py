"""
Removes whitespace from text, read from stdin.
"""

import os
import sys
import fileinput
import string
import errno

def main(argc: int, argv: list[str]) -> int:
    text = ''.join(fileinput.input())

    for c in string.whitespace:
        text = text.replace(c, '')
    print(text)

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)

    status = main(argc, argv)

    sys.exit(status)
