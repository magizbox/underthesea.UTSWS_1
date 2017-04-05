# -*- coding: utf-8 -*-
from os import listdir

import re
from os.path import dirname, join

punctuations = open(join(dirname(__file__), "punctuation.txt"), "r").read().splitlines()
punctuations = [p.decode("utf-8") for p in punctuations]


def tokenize(text):
    specials = ["->", "\.\.\.",">>"]
    digit = "\d+([\.,_]\d+)+"
    email = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    web = "^(http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$"
    word = "\w+"
    non_word = "[^\w\s]"
    specials_name = u"[A-Za-zôăâêươđ]+-[A-Za-z0-9ôăâêươđ]+"

    patterns = []
    patterns.extend(specials)
    patterns.extend([web, email, specials_name])
    patterns.extend([digit, non_word, word])

    patterns = "(" + "|".join(patterns) + ")"
    tokens = re.findall(patterns, text, re.UNICODE)
    return u" ".join(["%s" % token[0] for token in tokens])


if __name__ == '__main__':
    file_path = join(dirname(dirname(__file__)), "data")
    out_file_path = join(dirname(dirname(__file__)), "corpus", "input")
    ids = listdir(file_path)
    sentences = [open(join(out_file_path, id), "w").write(
        tokenize(open(join(file_path, id), "r").read().decode('utf-8')).encode('utf-8')) for id in ids]
    print 0
