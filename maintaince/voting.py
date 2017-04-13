# -*- coding: utf-8 -*-
from os.path import join, dirname
from collections import Counter
from os import listdir

from pandas import DataFrame, ExcelWriter

from to_column import to_column

# path_Dongdu = join(dirname(dirname(__file__)), "corpus", "output_Dongdu_1")
path_UETsegmenter = join(dirname(dirname(__file__)), "corpus", "output_UETsegmenter_1")
path_jvntextpro = join(dirname(dirname(__file__)), "corpus", "output_jvntextpro_1")
path_pyvi = join(dirname(dirname(__file__)), "corpus", "output_pyvi_1")
path_vn_tokenize = join(dirname(dirname(__file__)), "corpus", "output_vntokenizer_1")
# path_raw = join(dirname(dirname(__file__)), "corpus", "input")
ids = listdir(path_UETsegmenter)
writer = ExcelWriter("compare_predict.xlsx")


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
    while "  " in sentence:
        sentence = sentence.replace(" ")
    return sentences


def format_column(columns):
    while ('', 'BW') in columns:
        columns.remove(('', 'BW'))
    return columns


def voting(columns):
    a = Counter(elem[1] for elem in columns)
    word = columns[0][0]
    if a["BW"] == max(a["BW"], a["IW"], a["O"]):
        return (word, 'BW')
    elif a["IW"] == max(a["BW"], a["IW"], a["O"]):
        return (word, 'IW')
    elif a["O"] == max(a["BW"], a["IW"], a["O"]):
        return (word, 'O')


total_count = []
actual_tagged = []
for id in ids:
    doc_tagged = []
    # raw_f = open(join(path_raw, id), "r")
    # sentence_Dongdu = to_list(open(join(path_Dongdu, id), "r").read())
    sentence_UETsegmenter = to_list(open(join(path_UETsegmenter, id), "r").read())
    sentence_jvntextpro = to_list(open(join(path_jvntextpro, id), "r").read())
    sentence_pyvi = to_list(open(join(path_pyvi, id), "r").read())
    sentence_vntokenizer = to_list(open(join(path_vn_tokenize, id), "r").read())
    # sentence_raw = to_list(raw_f.read())
    # column_Dongdu = [to_column(sentence) for sentence in sentence_Dongdu]
    column_UET = [to_column(sentence) for sentence in sentence_UETsegmenter]
    column_jvn = [to_column(sentence) for sentence in sentence_jvntextpro]
    column_pyvi = [to_column(sentence) for sentence in sentence_pyvi]
    column_vntokenizer = [to_column(sentence) for sentence in sentence_vntokenizer]
    # column_Dongdu = [column for columns in column_Dongdu for column in columns]
    # column_Dongdu = format_column(column_Dongdu)
    column_UET = format_column([column for columns in column_UET for column in columns])
    column_jvn = format_column([column for columns in column_jvn for column in columns])
    column_pyvi = format_column([column for columns in column_pyvi for column in columns])
    column_vntokenizer = format_column([column for columns in column_vntokenizer for column in columns])
    # for i, j in zip(column_Dongdu, column_jvn):
    #     if i[0] != j[0]:
    for i in range(0, len(column_jvn) - 1):
        columns = [column_UET[i], column_jvn[i], column_pyvi[i], column_vntokenizer[i]]
        doc_tagged.append(voting(columns))
        a = dict(Counter(elem[1] for elem in columns))
        a['word'] = columns[0][0].decode('utf-8')
        total_count.append(a)
df = DataFrame.from_dict(total_count)
df.to_excel(writer)
writer.save()
tokenized_sentence = ''
for words in actual_tagged:
    for word in words:
        if word[1] == "I_W":
            tokenized_sentence = tokenized_sentence + "_" + word[0]
        else:
            tokenized_sentence = tokenized_sentence + word[0]
        tokenized_sentence += " "
    tokenized_sentence += '\n=================================\n'
print 0
