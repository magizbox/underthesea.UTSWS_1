# -*- coding: utf-8 -*-
from os import listdir

import re
from os.path import dirname, join

punctuations = open(join(dirname(__file__), "punctuation.txt"), "r").read().splitlines()
punctuations = [p.decode("utf-8") for p in punctuations]


def token_segmenter(token):
    number = r"[0-9]|."
    digit_regex = "^\d+((\.\d+)|(\,\d))+$"
    # money_regex = "^\d+(\.\d+)+\w$"
    email_regex = "[^@]+@[^@]+\.[^@]+"
    web_regex = "^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$"
    web_2_regex = "\w+\.(com)"
    money_regex = r"\d+(\.\d)+\w"
    special_character = "->"
    special_regex = "\w+\/+\d"
    character_regex = r"[a-z]"
    specials = [money_regex, digit_regex, email_regex, special_character, web_regex, web_2_regex]
    for special in specials:
        a = ""
        if re.match(number, token):
            for character in token:
                if character in character_regex:
                    a = character
                    break
            if a != "":
                token = token.split(a)
                print 0
        if re.match(special, token):
            return token
    for punctuation in punctuations:
        token = token.replace(punctuation, u" {} ".format(punctuation))
    return token


def character_segmenter(sentence):
    tokens = re.split(" ", sentence)
    tokens = [token_segmenter(token) for token in tokens]
    output = u" ".join(tokens)
    while "  " in output:
        output = output.replace("  ", " ")
    return output


if __name__ == '__main__':
    file_path = join(dirname(dirname(__file__)), "data")
    out_file_path = join(dirname(dirname(__file__)), "corpus", "input")
    ids = listdir(file_path)
    ids = ids[:10]
    sentences = [open(join(out_file_path, id), "w").write(
        character_segmenter(open(join(file_path, id), "r").read().decode('utf-8')).encode('utf-8')) for id in ids]
    print 0
