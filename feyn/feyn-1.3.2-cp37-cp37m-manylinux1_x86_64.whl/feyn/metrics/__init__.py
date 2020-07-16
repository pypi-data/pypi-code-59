"""
This module contains functions to help evaluate and compare feyn graphs and other models.
"""

from ._metrics import r2_score, confusion_matrix, segmented_loss

__all__ = [
    'r2_score',
    'confusion_matrix',
    'segmented_loss',
]

