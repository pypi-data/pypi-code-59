# ! /usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2020 NVIDIA. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

from unittest import TestCase

import pytest

import nemo.collections.nlp as nemo_nlp


class TestHuggingFace(TestCase):
    @pytest.mark.unit
    def test_list_pretrained_models(self):
        pretrained_models = nemo_nlp.nm.trainables.huggingface.BERT.list_pretrained_models()
        self.assertTrue(len(pretrained_models) > 0)
