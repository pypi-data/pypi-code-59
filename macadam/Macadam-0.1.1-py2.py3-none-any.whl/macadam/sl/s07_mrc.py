# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/5/6 21:13
# @author  : Mo
# @function: MRC(阅读理解式序列标注)
# @url     : A Uniﬁed MRC Framework for Named Entity Recognition(https://arxiv.org/abs/1910.11476)


from bert4keras.layers import ConditionalRandomField
from macadam.base.layers import SelfAttention
from macadam import keras, K, O, C, L, M
from macadam.base.graph import graph
from typing import List, Set, Tuple
import json


class Mrcgraph(graph):
    def __init__(self, hyper_parameters):
        """
        Init of hyper_parameters and build_embed.
        Args:
            hyper_parameters: hyper_parameters of all, which contains "sharing", "embed", "graph", "train", "save" and "data".
        Returns:
            None
        """
        super().__init__(hyper_parameters)
        self.num_rnn_layers = hyper_parameters["graph"].get("num_rnn_layers", 2) # 1, 2, 3
        self.crf_lr_multiplier = hyper_parameters.get("train", {}).get("crf_lr_multiplier", 1 if self.embed_type
                                                                        in ["WARD", "RANDOM"] else 3200)
        self.wclstm_embed_type = hyper_parameters["graph"].get("wclstm_embed_type", "SHORT")  # "ATTENTION", "SHORT", "LONG", "CNN"

    def build_model(self, inputs, outputs):
        """
        build_model.
        Args:
            inputs: tensor, input of model
            outputs: tensor, output of model
        Returns:
            None
        """

        logits_start = L.Dense(units=2, activation="sigmoid")(outputs)  # batch * seq_len * 2
        logits_end = L.Dense(units=2, activation="sigmoid")(outputs)    # batch * seq_len * 2
        span_start = L.Lambda(lambda x:K.repeat_elements(x=K.expand_dims(x=x, axis=2),
                                                         rep=self.length_max, axis=2))(outputs)
        span_end = L.Lambda(lambda x:K.repeat_elements(x=K.expand_dims(x=x, axis=1),
                                                       rep=self.length_max, axis=1))(outputs)
        span_matrix = L.Concatenate(axis=3)([span_start, span_end])  # batch * seq_len * seq_len * 2*hidden

        span_liner_1 = L.Dense(units=self.embed_size, activation="relu")(span_matrix)  # batch * seq_len * 2
        span_liner_1_dropout = L.Dropout(rate=self.dropout)(span_liner_1)
        span_liner_2 = L.Dense(units=self.label, activation="sigmoid")(span_liner_1_dropout)  # batch * seq_len * 2
        logits_span = L.Lambda(lambda x:K.squeeze(x, axis=-1))(span_liner_2)

        # loss
        if self.is_training:
            # 输入
            positions_start = L.Input(shape=(self.label, 2))
            positions_end = L.Input(shape=(self.label, 2))
            positions_span = L.Input(shape=(self.length_max, self.label, 2))
            y_true = [positions_start, positions_end, positions_span]

            # 输出
            self.outputs = [logits_start, logits_end, logits_span]

            # lm_metrics = L.Lambda(self.mertics_mrc, name="mertics_mrc")([y_true, self.outputs])
            lm_loss = L.Lambda(self.loss_mrc, name="loss_mrc")([y_true, self.outputs])

            self.model = M.Model(inputs, [y_true, self.outputs])
            self.model.summary(132)
            # self.metrics = [lm_metrics]
            self.loss = lm_loss
        else:
            logits_start = K.argmax(logits_start)
            logits_end = K.argmax(logits_end)
            logits_span = K.sigmoid(logits_span) # batch x seq_len x seq_len
            return logits_start, logits_end, logits_span

    def loss_mrc(self, inputs, weight_1=1, weight_2=1, weight_3=1):
        """
        loss of mrc
        Args:
            y_true: y of true from input, 正确的标签
            y_pred: y of pred from model pred, 模型预测的标签
            weight_1: weight of loss_start, 开始标签的损失权重
            weight_2: weight of loss_end,   结束标签的损失权重 
            weight_3: weight of loss_span,  指针(开始-结束)标签的损失权重 
        Returns:
            None 
        """
        y_true, y_pred = inputs[0], inputs[1]
        # 输入输出
        [positions_start, positions_end, positions_span] = y_true
        [logits_start, logits_end, logits_span] = y_pred
        # 交叉熵
        loss_start = K.categorical_crossentropy(target=logits_start, output=positions_start)
        loss_end = K.categorical_crossentropy(target=logits_end, output=positions_end)
        loss_span = K.categorical_crossentropy(target=logits_span, output=positions_span)
        # 总损失
        loss_total = weight_1 * loss_start + weight_2 * loss_end + weight_3 * loss_span

        return loss_total

    def mertics_mrc(self, inputs, batch_masks=None, label_list=None):
        """
        mertics of mrc
        Args:
            y_true: y of true from input, 正确的标签
            y_pred: y of pred from model pred, 模型预测的标签
            weight_1: weight of loss_start, 开始标签的损失权重
            weight_2: weight of loss_end,   结束标签的损失权重 
            weight_3: weight of loss_span,  指针(开始-结束)标签的损失权重 
        Returns:
            None 
        """
        batch_labels, batch_preds = inputs[0], inputs[1]
        fake_term = "#"
        true_positives = 0
        false_positives = 0
        false_negatives = 0

        if batch_masks is None:
            batch_masks = [None] * len(batch_preds)

        for preds, labels, masks in zip(batch_preds, batch_labels, batch_masks):
            if masks is not None:
                preds = trunc_by_mask(preds, masks)
                labels = trunc_by_mask(labels, masks)

            preds = [label_list[idx] if idx < len(label_list) else "O" for idx in preds]
            labels = [label_list[idx] for idx in labels]

            pred_tags = bmes_decode(char_label_list=[(fake_term, pred) for pred in preds])[1]
            golden_tags = bmes_decode(char_label_list=[(fake_term, label) for label in labels])[1]

            pred_set: Set[Tuple] = set((tag.begin, tag.end, tag.tag) for tag in pred_tags)
            golden_set: Set[Tuple] = set((tag.begin, tag.end, tag.tag) for tag in golden_tags)

            for pred in pred_set:
                if pred in golden_set:
                    true_positives += 1
                else:
                    false_positives += 1

            for pred in golden_set:
                if pred not in pred_set:
                    false_negatives += 1

        precision = true_positives / (true_positives + false_positives + 1e-10)
        recall = true_positives / (true_positives + false_negatives + 1e-10)
        f1 = 2 * precision * recall / (precision + recall + 1e-10)

        return f1 # {"span-precision": precision, "span-recall": recall, "span-f1": f1 }


