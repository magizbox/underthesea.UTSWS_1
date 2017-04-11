# -*- coding: utf-8 -*-
import re

def sylabelize(text):
    tmp = re.findall(r"((\d+[\.,-_]*\d+)+|\w+|[^\w\s])", text, re.UNICODE)
    return u" ".join(["[%s]" % a[0] for a in tmp])

# sylabelize(u"300.000đ")
# sylabelize(u"300.000đ/1")

sentence = u"""Vụ “hot girl xứ Thanh” has 400.000VND (USD)
"""

text = sylabelize(sentence)
print text