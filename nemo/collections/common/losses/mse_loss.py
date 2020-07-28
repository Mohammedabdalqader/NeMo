# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
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

from torch import nn

from nemo.core.classes import Serialization, Typing, typecheck
from nemo.core.neural_types import LabelsType, LossType, NeuralType, RegressionValuesType
from nemo.utils.decorators import experimental

__all__ = ['MSELoss']


@experimental
class MSELoss(nn.MSELoss, Serialization, Typing):
    """
    CrossEntropyLoss
    """

    @property
    def input_types(self):
        """Returns definitions of module input ports.
        """
        return {
            "preds": NeuralType(tuple('B'), RegressionValuesType()),
            "labels": NeuralType(tuple('B'), LabelsType()),
        }

    @property
    def output_types(self):
        """Returns definitions of module output ports.
        loss:
            NeuralType(None)
        """
        return {"loss": NeuralType(elements_type=LossType())}

    def __init__(self, reduction='mean'):
        """
        Args:
            reduction (str): type of the reduction over the batch
        """
        super().__init__(reduction=reduction)

    @typecheck()
    def forward(self, preds, labels):
        """
        Args:
            preds: output of the classifier
            labels: ground truth labels
        """
        return super().forward(preds, labels)