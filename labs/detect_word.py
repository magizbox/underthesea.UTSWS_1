from os.path import join, dirname

from os import listdir

# model = 'UETsegmenter_1'
path_Dongdu = join(dirname(dirname(__file__)), "corpus", "output_Dongdu_1")
path_UETsegmenter = join(dirname(dirname(__file__)), "corpus", "output_UETsegmenter_1")
path_jvntextpro = join(dirname(dirname(__file__)), "corpus", "output_jvntextpro_1")
path_pyvi = join(dirname(dirname(__file__)), "corpus", "output_pyvi_1")
path_vn_tokenize = join(dirname(dirname(__file__)), "corpus", "output_vntokenizer_1")
ids = listdir(path_Dongdu)
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


total_words = []


def compare_dict(filepath):
    for id in ids:
        sentences = to_list(open(join(filepath, id), "r").read())
        words = [to_words(sentence) for sentence in sentences]
        words = [word for sub_words in words for word in sub_words]
        # total_words.append(words)
        word_in_dict = []
        word_not_in_dict = []
        # total_words = [word for sub_words in total_words for word in sub_words]
        for word in total_words:
            if word in dictionary:
                word_in_dict.append(word)
            else:
                word_not_in_dict.append(word)
    return word_in_dict, word_not_in_dict


word_in_dict_DongDu, word_not_in_dict_DongDu = compare_dict(path_Dongdu)
word_in_dict_UET, word_not_in_dict_UET = compare_dict(path_UETsegmenter)
word_in_dict_jvn, word_not_in_dict_jvn = compare_dict(path_jvntextpro)
word_in_dict_pyvi, word_not_in_dict_pyvi = compare_dict(path_pyvi)
word_not_in_dict_vntokenizer, word_not_in_dict_vntokenizer = compare_dict(path_vn_tokenize)
# f_word_in_dict.write("\n".join(word_in_dict))
# f_word_not_in_dict.write("\n".join(word_not_in_dict))
# f_result.write("word in dictionary = " + str(len(word_in_dict)) + '\n')
# f_result.write("word not in dictionary = " + str(len(word_not_in_dict)) + '\n')
print 0
