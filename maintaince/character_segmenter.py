# -*- coding: utf-8 -*-
import os
import re

punctuations = open("punctuation.txt", "r").read().splitlines()
punctuations = [p.decode("utf-8") for p in punctuations]


def token_segmenter(token):
    digit_regex = r"^\d+(\.\d+)+$"
    money_regex = r"^\d+(\.\d+)+\w"
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    url_regex = r""
    specials = [digit_regex, email_regex, money_regex,url_regex]
    for special in specials:
        if re.match(special, token):
            return token
    for punctuation in punctuations:
        token = token.replace(punctuation, u" {} ".format(punctuation))
    return token


def character_segmenter(sentence):
    tokens = re.split("(\ |/)", sentence)
    tokens = [token_segmenter(token) for token in tokens]
    output = u" ".join(tokens)
    output = output.replace("  ", " ")
    return output


if __name__ == '__main__':
    file_names = os.listdir("../data/")
    for file_name in file_names:
        input = os.path.join("../data", file_name)
        lines = open(input, 'r').read().splitlines()

        segmented_lines = [character_segmenter(l) for l in lines]
        content = zip(lines, segmented_lines)
        content = "\n\n".join(["\n".join(item) for item in content])

        output = os.path.join("../corpus/input", file_name)
        open(output, "w").write(content)
    print "finish"

