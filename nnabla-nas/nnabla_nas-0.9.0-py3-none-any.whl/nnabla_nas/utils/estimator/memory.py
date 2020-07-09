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

import numpy as np

from .estimator import Estimator


class MemoryEstimator(Estimator):
    """Estimator for the memory used."""

    def predict(self, module):
        idm = id(module)
        if idm not in self.memo:
            self.memo[idm] = sum(np.prod(p.shape)
                                 for p in module.parameters.values())
        return self.memo[idm]
