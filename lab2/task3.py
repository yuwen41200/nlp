#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
import jieba.posseg as pseg

jieba.set_dictionary('dict.txt.big')
jieba.enable_parallel(4)
pos_pattern = {}


def parser(filename):
    with open(filename) as f:
        for line in f:
            words = pseg.cut(line.strip())
            words = [(word, flag[0]) for word, flag in words if flag[0] != 'x']
            for i in range(len(words)-1):
                key = words[i][1] + words[i+1][1]
                value = words[i][0] + words[i+1][0]
                if key not in pos_pattern:
                    pos_pattern[key] = []
                pos_pattern[key].append(value)


if __name__ == '__main__':
    parser('年度最高票房紀錄列表簡中.csv')
    for _ in range(3):
        m = max(pos_pattern, key=lambda x: len(pos_pattern[x]))
        title = '(' + m[0] + ', ' + m[1] + ')'
        ans = '\t'.join(pos_pattern[m])
        print(title, len(pos_pattern[m]), ans, sep='\t')
        del pos_pattern[m]
