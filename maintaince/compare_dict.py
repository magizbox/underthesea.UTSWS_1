# -*- coding: utf-8 -*-
from os.path import join, dirname

from os import listdir
from pandas import DataFrame, ExcelWriter
import sys
from collections import Counter

reload(sys)
sys.setdefaultencoding('utf 8')

model = "vntokenizer_1"
# path_Dongdu = join(dirname(dirname(__file__)), "corpus", "output_Dongdu_1")
path = join(dirname(dirname(__file__)), "corpus", "output_" + model)
# path_jvntextpro = join(dirname(dirname(__file__)), "corpus", "output_jvntextpro_1")
# path_pyvi = join(dirname(dirname(__file__)), "corpus", "output_pyvi_1")
# path_vn_tokenize = join(dirname(dirname(__file__)), "corpus", "output_vntokenizer_1")
ids = listdir(path)
# f_word_in_dict = open(join(dirname(__file__), "word_analysis", model, "word_in_dict.txt"), "w")
# f_word_not_in_dict = open(join(dirname(__file__), "word_analysis", model, "word_not_in_dict.txt"), "w")
# f_result = open(join(dirname(__file__), "word_analysis", model, "result"), "w")
dictionary = open('Viet74K.txt', "r").read().split('\n')
dictionary = [word.replace(' ', '_') for word in dictionary if ' ' in word]


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


def compare_dict(filepath):
    word_in_dict = []
    word_not_in_dict = []
    for id in ids:
        sentences = to_list(open(join(filepath, id), "r").read())
        words = [to_words(sentence) for sentence in sentences]
        words = [word for sub_words in words for word in sub_words]
        # total_words.append(words)
        # total_words = [word for sub_words in total_words for word in sub_words]
        for word in words:
            if word in dictionary:
                word_in_dict.append(word)
            else:
                word_not_in_dict.append(word)
    return word_in_dict, word_not_in_dict


# word_in_dict_DongDu, word_not_in_dict_DongDu = compare_dict(path_Dongdu)
writer_1 = ExcelWriter(join(dirname(__file__), "word_analysis", model, "word_in_dict.xlsx"))
writer_2 = ExcelWriter(join(dirname(__file__), "word_analysis", model, "word_not_in_dict.xlsx"))
# df = DataFrame(word_in_dict_DongDu)
# df.index = df.index.str.encode('utf-8')

word_in_dict, word_not_in_dict = compare_dict(path)
word_in_dict = Counter(word_in_dict)
df1 = DataFrame.from_dict(word_in_dict, orient='index').reset_index()
df1.to_excel(writer_1)
word_not_in_dict = Counter(word_not_in_dict)
df2 = DataFrame.from_dict(word_not_in_dict, orient='index').reset_index()
df2.to_excel(writer_2)
writer_1.save()
writer_2.save()
# word_in_dict_jvn, word_not_in_dict_jvn = compare_dict(path_jvntextpro)
# word_in_dict_pyvi, word_not_in_dict_pyvi = compare_dict(path_pyvi)
# word_not_in_dict_vntokenizer, word_not_in_dict_vntokenizer = compare_dict(path_vn_tokenize)
# words = [word_in_dict_DongDu, word_in_dict_UET, word_in_dict_jvn, word_in_dict_pyvi, word_not_in_dict_vntokenizer]

print 0
