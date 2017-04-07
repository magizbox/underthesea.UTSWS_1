# -*- coding: utf-8 -*-
from collections import Counter
import pandas as pd
from os import listdir
from underscore import _
from os.path import join


input_folder = join("..", "corpus", "input")
files = listdir(input_folder)
files = [join(input_folder, file) for file in files]
words = [open(file, "r").read().decode("utf-8").split() for file in files]
words = _.flatten(words)


counter = Counter(words)
df = pd.DataFrame.from_dict(counter, orient='index').reset_index()
df.to_excel("words.xlsx", encoding="utf-8", index=False)