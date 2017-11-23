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
            keys = [flag[0] for word, flag in words if flag[0] != 'x']
            key_str = '(' + ', '.join(keys) + ')'
            value_str = line.strip()
            if key_str not in pos_pattern:
                pos_pattern[key_str] = []
            pos_pattern[key_str].append(value_str)


if __name__ == '__main__':
    parser('年度最高票房紀錄列表簡中.csv')
    for _ in range(3):
        m = max(pos_pattern, key=lambda x: len(pos_pattern[x]))
        ans = '\t'.join(pos_pattern[m])
        print(m, len(pos_pattern[m]), ans, sep='\t')
        del pos_pattern[m]
