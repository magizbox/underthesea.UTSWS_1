from os.path import dirname, join
from os import listdir
from collections import Counter

path_Dongdu = join(dirname(dirname(__file__)), "corpus", "output_DongDu_1")
path_UETsegmenter = join(dirname(dirname(__file__)), "corpus", "output_UETsegmenter_1")
path_jvntextpro = join(dirname(dirname(__file__)), "corpus", "output_jvntextpro_1")
path_pyvi = join(dirname(dirname(__file__)), "corpus", "output_pyvi_1")
path_vn_tokenize = join(dirname(dirname(__file__)), "corpus", "output_vntokenizer_1")
path_raw = join(dirname(dirname(__file__)), "corpus", "input")
ids = listdir(path_Dongdu)
f_dict = open("dict.txt", "a")
f_error = open("error.txt", "a")


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


def intersect(a, b, c, d, e):
    return list(set(a) & set(b) & set(c) & set(d) & set(e))


dict = []


def error_word(words, not_freqs):
    return [word for word in words if word in not_freqs]


for id in ids:
    Dongdu = open(join(path_Dongdu, id), "r")
    UETsegmenter = open(join(path_UETsegmenter, id), "r")
    jvntextpro = open(join(path_jvntextpro, id), "r")
    pyvi = open(join(path_pyvi, id), "r")
    vn_tokenize = open(join(path_vn_tokenize, id), "r")
    raw_f = open(join(path_raw, id), "r")
    sentence_Dongdu = to_list(Dongdu.read())
    sentence_UETsegmenter = to_list(UETsegmenter.read())
    sentence_jvntextpro = to_list(jvntextpro.read())
    sentence_pyvi = to_list(pyvi.read())
    sentence_vntokenizer = to_list(vn_tokenize.read())
    sentence_raw = to_list(raw_f.read())
    for (Dongdu, UETsegmenter, jvntextpro, pyvi, vn_tokenize, raw) in zip(sentence_Dongdu, sentence_UETsegmenter,
                                                                          sentence_jvntextpro, sentence_pyvi,
                                                                          sentence_vntokenizer, sentence_raw):
        words_Dongdu = to_words(Dongdu)
        words_UETsegmenter = to_words(UETsegmenter)
        words_jvntextpro = to_words(jvntextpro)
        words_pyvi = to_words(pyvi)
        words_vntokenizer = to_words(vn_tokenize)

        # words = intersect(words_Dongdu, words_UETsegmenter, words_jvntextpro, words_pyvi, words_vntokenizer)
        # open a write file a word have '_' insinde it

        words = []
        words.extend(words_Dongdu)
        words.extend(words_UETsegmenter)
        words.extend(words_jvntextpro)
        words.extend(words_pyvi)
        words.extend(words_vntokenizer)
        uniques = set(words)

        not_freqs = [item for item in uniques if words.count(item) < 4]
        error_DongDu = error_word(words_Dongdu, not_freqs)
        error_UETsegmenter = error_word(words_Dongdu, not_freqs)
        error_jvntextpro = error_word(words_Dongdu, not_freqs)
        error_pyvi = error_word(words_Dongdu, not_freqs)
        error_vntokenizer = error_word(words_Dongdu, not_freqs)

        freqs = [item for item in uniques if words.count(item) > 3]
        items = [item for item in freqs if '_' in item and item != '_']
        dict.append(items)
dictionary = [i for sub_dict in dict for i in sub_dict]
dictionary = set(dictionary)
print 0
