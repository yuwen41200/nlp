#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pythonopensubtitles.opensubtitles import OpenSubtitles
import webbrowser
import jieba
import jieba.posseg as pseg
import pprint
import time
import zipfile

jieba.set_dictionary('dict.txt.big')
jieba.enable_parallel(4)
pp = pprint.PrettyPrinter(indent=4)


def crawler(title):
    ost = OpenSubtitles()
    _ = ost.login("doctest", 'doctest')
    data = ost.search_subtitles([{'query': title, 'sublanguageid': 'zht'}])
    # pp.pprint(data)
    highest_download_count = -1
    link = ''
    for d in data:
        if int(d['SubDownloadsCnt']) > highest_download_count:
            highest_download_count = int(d['SubDownloadsCnt'])
            link = d['ZipDownloadLink']
    webbrowser.open(link, new=2, autoraise=True)
    print(title, link, sep='\t', flush=True)


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


def counter(filename):
    with zipfile.ZipFile(filename, 'r') as z:
        print(z.namelist())
        # z.extractall('temp')


def part1():
    with open('task1.csv') as f:
        for line in f:
            title = line.split('\t')[0]
            crawler(title)
            time.sleep(10)


def part2():
    path = r'~/Downloads/'
    with open('task1map.txt') as f:
        for line in f:
            filename = path + line.strip()
            filename = filename.replace(r'(', r'\(')
            filename = filename.replace(r')', r'\)')
            counter(filename)
            break


if __name__ == '__main__':
    part2()
