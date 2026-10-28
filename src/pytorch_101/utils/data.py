from pathlib import Path

import torch
from torch.utils.data import Subset
from torchvision import datasets, transforms

DATADIR = Path(__file__).resolve().parents[3] / "data"
TRAIN_SAMPLES = 20_000
TEST_SAMPLES = 1_000
SEED = 42
CLASS_NAMES = (
    "T-skjorte/topp",
    "Bukse",
    "Genser",
    "Kjole",
    "Kåpe",
    "Sandal",
    "Skjorte",
    "Joggesko",
    "Veske",
    "Ankelstøvel",
)


def download_fashion_mnist(
    datadir: Path = DATADIR,
    num_train: int = TRAIN_SAMPLES,
    num_test: int = TEST_SAMPLES,
) -> tuple[Subset, Subset]:
    """Last ned Fashion-MNIST og hent faste tilfeldige trenings- og testutvalg.

    `datadir` angir datamappen. `num_train` og `num_test` angir antall bilder
    fra de separate trenings- og testdelene, med opptil 60 000 og 10 000 bilder.
    Hvert bilde er en float32-tensor med form [1, 28, 28] og verdier i [0, 1].
    Etiketten er en klasseindeks fra 0 til 9; navnene finnes i `CLASS_NAMES`.
    """
    trainset = datasets.FashionMNIST(datadir, train=True, download=True, transform=transforms.ToTensor())
    testset = datasets.FashionMNIST(datadir, train=False, download=True, transform=transforms.ToTensor())
    train_indices = torch.randperm(len(trainset), generator=torch.Generator().manual_seed(SEED))[:num_train]
    test_indices = torch.randperm(len(testset), generator=torch.Generator().manual_seed(SEED + 1))[:num_test]
    return Subset(trainset, train_indices.tolist()), Subset(testset, test_indices.tolist())
