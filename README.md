# PyTorch fra piksler til siffergjenkjenning

Et praktisk nybegynnerkurs på halvannen dag: seks notatbøker, små eksempler,
selvstendige oppgaver og skriftlige forklaringer. Du trenger grunnleggende Python,
men ingen erfaring med NumPy, maskinlæring eller derivasjon. Alt kjøres på CPU.

## Kom i gang

Installer [uv](https://docs.astral.sh/uv/getting-started/installation/) dersom det
ikke finnes på maskinen. Fra prosjektmappen:

```bash
make deps
uv run jupyter lab
```

`make deps` installerer også kursets `pytorch_101`-pakke i prosjektmiljøet med
[uv sitt byggesystem](https://docs.astral.sh/uv/concepts/build-backend/).
Da fungerer `from pytorch_101.utils import download_mnist` uansett hvilken mappe
notatbokkjernen starter i. Etter første installasjon: start en eventuell
åpen kjerne på nytt og velg Python-miljøet i `.venv/`.

Åpne `oppgaver/01_tensorer.ipynb`. I VS Code kan du åpne prosjektet i den
medfølgende utviklingscontaineren, eller velge `.venv/bin/python` som
Python-miljø for notatbøkene.

Kjør cellene ovenfra og ned. Les eksemplet, løs oppgaven i den tomme kodecellen,
og skriv faktiske svar i Markdown-cellene merket **Mitt svar**. Dobbeltklikk på
en Markdown-celle for å redigere; bruk Shift+Enter for å vise svaret.
Det er forventet at enkelte kontrollceller feiler frem til du har løst oppgaven.

## Rekkefølge

| Notatbok | Tema | Tid |
|---|---|---:|
| [01](oppgaver/01_tensorer.ipynb) | NumPy, tensorer og dimensjoner | 60 min |
| [02](oppgaver/02_utforsk_mnist.ipynb) | Bilder og klassefordeling | 90 min |
| [03](oppgaver/03_prediksjoner.ipynb) | Fra piksler til ti skårer | 75 min |
| [04](oppgaver/04_tap_og_gradienter.ipynb) | Tap, gradienter og læringsrate | 75 min |
| [05](oppgaver/05_lineaer_klassifikator.ipynb) | En synlig treningsløkke | 60 min |
| [06](oppgaver/06_nevralt_nettverk.ipynb) | Skjult lag, evaluering og eksperimenter | 180 min |

Dag én er seks timer. Dag to er tre timer. Pauser kommer i tillegg.
Notatbøkene har hver sin Python-kjerne: variabler følger ikke automatisk med.
Der tidligere kode skal gjenbrukes, står det uttrykkelig hva du skal kopiere.

## Data og løsninger

MNIST lastes ned til `data/` første gang datacellen kjøres. Da trenger du
internettilgang. Vi bruker et fast tilfeldig utvalg på **6 000 treningsbilder**
og **1 000 testbilder**. Klassene balanseres ikke manuelt.
`src/pytorch_101/utils/data.py` gir ferdige datasett. Vi undersøker først bildene som tabeller
med pikselverdier. Datalastere opprettes synlig i notatbøkene fra og med
notatbok 03, når vi trenger grupper av bilder.

Bildeoppgavene trekker tilfeldige eksempler, så deltakerne kan få forskjellige
bilder selv om treningsutvalget er fast. Vanlige oppgaver setter ikke tilfeldig
frø. `pytorch_101.utils.seed_everything()` samler frøsetting for Python, NumPy og PyTorch
og brukes i sammenligningsforsøket i notatbok 06. Ingen notatbok setter antall CPU-tråder.

`solutions/` inneholder kopier med samme oppgavetekster, eksempler og celler,
men med løsningskode og utfylte eksempelsvar. Prøv selv før du leser løsningen.
Tall og formuleringer i dine svar kan avvike; begrunn dem med egne resultater.

## For underviseren

[Undervisningsveiledningen](UNDERVISNING.md) beskriver gjennomføring,
læringsmål, tidsbruk og kontroll av materialet.

Teknisk referanse: [PyTorchs introduksjon](https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html)
og [MNIST-dokumentasjonen](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html).
