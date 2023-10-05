"""
Attempts to insert spaces between words found in a string.
This is a naive and inefficient implementation.
"""

import sys
import fileinput

def find_word(text: str, words: list[str]) -> int:
    """
    Finds the next word in `text`, prioritizing longer words over shorter ones.
    """

    longest_word: str = ''
    for word in words:
        if len(word) > len(longest_word) and text.startswith(word):
            longest_word = word
    
    return len(longest_word)

def insert_substring(string: str, substring: str, index: int) -> str:
    """
    Inserts a substring into a string at a given index.
    """
    return string[:index] + substring + string[index:]

if __name__ == '__main__':
    text = ''.join(fileinput.input())
    
    words_filepath = '/usr/share/dict/words'

    words: list[str] = []
    with open(words_filepath) as f:
        words = f.read().split()
    
    max_word_length = 0
    for word in words:
        if len(word) > max_word_length:
            max_word_length = len(word)
    
    idx_start = 0
    while idx_start < len(text):
        word_length = find_word(text[idx_start:], words)
        if word_length == 0:
            idx_start += 1
        else:
            idx_start += word_length
            text = insert_substring(text, ' ', idx_start)
            idx_start += 1
    
    print(text)
