import difflib
from os.path import dirname, join
from os import listdir

path_UETsegmenter = join(dirname(dirname(__file__)), "corpus", "output_UETsegmenter_1")
path_jvntextpro = join(dirname(dirname(__file__)), "corpus", "output_jvntextpro_1")
path_raw = join(dirname(dirname(__file__)), "corpus", "input")
f_sentence_error = open("sentence_error.txt", "a")
f_words_error = open("words_error.txt", "a")
f_result = open("result", "w")
ids = listdir(path_UETsegmenter)
total_similar = []
total_sentence = []
total_similar_word = []


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


def find_diferent(words, sentence):
    count = 0
    result = []
    similar = []
    for i in range(0, len(words)):
        if (words[i] == sentence[count:(count + 1 + len(words[i]))]) or (
                    words[i] == sentence[count:(count + len(words[i]))]):
            similar.append(words[i])
        else:
            result.append(words[i])
        count += (len(words[i]) + 1)
    return similar


total_word = 0
for id in ids:
    UETsegmenter = open(join(path_UETsegmenter, id), "r")
    jvntextpro = open(join(path_jvntextpro, id), "r")
    raw = open(join(path_raw, id), "r")
    sentence_UETsegmenter = to_list(UETsegmenter.read())
    sentence_jvntextpro = to_list(jvntextpro.read())
    sentence_raw = to_list(raw.read())
    total_sentence.append(sentence_raw)
    similar = [sentence for sentence in sentence_UETsegmenter if sentence in sentence_jvntextpro]
    for UET, jvn, raw_sentence in zip(sentence_UETsegmenter, sentence_jvntextpro, sentence_raw):
        if UET != jvn:
            f_sentence_error.write("Raw: %s\n" % raw_sentence)
            f_sentence_error.write("UET: %s\n" % UET)
            f_sentence_error.write("jvn: %s\n" % jvn)
            f_sentence_error.write("\n")
        f_sentence_error.write("\n==================================\n\n")
    total_similar.append(similar)

    for (UET, jvn, raw_words) in zip(sentence_UETsegmenter, sentence_jvntextpro, sentence_raw):
        f_words_error.write(raw_words + "\n")
        words_UET = to_words(UET)
        words_jvn = to_words(jvn)
        diff1 = difflib.ndiff(words_UET, words_jvn)
        diff2 = difflib.ndiff(words_jvn, words_UET)
        similar_word = find_diferent(words_jvn, UET)
        total_word += len(max(words_UET, words_jvn))
        total_similar_word.append(similar_word)
        f_words_error.write("UET: %s\n" % ', '.join(x[2:] for x in diff1 if x.startswith('- ')))
        f_words_error.write("jvn: %s\n" % ', '.join(x[2:] for x in diff2 if x.startswith('- ')))
        f_words_error.write("\n==================================\n\n")
total_similar_word = [word for words in total_similar_word for word in words]

total_similar = [sentence for sentences in total_similar for sentence in sentences]
total_sentence = [sentence for sentences in total_sentence for sentence in sentences]
f_result.write("similar = %0.2f percent\n" % float(float(len(total_similar)) / float(len(total_sentence))))
f_result.write("similar word = %0.2f percent\n" % float(float(len(total_similar_word)) / float(total_word)))
