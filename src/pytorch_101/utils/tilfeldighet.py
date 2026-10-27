"""Valgfri frøsetting når et forsøk skal gjentas med samme utgangspunkt."""

import random

import numpy as np
import torch


def seed_everything(seed=42):
    """Seed Python, NumPy og PyTorch."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
