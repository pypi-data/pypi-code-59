import json
import os
import re

from tqdm import tqdm

from nlprep.file_utils import cached_path
from nlprep.middleformat import MiddleFormat
import nlp2

DATASETINFO = {
    'DATASET_FILE_MAP': {
        "squad-qg-train": "https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json",
        "squad-qg-dev": "https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json"
    },
    'TASK': "gen",
    'FULLNAME': "The Stanford Question Answering Dataset 2.0",
    'REF': {"Source": "https://rajpurkar.github.io/SQuAD-explorer/"},
    'DESCRIPTION': 'Question Generate For SQuAD 2.0'
}


def load(data):
    return data


def toMiddleFormat(path):
    dataset = MiddleFormat(DATASETINFO)
    with open(path, "r", encoding='utf8') as f:
        data = json.loads(f.read())
        data = data["data"][0]["paragraphs"]
        for i in tqdm(data):
            for qas in i["qas"]:
                q = qas['question']
                if len(qas['answers']) == 0:
                    continue
                ans = qas['answers'][0]
                ans_text = ans['text']
                context = i["context"]
                start = int(ans['answer_start'])
                end = start + len(ans_text)
                input_data = context + " [SEP] " + ans_text
                target_data = q
                dataset.add_data(input_data, target_data)

    return dataset
