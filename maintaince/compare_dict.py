# -*- coding: utf-8 -*-
from os.path import join, dirname
import underthesea
from os import listdir
import pandas as pd
from collections import Counter
#
# reload(sys)
# sys.setdefaultencoding('utf 8')

model = "vntokenizer_1"
path = join(dirname(dirname(__file__)), "corpus", "output_" + model)
ids = listdir(path)
dictionary = open('Viet74K.txt', "r").read().split('\n')
words_74K = underthesea.corpus.viet_dict_74K.words


def to_list(sentences):
    sentences = sentences.replace('. . .', '...')
    sentences = sentences.replace('\n\n', '\n')
    sentences = sentences.split('\n')
    sentences = [sentence for sub_sentences in sentences for sentence in sub_sentences.split(' . ')]
    sentences = [sentence for sub_sentences in sentences for sentence in sub_sentences.split(' .') if
                 ' ...' not in sentences]
    sentences = [sentence for sub_sentences in sentences for sentence in sub_sentences.split('_.')]
    while "" in sentences:
        sentences.remove("")
    return sentences


def to_words(sentence):
    return [word for word in sentence.split(' ')]


def get_words(filepath):
    words_total = []
    for id in ids:
        sentences = to_list(open(join(filepath, id), "r").read())
        words = [to_words(sentence) for sentence in sentences]
        words = [word.replace('_', ' ') for sub_words in words for word in sub_words]
        words_total.append(words)
    words_total = [word.lower() for sub_words in words_total for word in sub_words]
    words_total = [word.decode("utf-8") for word in words_total]
    return words_total


words = get_words(path)
words_count = pd.DataFrame.from_dict(Counter(words), orient='index')
in_dict = list(set(words).intersection(set(words_74K)))
not_in_dict = list(set(words).difference(set(words_74K)))

in_dict = words_count.ix[in_dict, :].reset_index()
in_dict.columns = ["word", "count"]
out_dict = words_count.ix[not_in_dict, :].reset_index()
out_dict.columns = ["word", "count"]

# in_dict.to_excel("in.xlsx", index=False)
# out_dict.to_excel("out.xlsx", index=False)
