#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Ranker Mixin for adding classification metrics to ranking models in ParlAI.

Example usage:
python examples/train_model.py -m internal:bert_ranker_classifier -t internal:gender_multiclass:funpedia -mf /tmp/test11231 --train-predict True -cands inline -ecands inline -bs 4 --balance True
"""

from parlai.agents.bert_ranker.bi_encoder_ranker import BiEncoderRankerAgent
from parlai.core.opt import Opt
from parlai.utils.distributed import is_distributed
from parlai.core.torch_agent import TorchAgent, Output
from parlai.core.agents import Agent
from parlai.utils.misc import round_sigfigs, warn_once
from parlai.core.metrics import AverageMetric
from collections import defaultdict
from parlai.core.torch_classifier_agent import ConfusionMatrixMetric, WeightedF1Metric
from parlai.utils.distributed import is_primary_worker
from parlai.core.metrics import GlobalAverageMetric
from parlai.core.message import Message

import torch
import torch.nn.functional as F


class RankingClassificationMixin(Agent):
    def __init__(self, opt: Opt, shared=None):
        super().__init__(opt, shared)
        if shared is None:
            self.reset_metrics()

    def _update_confusion_matrix(self, predictions, labels):
        """
        Update the confusion matrix given the batch and predictions.

        :param batch:
            a Batch object (defined in torch_agent.py)
        :param predictions:
            (list of string of length batchsize) label predicted by the
            classifier
        """
        f1_dict = {}
        explode_labels = []
        for x in labels:
            if x is not None and len(x) > 0:
                explode_labels.append(x[0])
            else:
                explode_labels.append(None)

        class_list = [x for x in set(predictions + explode_labels) if x is not None]
        for class_name in class_list:
            prec_str = f'class_{class_name}_prec'
            recall_str = f'class_{class_name}_recall'
            f1_str = f'class_{class_name}_f1'
            precision, recall, f1 = ConfusionMatrixMetric.compute_metrics(
                predictions, explode_labels, class_name
            )
            f1_dict[class_name] = f1
            self.record_local_metric(prec_str, precision)
            self.record_local_metric(recall_str, recall)
            self.record_local_metric(f1_str, f1)
        self.record_local_metric('weighted_f1', WeightedF1Metric.compute_many(f1_dict))

    def _get_preds(self, batch_reply):
        preds = [reply.get('text') for reply in batch_reply]
        if all(x is None for x in preds):
            return None

        return preds

    def _get_labels(self, observations, labels):
        labels = [obs.get(labels) for obs in observations]
        return labels

    def batch_act(self, observations):
        # clear local metrics before anything else
        self._local_metrics.clear()

        # initialize a list of replies with this agent's id
        batch_reply = [
            Message({'id': self.getID(), 'episode_done': False}) for _ in observations
        ]

        # check if there are any labels available, if so we will train on them
        self.is_training = any('labels' in obs for obs in observations)

        # create a batch from the vectors
        batch = self.batchify(observations)

        if (
            'label_vec' in batch
            and 'text_vec' in batch
            and batch.label_vec is not None
            and batch.text_vec is not None
        ):
            # tokens per batch
            # we divide by the binary is_primary_worker() so that the numerator is
            # num_tokens in all workers, and the denominator is 1.
            tpb = GlobalAverageMetric(
                (batch.label_vec != self.NULL_IDX).sum().item(),
                float(is_primary_worker()),
            )
            self.global_metrics.add('tpb', tpb)

        if self.is_training:
            output = self.train_step(batch)
        else:
            with torch.no_grad():
                # save memory and compute by disabling autograd.
                # use `with torch.enable_grad()` to gain back gradients.
                output = self.eval_step(batch)

        if output is not None:
            # local metrics are automatically matched up
            self.match_batch(batch_reply, batch.valid_indices, output)

        preds = self._get_preds(batch_reply)
        if 'labels' in observations[0]:
            labels = 'labels'
        elif 'eval_labels' in observations[0]:
            labels = 'eval_labels'
        else: 
            labels = None

        if preds is not None and labels is not None:
            labels_lst = self._get_labels(observations, labels)
            self._update_confusion_matrix(preds, labels_lst)

        # broadcast the metrics back
        for k, values in self._local_metrics.items():
            if len(values) != len(batch.valid_indices):
                raise IndexError(
                    f"Batchsize mismatch on metric {k} (got {len(values)}, "
                    f"expected {len(batch.valid_indices)}"
                )
            for i, value in zip(batch.valid_indices, values):
                if 'metrics' not in batch_reply[i]:
                    batch_reply[i]['metrics'] = {}
                batch_reply[i]['metrics'][k] = value

        # Make sure we push all the metrics to main thread in hogwild/workers
        self.global_metrics.flush()

        return batch_reply


class BertRankerClassifierAgent(RankingClassificationMixin, BiEncoderRankerAgent):
    """
    Bert BiEncoder that computes F1 metrics
    """

    pass
