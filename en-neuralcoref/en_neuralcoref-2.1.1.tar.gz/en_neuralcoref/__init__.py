# coding: utf8
from __future__ import unicode_literals

from pathlib import Path
from spacy.util import load_model_from_init_py, get_model_meta
from spacy.language import Language
from neuralcoref import NeuralCoref

__version__ = get_model_meta(Path(__file__).parent)['version']


def load(**overrides):
    Language.factories['neuralcoref'] = lambda nlp, **cfg: NeuralCoref(nlp.vocab, **cfg)
    return load_model_from_init_py(__file__, **overrides)