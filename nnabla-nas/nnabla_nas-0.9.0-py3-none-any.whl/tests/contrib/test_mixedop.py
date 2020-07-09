# Copyright (c) 2020 Sony Corporation. All Rights Reserved.
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

import nnabla as nn
import numpy as np
import pytest

from nnabla_nas.module import Conv
from nnabla_nas.module import MixedOp
from nnabla_nas.module import Module


class Block(Module):
    def __init__(self, in_channels, out_channels, mode='full'):
        self._sel = MixedOp(
            [
                Conv(in_channels, out_channels, (3, 3), pad=(1, 1)),
                Conv(in_channels, out_channels, (5, 5), pad=(2, 2)),
                Conv(in_channels, out_channels, (7, 7), pad=(3, 3)),
            ],
            mode=mode
        )

    def call(self, input):
        return self._sel(input)


@pytest.mark.parametrize('mode', ['max', 'sample', 'full'])
@pytest.mark.parametrize('in_channels', [3, 5, 10])
@pytest.mark.parametrize('out_channels', [8, 16, 32])
def test_mixedop(mode, in_channels, out_channels):
    module = Block(in_channels, out_channels, mode)
    input = nn.Variable([8, in_channels, 32, 32])

    output = module(input)
    assert output.shape == (8, out_channels, 32, 32)

    input.d = np.random.randn(*input.shape)
    output.forward()
    assert not np.isnan(output.d).any()