def trunc_by_mask(lst: List, masks: List) -> List:
    """mask according to truncate lst"""
    out = []
    for item, mask in zip(lst, masks):
        if mask:
            out.append(item)
    return out


class Tag(object):
    def __init__(self, term, tag, begin, end):
        self.term = term
        self.tag = tag
        self.begin = begin
        self.end = end

    def to_tuple(self):
        return tuple([self.term, self.begin, self.end])

    def __str__(self):
        return str({key: value for key, value in self.__dict__.items()})

    def __repr__(self):
        return str({key: value for key, value in self.__dict__.items()})


def bmes_decode(char_label_list: List[Tuple[str, str]]) -> Tuple[str, List[Tag]]:
    idx = 0
    length = len(char_label_list)
    tags = []
    while idx < length:
        term, label = char_label_list[idx]
        current_label = label[0]

        # correct labels
        if idx + 1 == length and current_label == "B":
            current_label = "S"
        # merge chars
        if current_label == "O":
            idx += 1
            continue
        if current_label == "S":
            tags.append(Tag(term, label[2:], idx, idx + 1))
            idx += 1
            continue
        if current_label == "B":
            end = idx + 1
            while end + 1 < length and char_label_list[end][1][0] == "M":
                end += 1
            if char_label_list[end][1][0] == "E":  # end with E
                entity = "".join(char_label_list[i][0] for i in range(idx, end + 1))
                tags.append(Tag(entity, label[2:], idx, end + 1))
                idx = end + 1
            else:  # end with M/B
                entity = "".join(char_label_list[i][0] for i in range(idx, end))
                tags.append(Tag(entity, label[2:], idx, end))
                idx = end
            continue
        else:
            continue

    sentence = "".join(term for term, _ in char_label_list)
    return sentence, tags


# def precision(y_true, y_pred):
#     # Calculates the precision
#     true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
#     predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
#     precision = true_positives / (predicted_positives + K.epsilon())
#     return precision
#
# def recall(y_true, y_pred):
#     # Calculates the recall
#     true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
#     possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
#     recall = true_positives / (possible_positives + K.epsilon())
#     return recall
#
# def fbeta_score(y_true, y_pred, beta=1):
#     # Calculates the F score, the weighted harmonic mean of precision and recall.
#
#     if beta < 0:
#         raise ValueError('The lowest choosable beta is zero (only precision).')
#
#     # If there are no true positives, fix the F score at 0 like sklearn.
#     if K.sum(K.round(K.clip(y_true, 0, 1))) == 0:
#         return 0
#
#     p = precision(y_true, y_pred)
#     r = recall(y_true, y_pred)
#     bb = beta ** 2
#     fbeta_score = (1 + bb) * (p * r) / (bb * p + r + K.epsilon())
#     return fbeta_score
#
# def fmeasure(y_true, y_pred):
#     # Calculates the f-measure, the harmonic mean of precision and recall.
#     return fbeta_score(y_true, y_pred, beta=1)



