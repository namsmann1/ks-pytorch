"""Valgfri frøsetting når et forsøk skal gjentas med samme utgangspunkt."""

import random

import numpy as np
import torch


def seed_everything(seed=42):
    """Sett frø for Python, NumPy og PyTorch.

    Brukes før modelloppretting og stokking i sammenligningsforsøket.
    Vanlige bildeoppgaver trenger ikke frøsetting. Samme frø garanterer
    ikke identiske resultater på tvers av maskiner og bibliotekversjoner.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
