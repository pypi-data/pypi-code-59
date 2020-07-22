from torch.utils.data import Dataset
import torch
import logging
import gzip
import os
import random
from .. import SentenceTransformer
from typing import List

class ParallelSentencesDataset(Dataset):
    """
    This dataset reader can be used to read-in parallel sentences, i.e., it reads in a file with tab-seperated sentences with the same
    sentence in different languages. For example, the file can look like this (EN\tDE\tES):
    hello world     hallo welt  hola mundo
    second sentence zweiter satz    segunda oración

    The sentence in the first column will be mapped to a sentence embedding using the given the embedder. For example,
    embedder is a mono-lingual sentence embedding method for English. The sentences in the other languages will also be
    mapped to this English sentence embedding.

    When getting a sample from the dataset, we get one sentence with the according sentence embedding for this sentence.

    teacher_model can be any class that implement an encode function. The encode function gets a list of sentences and
    returns a list of sentence embeddings
    """

    def __init__(self, student_model: SentenceTransformer, teacher_model: SentenceTransformer):
        """
        Parallel sentences dataset reader to train student model given a teacher model
        :param student_model: Student sentence embedding model that should be trained
        :param teacher_model: Teacher model, that provides the sentence embeddings for the first column in the dataset file
        """
        self.student_model = student_model
        self.teacher_model = teacher_model
        self.datasets = []
        self.dataset_indices = []
        self.copy_dataset_indices = []

    def load_data(self, filepath: str, weight: int = 100, max_sentences: int = None, max_sentence_length: int = 128, batch_size: int = 8):
        """
        Reads in a tab-seperated .txt/.csv/.tsv or .gz file. The different columns contain the different translations of the sentence in the first column

        :param filepath: Filepath to the file
        :param weight: If more that one dataset is loaded with load_data: With which frequency should data be sampled from this dataset?
        :param max_sentences: Max number of lines to be read from filepath
        :param max_sentence_length: Skip the example if one of the sentences is has more characters than max_sentence_length
        :param batch_size: Size for encoding parallel sentences
        :return:
        """

        logging.info("Load "+filepath)
        parallel_sentences = []

        with gzip.open(filepath, 'rt', encoding='utf8') if filepath.endswith('.gz') else open(filepath, encoding='utf8') as fIn:
            count = 0
            for line in fIn:
                sentences = line.strip().split("\t")
                if max_sentence_length is not None and max_sentence_length > 0 and max([len(sent) for sent in sentences]) > max_sentence_length:
                    continue

                parallel_sentences.append(sentences)
                count += 1
                if max_sentences is not None and max_sentences > 0 and count >= max_sentences:
                    break
        self.add_dataset(parallel_sentences, weight=weight, max_sentences=max_sentences, max_sentence_length=max_sentence_length, batch_size=batch_size)


    def add_dataset(self, parallel_sentences: List[List[str]], weight: int = 100, max_sentences: int = None, max_sentence_length: int = 128, batch_size: int = 8):
        sentences_map = {}
        for sentences in parallel_sentences:
            if max_sentence_length is not None and max_sentence_length > 0 and max([len(sent) for sent in sentences]) > max_sentence_length:
                continue

            source_sentence = sentences[0]
            if source_sentence not in sentences_map:
                sentences_map[source_sentence] = set()

            for sent in sentences:
                sentences_map[source_sentence].add(sent)

            if max_sentences is not None and max_sentences > 0 and len(sentences_map) >= max_sentences:
                break

        source_sentences = list(sentences_map.keys())
        logging.info("Create sentence embeddings")
        labels = self.teacher_model.encode(source_sentences, batch_size=batch_size, convert_to_numpy=False)

        data = []
        for idx in range(len(source_sentences)):
            source_key = source_sentences[idx]
            label = labels[idx]
            for sent in sentences_map[source_key]:
                data.append([[self.student_model.tokenize(sent)], label])

        dataset_id = len(self.datasets)
        self.datasets.append(data)
        self.dataset_indices.extend([dataset_id] * weight)

    def __len__(self):
        return max([len(dataset) for dataset in self.datasets])

    def __getitem__(self, idx):
        if len(self.copy_dataset_indices) == 0:
            self.copy_dataset_indices = self.dataset_indices.copy()
            random.shuffle(self.copy_dataset_indices)

        dataset_idx = self.copy_dataset_indices.pop()
        return self.datasets[dataset_idx][idx % len(self.datasets[dataset_idx])]
