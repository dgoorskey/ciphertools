"""
Finds digraph frequencies.
Reads input from stdin.
"""

import sys
import fileinput

def main(argc: int, argv: list[str]) -> int:
    text = ''.join(fileinput.input())

    digraphs: dict[str, int] = {}
    for i in range(len(text) - 1):
        digraph = f'{text[i]}{text[i+1]}'
        if digraph in digraphs:
            digraphs[digraph] += 1
        else:
            digraphs[digraph] = 1
    
    sorted_digraphs: list[tuple[str, int]] = sorted(digraphs.items(), key=lambda i: i[1], reverse=True)

    max_occurrances = sorted_digraphs[0][1]

    print('DIGRAPH\tRELATIVE_FREQUENCY\tINVERSE_RELATIVE_FREQUENCY\tFREQUENCY_DIFFERENCE')
    for digraph in sorted_digraphs:
        ratio = digraph[1] / max_occurrances
        inverse_digraph = digraph[0][::-1]

        inverse_ratio = 0.0
        if inverse_digraph in digraphs:
            inverse_ratio = digraphs[inverse_digraph] / max_occurrances
            ratio_difference = abs(ratio - inverse_ratio)
        print(f'{digraph[0]}\t{ratio:.2}\t{inverse_ratio:.2}\t{ratio_difference:.2}')

    return 0

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)

    status = main(argc, argv)
    
    sys.exit(status)
