# Undervisningsveiledning

## Arbeidsform

Bruk korte forklaringer rett før deltakerne trenger dem. Vis et eksempel med
andre data enn oppgaven, la deltakerne overføre mønsteret til MNIST og sett av
tid til skriftlige svar i Markdown. Eksemplene er kjørbare; oppgavecellene er
tomme bortsett fra en instruksjon. Hint er tilgjengelige under oppgaveteksten.

Gå gjennom noen skriftlige svar i plenum. Be om begrunnelser og tensorformer,
også når koden gir riktig resultat. Studentene skal selv skrive visualisering,
modeller og sentrale treningssteg. Datanedlasting er gitt i `src/pytorch_101/utils/data.py`.
Deltakerne bruker bare datasettet i notatbok 02. Først når de trenger grupper
av bilder i notatbok 03, introduseres `DataLoader`, med synlig oppsett i en celle.
Det er ingen gjenopprettingspunkter eller separat forhåndsnedlasting.

## Tidsplan

Dag 1: 60 minutter tensorer, 90 minutter datautforsking, 75 minutter prediksjoner,
75 minutter gradienter og 60 minutter lineær klassifikator. Sett av siste del
av hver økt til refleksjon og felles gjennomgang. Legg pauser mellom øktene.

Dag 2, notatbok 06:

- 60 minutter: repetisjon, skjult lag og ReLU.
- 75 minutter: trening, læringskurver, feilbilder og sammenligning av 32 og 128 nevroner.
- 45 minutter: selvstendig oppsummeringsoppgave og skriftlige forklaringer.

Hvis tiden blir knapp, gjør den siste selvstendige oppgaven til en paroppgave.
Ekstraoppgavene er valgfrie. Prioriter at alle får forstå og kjøre treningsløkken.

## Faglige holdepunkter

- Skill mellom `ndim`, `shape` og antall elementer tidlig.
- Vis samme gråtonebilde som tallmatrise og som figur. Hvert tall er lysstyrken
  til én piksel, og rad og kolonne bestemmer plasseringen. La deltakerne endre
  én piksel og forklare den synlige forskjellen før de undersøker MNIST.
- Vis rå piksler fra 0 til 255 før de skalerte verdiene fra 0 til 1.
- Følg bildene fra `[B, 1, 28, 28]` til `[B, 784]` og til `[B, 10]`.
- Knytt gradienter til lokal helning. Ingen utledning av kjerneregelen er nødvendig.
- Forklar at `backward()` beregner gradienter, mens `step()` oppdaterer parametere.
- Kryssentropitapet mottar rå skårer og heltallsetiketter. Softmax brukes bare til visning.
- Skill mellom `eval()` og `no_grad()`: modellmodus og registrering av gradienter.
- Testdata brukes til avtalt rapportering, aldri til parameteroppdateringer.
  To modellstørrelser er bestemt på forhånd. Ikke la forsøket bli gjentatt tuning
  mot testsettet; et eget valideringssett hører til et videregående kurs.

Hold treningsutvalget fast gjennom kurset, men la tilfeldige bildevalg og
modellinitialisering variere i vanlige oppgaver. Det er forventet at deltakerne
ser ulike bilder og får litt ulike målinger. I det kontrollerte eksperimentet
brukes `seed_everything(42)` fra `src/pytorch_101/utils/tilfeldighet.py` før hver modell og
stokking. Hjelperen setter frø for Python, NumPy og PyTorch. Den endrer ikke
antall tråder, og ingen av notatbøkene setter antall CPU-tråder.

## Kontroll før gjennomføring

```bash
make deps
make kontroller
make kjor-losninger
```

Første kommando installerer låste avhengigheter. Andre kommando kontrollerer
notatbokformat, Python-syntaks, Markdown-svarceller og samsvar mellom oppgaver
og løsninger. Siste kommando kjører alle løsninger fra nye kjerner, laster ned
MNIST ved behov og lagrer kjørte kopier i `outputs/solutions/`.

Bruk figurene og de utskrevne målingene fra denne gjennomkjøringen som grunnlag
for forventninger på undervisningsmaskinen. Nøyaktigheten er en observasjon,
ikke et beståttkrav. Deltakerne skal kunne forklare egne resultater og vise
en modell som lærer. Kontroller også oppgaveversjonen visuelt i Jupyter og
prøv starten med en person som bare kan grunnleggende Python.

Løsninger har forklarende eksempelsvar. Der svaret avhenger av kjøringen,
viser koden konkrete tall og teksten beskriver hvordan de skal tolkes.
