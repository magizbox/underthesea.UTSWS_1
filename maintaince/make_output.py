# -*- coding: utf-8 -*-
import requests
import json
from os import listdir
from os.path import join, dirname

file_path = join(dirname(dirname(__file__)), "corpus", "input")
files_input = listdir(file_path)
files_input = files_input[:1]
for file in files_input:
    file_input = join(file_path, file)
    text = open(file_input, "r").read()
    url = "http://127.0.0.11:8082/tokenize"
    data = {'text': text}
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    out_file_path = join(dirname(dirname(__file__)), "corpus", "output")
    fout = open(join(out_file_path, file), "w")
    fout.write(json.dumps(r.text, ensure_ascii=False).encode('utf-8'))
