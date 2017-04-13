# -*- coding: utf-8 -*-
import difflib

sentence_1 = "Hoảng với những bộ_cánh khoe vòng một quá táo_bạo của Phi_Thanh_Vân"
sentence_2 = "Hoảng với những bộ_cánh khoe vòng một quá táo_bạo của Phi Thanh_Vân"


def to_words(sentence):
    return [word for word in sentence.split(' ')]


print difflib.get_close_matches(to_words(sentence_1), to_words( sentence_2))
