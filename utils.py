import numpy as np
import re


def get_translate_table(from_letters, to_letters):
    """
    Override str object to convert turkish letters to english letters
    @return: Translate table
    """
    return str.maketrans(from_letters, to_letters)


def get_process_data(file_name):
    """
    Preparation of data
    @param file_name: file
    @return: dictionary contains processed words from corpus as values
    """
    words = re.findall(r'\D+', open(file_name).read().lower())
    w_dict = {}
    for i, word in enumerate(words, 1):
        word = re.sub("\n", "", re.sub(",", "", word))
        w_dict[i] = re.split(r'\s', word)
    return w_dict


def min_edit_distance(word_1, word_2, ins_cost=1, del_cost=1, rep_cost=2):
    """
    Function counts minimum edit distance between words to get similarity
    @param word_1: source word
    @param word_2: target word
    @param ins_cost: preset insert cost
    @param del_cost: preset delete cost
    @param rep_cost: preset replace cost
    @return:
        med: minimum edit distance between word_1 and word_2
    """
    m = len(word_1)
    n = len(word_2)
    D = np.zeros((m+1, n+1), dtype=int)

    D[0, 0] = 0
    for i in range(m):
        D[i + 1, 0] = D[i, 0] + del_cost
    for j in range(n):
        D[0, j + 1] = D[0, j] + ins_cost

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            add = D[i, j - 1] + ins_cost
            sub = D[i - 1, j] + del_cost
            if word_1[i - 1] == word_2[j - 1]:
                replace = D[i - 1, j - 1]
            else:
                replace = D[i - 1, j - 1] + rep_cost

            D[i, j] = min(add, sub, replace)
    med = D[m, n]
    return med

