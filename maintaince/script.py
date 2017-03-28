# -*- coding: utf-8 -*-
import os
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')


punctuations = open("punctuation.txt", "r").read().splitlines()
punctuations = [unicode(p) for p in punctuations]


def character_segmenter(sentence):
    sentence = re.match('^[a-zA-Z0-9._\s]+$', sentence)
    for punctuation in punctuations:
        sentence = sentence.replace(punctuation, ' {} '.format(punctuation))
        sentence = ' '.join(sentence.split())
    return sentence


def process_data():
    file_names = os.listdir("../data")
    for file_name in file_names:
        file_path = os.path.join("../data", file_name)
        with open(file_path, 'r') as f:
            for line in f:
                processed_line = character_segmenter(line)
                yield (file_name, processed_line)


def save_data(file_path, line):
    with open(file_path, 'a+') as f:
        f.write(line)
        f.write('\n')
        f.flush()


if __name__ == '__main__':
    processed_data = process_data()
    for file_name, processed_line in processed_data:
        file_path = os.path.join("../corpus/input", file_name)
        save_data(file_path, processed_line)

