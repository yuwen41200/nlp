#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
import jieba.posseg as pseg
import json

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


if __name__ == '__main__':
    parser('You Are the Apple of My Eye SC.srt')
