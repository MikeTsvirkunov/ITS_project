from itertools import combinations
import numpy as np


def get_wp_in_line_hard(text: str) -> list:
    words = text.split(' ')
    words_pairs = list()
    for i in range(len(words)):
        for j in range(i, len(words)):
            if j-i > 1:
                words_pairs.append(' '.join(words[i:j]))
    return words_pairs


def get_vectorized_wp_and_wp(word_pairs: str, 
                             vectorizer: callable):
    list_of_wp, list_of_vectors = list(), list()
    for wp in word_pairs:
        # print(wp)
        list_of_vectors.append(vectorizer(wp))
        list_of_wp.append(wp)
    return np.array(list_of_wp), np.array(list_of_vectors)