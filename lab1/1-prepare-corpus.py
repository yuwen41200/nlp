#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('../cornell_movie_dialogs_corpus/movie_lines.txt', encoding='cp1252') as fin:
        with open('corpus.txt', 'w') as fout:
            for line in fin:
                fields = line.split('+++$+++')
                assert len(fields) == 5
                sentence = fields[4].strip()
                if sentence != '':
                    sentence += '\n'
                    fout.write(sentence)
