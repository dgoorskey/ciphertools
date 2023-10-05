import sys
import fileinput

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)

    if '--help' in argv:
        print('Usage: frequencyanalysis.py [TEXT]')
        sys.exit(0)
    
    if '--version' in argv:
        print('frequencyanalysis 1.0')
        sys.exit(0)

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
