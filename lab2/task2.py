#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
import jieba.posseg as pseg
import json
import math

jieba.set_dictionary('dict.txt.big')
jieba.enable_parallel(4)


def parser(filename):
    observations = []
    with open(filename) as f:
        state = 1
        for line in f:
            if state == 3:
                line = line.strip()
                words = pseg.cut(line)
                observations.append([])
                for word, flag in words:
                    if word in {'喜欢', '妳', '打', '手枪', '追', '她'}:
                        observations[-1].append((word, flag))
                        print(len(observations), word, flag)
                state = 0
            else:
                state += 1
    with open('task2.json', 'w') as f:
        json.dump(observations, f, ensure_ascii=False, indent='\t')


def analyzer1():
    counter = {}
    with open('task2.json') as f:
        observations = json.load(f)
    print('N =', len(observations))
    ls = [term[0] + term[1] for line in observations for term in line]
    for l in ls:
        if l not in counter:
            counter[l] = 0
        counter[l] += 1
    for k, v in counter.items():
        print(k, v)


def probability(observations, word1, flag1, word2=None, flag2=None):
    count = 0
    N = len(observations)
    if not word2:
        word2, flag2 = word1, flag1
    for line in observations:
        match1, match2 = False, False
        for term in line:
            if term[0] == word1 and term[1] == flag1:
                match1 = True
            if term[0] == word2 and term[1] == flag2:
                match2 = True
        if match1 and match2:
            count += 1
    return count / N


def pointwise_mutual_information(observations, word1, flag1, word2, flag2):
    Px = probability(observations, word1, flag1)
    Py = probability(observations, word2, flag2)
    Pxy = probability(observations, word1, flag1, word2, flag2)
    PMI = math.log2(Pxy / (Px * Py))
    print(word1, flag1, Px, sep='\t')
    print(word2, flag2, Py, sep='\t')
    print(PMI)
    print()
    return PMI


def analyzer2():
    with open('task2.json') as f:
        observations = json.load(f)
    pointwise_mutual_information(observations, '喜欢', 'v', '妳', 'zg')
    pointwise_mutual_information(observations, '打', 'v', '手枪', 'n')
    pointwise_mutual_information(observations, '追', 'v', '她', 'r')


if __name__ == '__main__':
    # parser('You Are the Apple of My Eye SC.srt')
    # analyzer1()
    analyzer2()
