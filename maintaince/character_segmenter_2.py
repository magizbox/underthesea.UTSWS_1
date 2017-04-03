# -*- coding: utf-8 -*-
import os
import re

punctuations = open("punctuation.txt", "r").read().splitlines()
punctuations = [p.decode("utf-8") for p in punctuations]

def token_segmenter(token):
    digit_regex = r"^\d+(\.|\,\d+)+$"
    money_regex = r"^\d+(\.\d+)+\w$"
    large_number_regex = r"\d \. \d"
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    special_double_regex = r"[-=<>\s]"
    url_regex = r"((http)|(https))+\:+//"
    specials = [digit_regex, email_regex, money_regex,special_double_regex,url_regex,large_number_regex]

    for special in specials:
        if re.match(special, token):
            return token
    for punctuation in punctuations:
        token = token.replace(punctuation, u" {} ".format(punctuation))
    if re.match(large_number_regex, token, re.UNICODE):
        token = token.replace(" . ", ".")
    return token

def character_segmenter(sentence):
    tokens = re.split(" ", sentence)
    tokens = [token_segmenter(token) for token in tokens]
    output = u" ".join(tokens)
    output = re.sub(' +', ' ', output)
    return output


# def character_segmenter(sentence):
#     if token_segmenter(sentence) in sentence:
#         return sentence
#     else:
#         tokens = re.split("(\ |/)", sentence)
#         tokens = [token_segmenter(token) for token in tokens]
#         output = u" ".join(tokens)
#         output = re.sub(' +', ' ', output)
#     return output



if __name__ == '__main__':
    file_names = os.listdir("../data/")
    for file_name in file_names[:10]:
        input = os.path.join("../data", file_name)
        lines = open(input, 'r').read().splitlines()

        segmented_lines = [character_segmenter(l) for l in lines]
        content = zip(lines, segmented_lines)
        content = ["\n".join(item) for item in content]

        output = os.path.join("../corpus/input", file_name)
        open(output, "w").write(content)
    print "finish"



