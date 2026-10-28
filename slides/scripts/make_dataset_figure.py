"""Lag lysbildets datasettfigur. Kjør med prosjektets Python-miljø fra repo-roten."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from pytorch_101.utils import CLASS_NAMES, download_fashion_mnist

train_data, _ = download_fashion_mnist()
figure, axes = plt.subplots(2, 5, figsize=(11, 4.5), facecolor="#faf9f5")
seen = set()
for image, label in train_data:
    if label in seen:
        continue
    seen.add(label)
    axis = axes.flat[label]
    axis.imshow(image[0], cmap="gray", vmin=0, vmax=1, interpolation="nearest")
    axis.set_title(CLASS_NAMES[label], fontsize=12)
    axis.axis("off")
    if len(seen) == 10:
        break
figure.tight_layout()
output_path = Path(__file__).resolve().parents[1] / "public" / "fashion-mnist.png"
figure.savefig(output_path, dpi=160, facecolor=figure.get_facecolor())
plt.close(figure)
