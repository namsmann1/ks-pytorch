"""Felles hjelpere til kurset."""

from .data import download_mnist
from .tilfeldighet import seed_everything

__all__ = ["download_mnist", "seed_everything"]
