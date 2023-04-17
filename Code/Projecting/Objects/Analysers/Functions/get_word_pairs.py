from itertools import combinations


def get_wp_in_line_hard(text: str) -> list:
    words = text.split(' ')
    words_pairs = list()
    for i in range(len(words)):
        for j in range(i, len(words)):
            if j-i > 1:
                words_pairs.append(' '.join(words[i:j]))
    return words_pairs
