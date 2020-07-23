import os

import requests

from .over import OvertalkDetector
from ..utils import tokenization


class NNOvertalkDetecter(object):

    def __init__(self, pre_url="http://model.ai-open.hrtps.com/v1/models/meanless:predict"):
        model_mess_path = os.path.dirname(__file__)
        vocab_file = os.path.join(model_mess_path, "..", "data", "meanful", "vocab.txt")
        self.pre_url = pre_url
        self.tokenizer = tokenization.FullTokenizer(vocab_file=vocab_file, do_lower_case=False)
        self.max_seq_length = 128

    def trans_tensor(self, texts):
        data_list = []
        for query in texts:
            tokens_a = self.tokenizer.tokenize(query)
            tokens_b = None
            if len(tokens_a) > self.max_seq_length - 2:
                tokens_a = tokens_a[0:(self.max_seq_length - 2)]

            tokens = []
            tokens.append('[CLS]')
            tokens += tokens_a
            tokens.append('[SEP]')

            segment_ids = [0 for _ in tokens]
            input_ids = self.tokenizer.convert_tokens_to_ids(tokens)
            input_mask = [1] * len(input_ids)

            while len(input_ids) < self.max_seq_length:
                input_ids.append(0)
                input_mask.append(0)
                segment_ids.append(0)

            feature = {"input_ids": input_ids, "input_mask": input_mask, "segment_ids": segment_ids, "label_ids": 0}
            data_list.append(feature)

        tensor_data = {"instances": data_list}
        return tensor_data

    def predict_doc(self, text1: str):
        tensor_data = self.trans_tensor([text1])
        resp = requests.post(self.pre_url, json=tensor_data)
        resp_json = resp.json()
        return resp_json


import requests
import json
import collections
import traceback
import numpy as np


THRESHOLD = 2.0

def convert_tokens_to_origin_index(tokens, raw_text, max_seq_length):
  all_text = u''
  start_pos = 0
  tok_to_orig_index = list()
  orig_to_tok_index = list()
  for i, token in enumerate(tokens):
    if token[:2] == "##":
      token = token[2:]
    findIdx = raw_text.find(token, start_pos)
    if findIdx == -1:
      end_pos = start_pos + len(token) # force add length
    else:
      start_pos = findIdx
      end_pos = start_pos + len(token)
    # tok_to_orig_index update
    tok_to_orig_index.append(start_pos)

    # orig_to_tok_index update
    while len(orig_to_tok_index) < start_pos:
      if orig_to_tok_index:
        orig_to_tok_index.append(orig_to_tok_index[-1])
      else:
        orig_to_tok_index.append(0)
    for j in range(start_pos, end_pos):
      orig_to_tok_index.append(i)

    start_pos = end_pos
  return tok_to_orig_index, orig_to_tok_index

def convert_text_to_features(text, tokenizer, max_seq_length, doc_stride):
    text = tokenization.convert_to_unicode(text)
    doc_tokens = tokenizer.tokenize(text)
    if len(doc_tokens) > max_seq_length:
        doc_tokens = doc_tokens[:max_seq_length]

    data_list = list()

    tok_to_orig_index, orig_to_tok_index = convert_tokens_to_origin_index(doc_tokens, text, max_seq_length)

    # split docs
    _DocSpan = collections.namedtuple(
            "DocSpan", ["start", "length"])
    doc_spans = []
    start_offset = 0
    max_tokens_for_doc = max_seq_length - 2
    while start_offset < len(doc_tokens):
        length = len(doc_tokens) - start_offset
        if length > max_tokens_for_doc:
            length = max_tokens_for_doc
        doc_spans.append(_DocSpan(start=start_offset, length=length))
        if start_offset + length == len(doc_tokens):
            break
        start_offset += min(length, doc_stride)

    for (doc_span_index, doc_span) in enumerate(doc_spans):
        tokens = []
        token_to_orig_map = {}
        segment_ids = []
        tokens.append("[CLS]")
        segment_ids.append(0)

        for i in range(doc_span.length):
            split_token_idx = doc_span.start + i
            tokens.append(doc_tokens[split_token_idx])
            segment_ids.append(0)

        tokens.append("[SEP]")
        segment_ids.append(0)

        input_ids = tokenizer.convert_tokens_to_ids(tokens)
        input_mask = [1] * len(input_ids)

        while len(input_ids) < max_seq_length:
            input_ids.append(0)
            input_mask.append(0)
            segment_ids.append(0)

        assert len(input_ids) == max_seq_length
        assert len(input_mask) == max_seq_length
        assert len(segment_ids) == max_seq_length

        data_list.append({"input_ids": input_ids, "input_mask": input_mask, "segment_ids": segment_ids})

    return data_list, orig_to_tok_index, tok_to_orig_index

def convert_result(js_result, text, orig_to_tok_index, tok_to_orig_index, data_list):
    result_list = list()
    text = tokenization.convert_to_unicode(text)
    if "predictions" in js_result:
        for index, obj in enumerate(js_result["predictions"]):
            start_logits = obj["start_logits"]
            end_logits = obj["end_logits"]
            hypo_probabilities = obj["probabilities"]
            input_mask = data_list[index]["input_mask"]
            length = np.sum(input_mask)
            null_score = start_logits[0] + end_logits[0]
            max_score = -1e5
            max_start = 0
            max_end = 0
            for i in range(1, length):
                start_score = start_logits[i]
                for j in range(i+1, length):
                    end_score = end_logits[j]
                    cur_score = start_score + end_score
                    if cur_score > max_score:
                        max_score = cur_score
                        max_start = i
                        max_end = j
            final_score = max_score - null_score
            if max_score - null_score > THRESHOLD:
                is_empty_talk = False
                start_idx = max_start
                end_idx = max_end
                orig_start = tok_to_orig_index[start_idx - 1]
                orig_end = tok_to_orig_index[end_idx - 1]
                event_part = text[orig_start: orig_end + 1]
            else:
                is_empty_talk = True
                start_idx = 0
                end_idx = 0
                event_part = ""
            result_list.append({"is_emptytalk": is_empty_talk, "emptytalk_score": final_score, "event": event_part, "tense_prob": hypo_probabilities})
    return result_list

def request_from_raw_text(vocab_file, query, model_key):
    """

    : return:
    """
    #text_list = [query]
    data_list = []
    label_list = ['0', '1', '2']
    max_seq_length = 384
    tokenizer = tokenization.FullTokenizer(vocab_file=vocab_file, do_lower_case=False)

    data_list, orig_to_tok_index, tok_to_orig_index = convert_text_to_features(query, tokenizer, max_seq_length=384, doc_stride=128)

    data = json.dumps({"instances": data_list}, ensure_ascii=False)
    #print data
    try:
        resp = requests.post("http://localhost:8501/v1/model/{}:predict".format(model_key), data=data)
        text = resp.text
        #print text
        js = json.loads(text)
        result_list = convert_result(js, query, orig_to_tok_index, tok_to_orig_index, data_list)
    except Exception as e:
        traceback.print_exc()
        raise e
    return json.dumps(result_list, ensure_ascii=False)

if __name__ == "__main__":
    text = input("input:")
    print(request_from_raw_text('./vocab.txt', text, 'emptytalk'))

