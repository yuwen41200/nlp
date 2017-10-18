#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import html

if __name__ == '__main__':
    c_map = []
    p_map = []
    i_map = []

    with open('corpus.txt') as file:
        line_no = 1
        for line in file:
            for char in html.unescape(line):
                if char.isalnum():
                    c_map.append((char, line_no))
            line_no += 1

    with open('parsed.txt') as file:
        state = 0
        line_no = 1
        for line in file:
            if line == '\n':
                state += 1
            elif state % 3 == 0:
                tokens = line.split()
                for token in tokens:
                    parts = token.rsplit('/', maxsplit=1)
                    if parts[0][0] == '-' and parts[0][-1] == '-':
                        continue
                    for char in parts[0]:
                        if char.isalnum():
                            p_map.append((char, line_no))
            line_no += 1

    with open('../cornell_movie_dialogs_corpus/movie_lines.txt', encoding='cp1252') as file:
        for line in file:
            fields = line.split('+++$+++')
            line_no = fields[0].strip()
            sentence = fields[4].strip()
            if sentence != '':
                i_map.append(line_no)

    try:
        assert len(c_map) == len(p_map)
        assert len(i_map) == 304446
    except AssertionError:
        print('WTF?!')
        print(len(c_map), len(p_map), len(i_map), sep='\t')

    for i in range(len(c_map)):
        try:
            assert c_map[i][0] == p_map[i][0]
        except AssertionError:
            print('WTF?!')
            for j in range(i - 10, i + 10):
                print(c_map[j][0], c_map[j][1], p_map[j][0], p_map[j][1], sep='\t')
            exit(0)
        else:
            print(i_map[c_map[i][1]-1], c_map[i][1], p_map[i][1], c_map[i][0], sep='\t')
