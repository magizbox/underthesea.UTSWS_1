# -*- coding: utf-8 -*-
import os
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')

punctuations = open("punctuation.txt", "r").read().splitlines()
punctuations = [unicode(p) for p in punctuations]

regex = re.compile(r"(\d \. \d)")
regex1 = re.compile(r"\d \, \d")
regex2 = re.compile(r"\@")
url = re.compile(r"((http)|(https))+\:+//")


# exception = [',', '.', '@']


def character_segmenter(sentences):
    count = 0
    if url.search(sentences):
        return sentences
    for punctuation in punctuations:
        if sentences[len(sentences) - 1] == punctuation:
            count += 1
        sentences = sentences.replace(punctuation, " {} ".format(punctuation))
    # sentences = sentences.replace(" . ", ".")
    if regex.search(sentences):
        sentences = sentences.replace(" . ", ".")
        sentences = sentences.replace(". ", " . ")
    if regex1.search(sentences):
        sentences = sentences.replace(" , ", ",")
    if regex2.search(sentences):
        sentences = sentences.replace(" @ ", "@")
        sentences = sentences.replace(" . ", ".")
        sentences = sentences.replace(". ", " . ")
    while "  " in sentences:
        sentences = sentences.replace("  ", " ")
    if count != 0:
        sentences = sentences[:-1]

    return sentences

#
# if __name__ == '__main__':
#     file_names = os.listdir("../data/")
#     for file_name in file_names:
#         input = os.path.join("../data", file_name)
#         lines = open(input, 'r').read().splitlines()
#
#         segmented_lines = [character_segmenter(l) for l in lines]
#         content = zip(lines, segmented_lines)
#         content = "\n\n".join(["\n".join(item) for item in content])
#
#         output = os.path.join("../corpus/input", file_name)
#         open(output, "w").write(content)
#     print "finish"


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
