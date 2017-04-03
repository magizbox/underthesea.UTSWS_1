# -*- coding: utf-8 -*-
from os import listdir

import re
from os.path import dirname, join

punctuations = open(join(dirname(__file__), "punctuation.txt"), "r").read().splitlines()
punctuations = [p.decode("utf-8") for p in punctuations]


def tokenize(token):
    digit_regex = r"\b\d+([\.,]\d+)+\b"
    email_regex = "[^@]+@[^@]+\.[^@]+"
    web_regex = "^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$"
    web_2_regex = "\w+\.(com)"
    special_character = "->"
    specials = [digit_regex, email_regex, special_character, web_regex, web_2_regex]
    for special in specials:
        if re.match(special, token, re.UNICODE):
            return token
    # digit_regex_ = "\d+([\.,]\d+)+"
    for pattern in specials:
        if re.findall(pattern, token, re.UNICODE):
            token = re.sub(pattern, lambda matched: matched.group() + " ", token)
            return tokenize_sentence(token)
    for punctuation in punctuations:
        token = token.replace(punctuation, u" {} ".format(punctuation))
    return token


def tokenize_sentence(sentence):
    tokens = re.split("\s", sentence)
    tokens = [tokenize(token) for token in tokens]
    output = u" ".join(tokens)
    output = re.sub(r"\s+", " ", output)
    return output


if __name__ == '__main__':
    file_path = join(dirname(dirname(__file__)), "data")
    out_file_path = join(dirname(dirname(__file__)), "corpus", "input")
    ids = listdir(file_path)
    ids = ids[:10]
    sentences = [open(join(out_file_path, id), "w").write(
        tokenize_sentence(open(join(file_path, id), "r").read().decode('utf-8')).encode('utf-8')) for id in ids]
    print 0
