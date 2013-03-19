#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import with_statement
from __future__ import print_function 


from bwt import bwt


FILENAME = 'text.txt'
MAX_CHUNK_SIZE = 1024
MAX_NUM_CHUNKS = 5


def levenshtein_distance(s1, s2):
    """
    Compute the Levenshtein distance between two strings s1 and s2.
    """
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s2) == 0:
        return len(s1)
    length1 = len(s1) + 1
    length2 = len(s2) + 1
    distance_matrix = [[0] * length2 for x in range(length1)]
    for i in range(length1):
       distance_matrix[i][0] = i
    for j in range(length2):
       distance_matrix[0][j] = j
    for i in range(1, length1):
        for j in range(1, length2):
            del_cost = distance_matrix[i-1][j] + 1
            ins_cost = distance_matrix[i][j-1] + 1
            sub_cost = distance_matrix[i-1][j-1]
            if s1[i-1] != s2[j-1]:
                sub_cost += 1
            distance_matrix[i][j] = min(del_cost, ins_cost, sub_cost)
    return distance_matrix[-1][-1]


def compute_distance_matrix(chunks, verbose=False):
    matrix = []
    n_chunks = len(chunks)
    for i in range(n_chunks):
        matrix.append([])
        for j in range(n_chunks):
            d = levenshtein_distance(chunks[i], chunks[j])
            matrix[-1].append(d)
            if verbose:
                if j > 0:
                    print(', ', end='')
                print('{0:#5}'.format(d), end='')
        if verbose:
            print('')
    return matrix


def main():
    chunks = []
    with open(FILENAME, 'rb') as f:
        for _ in range(MAX_NUM_CHUNKS):
            c = f.read(MAX_CHUNK_SIZE)
            if not c:
                break
            chunks.append(c)

    print('Original:')
    matrix = compute_distance_matrix(chunks, verbose=True)
    # print(matrix)

    print('After BWT:')
    chunks_bwt = [bwt(c) for c in chunks]
    matrix_bwt = compute_distance_matrix(chunks_bwt, verbose=True)
    # print(matrix_bwt)


if __name__ == "__main__":
    main()
