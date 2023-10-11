"""
Converts text from stdin to lowercase.
"""

import sys
import fileinput

def main(argc: int, argv: list[str]) -> int:
    text = ''.join(fileinput.input())
    text = text.lower()
    print(text)

    return 0

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)

    status = main(argc, argv)

    sys.exit(status)
