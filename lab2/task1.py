#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pythonopensubtitles.opensubtitles import OpenSubtitles
import webbrowser
import jieba
import jieba.posseg as pseg
import pprint
import time
import zipfile
import os

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
    with zipfile.ZipFile(filename) as z:
        subtitle_info = None
        for i in z.infolist():
            if i.filename.endswith('.srt'):
                subtitle_info = i
                break
        subtitle_file = z.extract(subtitle_info)
    with open(subtitle_file, errors='backslashreplace') as f:
        state = 1
        for line in reversed(list(f)):
            if state == 2:
                print(line.strip())
                state = 3
                continue
            if state == 3:
                assert line.strip() == ''
                break
            if '-->' in line:
                state = 2
    os.unlink(subtitle_file)


def part1():
    with open('task1.csv') as f:
        for line in f:
            title = line.split('\t')[0]
            crawler(title)
            time.sleep(10)


def part2():
    path = r'/Users/ywpu/Downloads'
    with open('task1map.txt') as f:
        for line in f:
            filename = os.path.join(path, line.strip())
            # noinspection PyBroadException
            try:
                counter(filename)
            except:
                print(filename)


def part3():
    outputs = []
    with open('task1.txt') as f1:
        with open('task1p2.txt') as f2:
            for l1 in f1:
                l2 = f2.readline()
                outputs.append(l1.strip() + '\t' + l2.strip() + '\n')
    with open('task1.txt', 'w') as f:
        f.writelines(outputs)


if __name__ == '__main__':
    part3()
