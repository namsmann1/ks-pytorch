# PyTorch 101
Introduksjon til grunnprinsippene i PyTorch, samt noe bildebehandling.

## Kom i gang

### GitHub Codespaces

1. Logg inn på GitHub og åpne [kursrepoet](https://github.com/namsmann1/ks-pytorch).
2. Velg **Code → Codespaces → Create codespace on main** (eller en annen branch hvis du ønsker)
3. Vent til miljøet er ferdig satt opp. Avhengigheter installeres automatisk.
4. Åpne `oppgaver/01_tensorer.ipynb`. Velg **Select Kernel → Python Environments**
   og prosjektets `.venv`-miljø hvis du blir bedt om å velge kjerne.

Du kan kjøre notatbøkene direkte i VS Code i nettleseren.
Se [GitHubs Codespaces-veiledning](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository)
ved behov.

### Lokal kjøring

Installer [Git](https://git-scm.com/downloads) og
[uv](https://docs.astral.sh/uv/getting-started/installation/). Kjør:

```bash
git clone https://github.com/namsmann1/ks-pytorch.git
cd ks-pytorch
uv sync --all-extras
```

Bruker du VS Code lokalt, kan du åpne prosjektmappen, installere Python- og
Jupyter-utvidelsene og velge `.venv` som notatbokkjerne. Med Docker og
Dev Containers-utvidelsen kan du også velge **Dev Containers: Reopen in Container**
for å bruke samme miljø som i Codespaces.

### Arbeid med oppgavene

Kjør cellene ovenfra og ned. Les eksemplet, løs oppgaven i den tomme kodecellen,
og fyll ut Markdown-cellene merket **Mitt svar**. Dobbeltklikk på
en Markdown-celle for å redigere; bruk Shift+Enter for å vise svaret.

## Rekkefølge

| Notatbok | Tema |
|---|---|
| [01](oppgaver/01_tensorer.ipynb) | Tensorer, akser, broadcasting og matriseprodukt |
| [02](oppgaver/02_bilder.ipynb) | Bilder, klassefordeling og enkel referanse |
| [03](oppgaver/03_prediksjoner.ipynb) | Fra piksler til ti skårer |
| [04](oppgaver/04_lineaer_klassifikator.ipynb) | Trening og evaluering av Fashion-MNIST-modellen |
| [05](oppgaver/05_nevralt_nettverk.ipynb) | Skjult lag, feilanalyse og selvstendig oppsummering |
| [06 (bonus)](oppgaver/06_bonus.ipynb) | Velg et datasett og bygg din egen pipeline |

Notatbok 06 er et åpent, valgfritt prosjekt. Utforsk
[datasettene i torchvision](https://docs.pytorch.org/vision/stable/datasets.html),
velg en problemstilling og bygg en pipeline for trening og evaluering.
Løsningsnotatboken viser ett mulig prosjekt med MNIST, som lastes ned til `data/`.

## Forelesningsmateriell

[Slidev-presentasjonen](slides/slides.md) dekker notatbok 01–05 med
forelesernotater, demonstrasjoner og oppgavepauser mellom fem korte bolker.
51 lysbilder med talemanus, omtrent 90–105 minutter forelesning totalt,
samt overgang til bonusprosjektet i 06.
Se [kjøring og foreleserveiledning](slides/README.md).

```bash
cd slides
npm ci
npm run dev
```

## Data og løsninger

Se `src/pytorch_101/utils/data.py` for hjelpefunksjoner til nedlasting av data.

Fashion-MNIST lastes automatisk ned til `data/`. Notatbok 02–05 bruker de samme
faste utvalgene på 20 000 treningsbilder og 1 000 testbilder.
Bildene viser klær, sko og vesker i ti klasser; norske klassenavn finnes
i `CLASS_NAMES` fra `pytorch_101.utils`.

I hovedløpet i notatbok 04–05 trener vi med Adam, læringsrate 0.001, batchstørrelse 64 og
25 epoker. Den valgfrie sammenligningen i 05 bruker 8 og 128 skjulte nevroner.
Treningen tar lengre tid enn de innledende eksemplene.

Datasett: [Zalando Research – Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist).

## Referanser

- [PyTorch introduksjon](https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html)
