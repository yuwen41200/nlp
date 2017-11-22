#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pythonopensubtitles.opensubtitles import OpenSubtitles
import webbrowser
import jieba
import jieba.posseg as pseg

jieba.set_dictionary('dict.txt.big')
jieba.enable_parallel(4)


def crawler(title):
    ost = OpenSubtitles()
    _ = ost.login("doctest", 'doctest')
    data = ost.search_subtitles([{'query': title, 'sublanguageid': 'zht'}])
    link = data[0]['ZipDownloadLink']
    webbrowser.open(link, new=2, autoraise=True)


def parser(filename):
    with open(filename) as f:
        state = 1
        for line in f:
            if state == 3:
                line = line.strip()
                words = pseg.cut(line)
                for word, flag in words:
                    print(word, flag)
                print('-----')
                state = 0
            else:
                state += 1


if __name__ == '__main__':
    crawler('cape no.7')
    parser('Cape.No.7.2008.BluRay.720p.x264.AC3-CMCT.srt')
