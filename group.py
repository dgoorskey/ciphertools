import fileinput
import sys

def main(argc: int, argv: list[str]) -> int:
    filepaths = argv[3:]
    text = ''.join(fileinput.input(files=filepaths))

    if argc < 2:
        print('Usage: group.py [SIZE]')
        return 0
    
    size = int(argv[1])
    if size < 1:
        print('group.py: bad group size')
        return -1

    grouped_text = ''
    i = 0
    while i < len(text):
        c = text[i]

        if i % size == 0 and i != 0:
            grouped_text += ' '
        
        grouped_text += c

        i += 1
    
    print(grouped_text)

    return 0

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)

    status = main(argc, argv)

    sys.exit(status)
