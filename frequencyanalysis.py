import sys
import fileinput

def main(argc: int, argv: list[str]) -> int:
    text = ''.join(fileinput.input())

    characters: dict[str, int] = {}

    for c in text:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    
    sorted_characters: list[tuple[str, int]] = sorted(characters.items(), key=lambda i: i[1], reverse=True)

    for character, occurrances in sorted_characters:
        print(f'{character}\t{occurrances}')

    return 0

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    
    status = main(argc, argv)

    sys.exit(status)
