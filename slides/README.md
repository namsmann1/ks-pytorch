# Fra tall til prediksjoner

En introduksjon på norsk til de tre første notatbøkene i kurset.
Forelesningen bygger begrepene fra konkrete tall og visuelle eksempler.
Notatbøkene inneholder selvstendige eksempler, oppgaver og praktisk PyTorch-bruk.

## Kjør presentasjonen

Du trenger Node.js 22.12 eller nyere. Fra reporoten:

```bash
cd slides
npm ci
npm run dev
```

Åpne http://localhost:3030. Bruk piltastene til å navigere.
Trykk `P` for presentatørvisning med notater eller åpne
http://localhost:3030/presenter. `O` åpner oversikten.
I Codespaces åpner du den videresendte porten 3030.

## Forelesningsopplegg

| Bolk | Lysbilder | Tema | Arbeid etterpå |
|---|---|---|---|
| Tensorer | 2–18 | Skalar, vektor, matrise, former, akser og matrisemultiplikasjon | `01_tensorer.ipynb` |
| Bilder | 19–26 | Piksler, kanaler, utflating, klassefordeling og nye data | `02_bilder.ipynb` |
| Prediksjoner | 27–33 | Vektet sum, bias, skårer og delte vekter | `03_prediksjoner.ipynb` |

Lysbilde 1 åpner kurset, 34 peker frem mot trening og 35 gir referanser.
Sett av omtrent 25–30 minutter til første bolk og 10–15 minutter til hver
av de to neste, pluss selvstendig arbeid.

Åpningen forutsetter ikke at studentene kjenner tensorer eller matriser.
Lysbilde 12–15 går gjennom ett matriseprodukt: først matrisene, så første
resultattall, resten av produktet og til slutt regelen for dimensjonene.
På lysbilde 13 vises svaret ved neste klikk. Eksemplet har andre tall enn
notatbøkene. Den vektede summen i bolk 3 bruker igjen samme beregning,
slik at modellbegrepene bygger på noe kjent.

HTML-kommentarene i `slides.md` er forelesernotater med forklaringer,
spørsmål og begrepsavklaringer. De vises i presentatørvisningen.
Lysbilde 23 viser samme siffer forskjøvet i bildet.

## Bygg og eksporter

```bash
npm run build
npm run export
```

Bygget ligger i `dist/`; PDF-en heter `pytorch-101.pdf`. Ved manglende
Chromium kan du kjøre `npx playwright install chromium`. Med lokal Chrome:

```bash
npm run export -- --executable-path /usr/bin/google-chrome
```

PDF-en viser det ferdige innholdet på hvert lysbilde. Presentasjonen bruker
lokale systemfonter og illustrasjoner.

## Rediger materialet

- `slides.md`: innhold, regneeksempler, forelesernotater og fagkilder.
- `styles/style.css`: farger, typografi og oppsett.
- `components/`: tallmatriser og romlig forskyvning.
- `public/mnist-seven.svg`: pikselillustrasjonen.

Generer pikselillustrasjonen på nytt fra reporoten etter Python-oppsettet:

```bash
uv run python slides/generate_assets.py
```

Skriptet bruker prosjektets datahjelper, som laster ned MNIST ved behov.
