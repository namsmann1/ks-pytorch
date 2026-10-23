from pathlib import Path

import torch
from torch.utils.data import Subset
from torchvision import datasets, transforms

DATADIR = Path(__file__).resolve().parents[3] / "data"
TRAIN_SAMPLES = 6_000
TEST_SAMPLES = 1_000
SEED = 42


def download_mnist(
    datadir: Path = DATADIR,
    num_train: int = TRAIN_SAMPLES,
    num_test: int = TEST_SAMPLES,
) -> tuple[Subset, Subset]:
    """
    Download MNIST and return random train + test subsets.

    Args:
        datadir: Directory in which to download the MNIST files.
        num_train: Number of training examples to select, up to 60,000.
        num_test: Number of test examples to select, up to 10,000.

    Returns:
        A pair of training and test subsets from the separate MNIST splits.
        Each example contains an f32 image tensor of shape [1, 28, 28]
        with pixel values in [0, 1], and an integer label from 0 to 9.
    """
    trainset = datasets.MNIST(datadir, train=True, download=True, transform=transforms.ToTensor())
    testset = datasets.MNIST(datadir, train=False, download=True, transform=transforms.ToTensor())
    train_indices = torch.randperm(len(trainset), generator=torch.Generator().manual_seed(SEED))[:num_train]
    test_indices = torch.randperm(len(testset), generator=torch.Generator().manual_seed(SEED + 1))[:num_test]
    return Subset(trainset, train_indices.tolist()), Subset(testset, test_indices.tolist())
