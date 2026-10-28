"""Felles hjelpere til kurset."""

from .data import CLASS_NAMES, download_fashion_mnist
from .tilfeldighet import seed_everything

__all__ = ["CLASS_NAMES", "download_fashion_mnist", "seed_everything"]
