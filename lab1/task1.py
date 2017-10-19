#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from math import log10

if __name__ == '__main__':
    corpus = []
    with open('parsed.txt') as file:
        state = 0
        line_no = 1
        for line in file:
            if line == '\n':
                state += 1
            elif state % 3 == 0:
                sentence = []
                tokens = line.split()
                for token in tokens:
                    parts = token.rsplit('/', maxsplit=1)
                    if len(parts) != 2:
                        continue
                    word = (parts[0].lower(), parts[1])
                    sentence.append(word)
                corpus.append(sentence)
            line_no += 1
    cntr = Counter(word[0] for sentence in corpus for word in sentence)
    dimension = [word[0] for word in cntr.most_common(300)]
    dimension_pos = [''] * 300
    print('|'.join(dimension))
    N = len(corpus)
    df = [0] * 300
    for sentence in corpus:
        exist = [False] * 300
        for word in sentence:
            for i in range(300):
                if word[0] == dimension[i] and not exist[i]:
                    dimension_pos[i] = word[1]
                    df[i] += 1
                    exist[i] = True
    print('|'.join(dimension_pos))
    idf = []
    for i in range(300):
        idf.append(str(log10(N / df[i])))
    print(','.join(idf))
