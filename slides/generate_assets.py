"""Lag pikselillustrasjonen fra kursets MNIST-utvalg. Kjøres fra reporoten."""
from pathlib import Path

from pytorch_101.utils import download_mnist

DESTINATION = Path(__file__).resolve().parent / "public"


def main():
    train_data, _ = download_mnist()
    image = next(image for image, label in train_data if label == 7)
    parts = ['<rect width="28" height="28" fill="#000"/>']
    for row in range(28):
        for column in range(28):
            value = round(image[0, row, column].item() * 255)
            if value:
                parts.append(
                    f'<rect x="{column}" y="{row}" width="1" height="1" '
                    f'fill="rgb({value},{value},{value})"/>'
                )
    DESTINATION.mkdir(exist_ok=True)
    (DESTINATION / "mnist-seven.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28" role="img">'
        '<title>Et håndskrevet sjutall</title>' + "".join(parts) + '</svg>\n'
    )


if __name__ == "__main__":
    main()
