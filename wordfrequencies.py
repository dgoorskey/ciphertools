import sys
import fileinput

def main(argc: int, argv: list[str]) -> int:
    text = ''.join(fileinput.input())

    words = text.split()

    word_frequencies: dict[str, int] = {}
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    
    sorted_word_frequencies = sorted(
        word_frequencies.items(),
        key=lambda i: i[1],
        reverse=True
    )
    sorted_word_frequencies: dict[str, int] = dict(sorted_word_frequencies)

    for word, count in sorted_word_frequencies.items():
        print(f'{word}\t{count}')

    return 0

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)

    status = main(argc, argv)

    sys.exit(status)