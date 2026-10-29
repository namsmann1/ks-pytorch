---
theme: default
title: PyTorch 101
info: 32 lysbilder med forelesernotater. Omtrent 50–60 minutter, fordelt over kurset.
class: cover
colorSchema: light
aspectRatio: 16/9
canvasWidth: 1100
fonts:
  sans: DejaVu Sans
  mono: DejaVu Sans Mono
  provider: none
htmlAttrs:
  lang: nb
transition: none
mdc: true
drawings:
  enabled: true
---

# PyTorch 101

<div class="lead">Tensorer, bildeklassifikasjon og nevrale nettverk</div>

<!--
Målet er å bygge og forstå en liten bildemodell. Vi tar teorien i fem korte bolker og bruker den med en gang i notatbøkene. Start med helheten før detaljene.
-->

---

# Bildeklassifikasjon

<img src="/fashion-mnist.png" class="h-55 mx-auto" alt="Ett bilde fra hver av de ti Fashion-MNIST-klassene" />

<div class="flow"><div class="box">Bilde</div><span>→</span><div class="box">Modell</div><span>→</span><div class="box">Ti klasseskårer</div><span>→</span><div class="box">Predikert klasse</div></div>

Modellen trenes på merkede bilder og evalueres på et separat testsett.

<div class="small">Fashion-MNIST · Zalando Research · MIT</div>

<!--
Modellen skal skille klær, sko og vesker i ti klasser. Vi skriver ikke regler for hvert plagg. Vi bruker eksempler med fasit til å tilpasse modellen. Noen klasser ligner hverandre, så vi skal også undersøke feilene.
-->

---

# Nevrale nettverk

<div class="flow"><div class="box">Innganger<br>pikselverdier</div><span>→</span><div class="box">Skjult lag<br>mellomverdier</div><span>→</span><div class="box">Utganger<br>klasseskårer</div></div>

Et nevralt nettverk består av lag med lærbare parametere: **vekter og bias**.

Ulineære aktiveringsfunksjoner mellom lagene gjør at nettverket kan representere ulineære sammenhenger.

<div class="note">PyTorch gir oss tensorer, modellag og automatisk beregning av gradienter.</div>

<!--
Et nettverk er en sammensatt funksjon med justerbare parametere. Skjult betyr at vi ikke gir mellomverdiene en egen fasit. Treningen justerer vektene ut fra sluttresultatet. Vi begynner med en enklere lineær modell for å lære delene, og kommer tilbake til nettverket i siste bolk.
-->

---

# Nevroner, vekter og aktiveringer

<NetworkDiagram />


<!--
Sirklene inneholder verdier som beregnes for ett eksempel. Linjene representerer vekter, som er modellparametere. Velg et skjult nevron med knappene for å se dets inngående vekter og beregning. Linjetykkelsen viser absoluttverdien til vekten, og fargen viser fortegnet. Alle forbindelser til utgangene er tegnet nøytralt. Utgangene er merket z1 og z2; utregningen viser bare det valgte skjulte nevronet. Vektetikettene følger de tre inngangene ovenfra og ned. Bias vises ved siden av nevronvalget. Først beregnes den vektede summen z, deretter aktiveringen h. Verdiene endres med inndata; vektene endres under trening. ReLU-verdier er ikke begrenset til én, og utgangene er rå skårer. Diagramideen er inspirert av 3Blue1Browns introduksjon, men beregningen og figuren er laget for dette kurset.
-->

---

# Tensorer og former

| Tensor | Eksempel på form | Betydning |
|---|---|---|
| Skalar | `[]` | Ett tall |
| Vektor | `[3]` | Tre tall langs én akse |
| Matrise | `[2, 3]` | To rader, tre kolonner |
| Bildebatch | `[B, C, H, W]` | Bilder, kanaler, høyde, bredde |

```python
import torch
values = torch.tensor([[1., 2., 3.], [4., 5., 6.]])
values.shape  # torch.Size([2, 3])
```

<!--
Tensor er fellesnavnet for tall organisert langs null eller flere akser. Formen forteller hvor mange verdier hver akse har. Skill mellom antall akser og antall tall. PyTorch bruker samme datatype for disse strukturene.
-->

---

# Indeksering og akser

```python
values = torch.tensor([[1., 2., 3.], [4., 5., 6.]])
values[0]                  # Første rad: [1., 2., 3.]
values[:, 1]               # Andre kolonne: [2., 5.]
values.mean(dim=1)         # Ett gjennomsnitt per rad: [2., 5.]
values + 2                 # Legg 2 til hvert tall
```

**`dim` velger aksen vi regner over.**

`shape`: organisering · `dtype`: talltype · `device`: CPU eller GPU

<!--
Radene kan være eksempler og kolonnene målinger. Indekser starter på null. Ved gjennomsnitt over dim én forsvinner kolonneaksen, og vi får ett tall per rad. Vi bruker desimaltall for beregningene og heltall for klasseindekser. Detaljene prøver dere selv.
-->

---

# Matrisemultiplikasjon

$$
C=AB,\qquad C_{ik}=\sum_{j=1}^{D} A_{ij}B_{jk}
$$

$$
[B,D]\; @\; [D,K]\;\longrightarrow\;[B,K]
$$

Elementet $C_{ik}$ er prikkproduktet av rad $i$ i $A$ og kolonne $k$ i $B$.

```python
result = inputs @ weights
```

NB: Husk dimensjoner!

<!--
Pek på aksen D som summeres bort. B kan være antall eksempler, D antall innganger og K antall utganger. Formelen beskriver hvert enkelt tall i resultatet. Vi trenger bare ett konkret eksempel før dere prøver selv.
-->

---

# Matrisemultiplikasjon: eksempel

$$
\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}
\begin{bmatrix}2&0\\1&1\\0&2\end{bmatrix}
=\begin{bmatrix}4&8\\13&17\end{bmatrix}
$$

Første tall: $1\cdot2+2\cdot1+3\cdot0=4$.

```python
inputs = torch.tensor([[1., 2., 3.], [4., 5., 6.]])
weights = torch.tensor([[2., 0.], [1., 1.], [0., 2.]])
result = inputs @ weights  # Form [2, 2]
```

**`@`** beregner matriseprodukt. **`*`** ganger elementvis.

<!--
Vis bare beregningen av øverste venstre tall. Resten følger samme regel. To eksempler med tre innganger blir to eksempler med to utganger. Elementvis gange er en annen operasjon; disse to formene passer heller ikke sammen for elementvis gange.
-->

---
class: exercise
---

# Oppgaver 01 · Tensorer

`oppgaver/01_tensorer.ipynb`

Indeksering, reduksjoner, broadcasting og matrisemultiplikasjon.

<!--
Stopp forelesningen her og la studentene arbeide. Bruk eksemplene og hintene i notatboken ved behov.
-->

---

# Bilder som tensorer

<div class="cols">
<div>
<PixelGrid />
</div>
<div>

Én piksel = én lysstyrke.

**0 er svart. 1 er hvitt.**

```python
image[0, row, column]
```

Et gråtonebilde: `[1, H, W]`

Et RGB-bilde: `[3, H, W]`

</div></div>

<!--
Koble tallene i rutenettet til lysstyrkene. Kanalaksen kommer først i bildene vi bruker. Et RGB-bilde har tre kanaler. I notatboken endrer dere en piksel og ser hva som skjer.
-->

---

# Pikselverdier og skalering

<PixelValues />

```python
raw_pixels = torch.tensor([0, 128, 255], dtype=torch.uint8)
pixels = raw_pixels.float() / 255
# tensor([0.0000, 0.5020, 1.0000])
```

Skalering endrer tallområdet, men bevarer relative lysstyrker.

<!--
Dra i skyveknappen og sammenlign gråtonen med råverdien og den skalerte verdien. Dette er samme operasjon som ToTensor utfører for råbildene i Fashion-MNIST. Skillet mellom datatype og skala er viktig: float alene deler ikke på 255. Verdien 128 blir omtrent 0,502. PDF-en viser startverdien 204.
-->

---

# Fargekanaler

<ImageChannels />

```python
red = image[0]    # [H, W]
green = image[1]  # [H, W]
blue = image[2]   # [H, W]
```

Fashion-MNIST har én gråtonekanal: `[1, 28, 28]`.

<!--
Dette er et konstruert RGB-bilde med to ganger to piksler. Hver kanal er en matrise, og verdier på samme posisjon beskriver samme piksel. Øverste venstre piksel har R=224, G=96 og B=48. I figuren vises råverdier; etter skalering deles hver kanal på 255. Indekseringen i koden gjelder et RGB-bilde, ikke Fashion-MNIST.
-->

---

# Bildeform og batchakse

<div class="flow"><div class="box">Pikselmatrise<br><code>[28, 28]</code></div><span>→</span><div class="box">Én kanal<br><code>[1, 28, 28]</code></div><span>→</span><div class="box">64 bilder<br><code>[64, 1, 28, 28]</code></div></div>

```python
image.shape             # [1, 28, 28]
image.squeeze(0).shape  # [28, 28], for visning med imshow
```

| Akse | Betydning |
|---|---|
| `B` | Antall bilder i batchen |
| `C` | Antall kanaler per bilde |
| `H, W` | Høyde og bredde i piksler |

<!--
Skillet mellom en kanalakse og en batchakse er ofte vanskelig i starten. En ekstra akse endrer ikke pikselverdiene. Squeeze med eksplisitt akse null fjerner bare den ene gråtonekanalen. Batchen samler flere separate bilder; den endrer ikke oppløsningen. DataLoader i neste bolk viser hvordan slike batcher opprettes.
-->

---

# Fashion-MNIST

```python
from pytorch_101.utils import CLASS_NAMES, download_fashion_mnist

train_data, test_data = download_fashion_mnist()
image, label = train_data[0]
image.shape          # [1, 28, 28]
CLASS_NAMES[label]   # Navnet på riktig klasse
```

**10 klasser · 20 000 treningsbilder · 1 000 testbilder**


<!--
Dette er kursets faste utvalg. Et datasett gir oss et bilde og en etikett. Etiketten er et heltall fra null til ni. Klassefordelingen gir en nyttig referanse: hvor godt kan vi gjøre det bare ved å gjette den vanligste klassen?
-->

---

# Klassefordeling og referansenøyaktighet

Et tenkt datasett med 100 bilder:

| Klasse | Antall |
|---|---:|
| T-skjorte | 80 |
| Bukse | 10 |
| Sko | 10 |

En modell som alltid velger T-skjorte får **80 % nøyaktighet**, men finner ingen bukser eller sko.

```python
baseline_accuracy = max(class_counts) / sum(class_counts)
```

<!--
Samlet nøyaktighet må tolkes i lys av klassefordelingen. Her er 80 prosent mulig uten å bruke bildene i det hele tatt. I notatboken beregnes flertallsklassen og dens nøyaktighet på treningsutvalget. For en testreferanse velges klassen fra trening, og treffandelen måles separat på testdata. Tilfeldig, uniform gjetting blant ti klasser har forventet nøyaktighet 10 prosent.
-->

---
class: exercise
---

# Oppgaver 02 · Bilder

`oppgaver/02_bilder.ipynb`

Visualisering av bilder, klassefordeling og nøyaktighet ved flertallsgjetting.

<!--
Stopp forelesningen her og la studentene arbeide. Bruk eksemplene og hintene i notatboken ved behov.
-->

---

# Batcher og DataLoader

```python
from torch.utils.data import DataLoader

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
images, labels = next(iter(train_loader))
images.shape  # [64, 1, 28, 28]
labels.shape  # [64]
```

**Dataset** henter eksempler. **DataLoader** samler dem i grupper.

`shuffle=True` stokker rekkefølgen for hver gjennomgang.

<!--
Batchaksen skiller bildene fra hverandre. Vi bruker de samme modellvektene på alle bildene. Den siste batchen kan være mindre. Dette er første gang studentene trenger DataLoader, i notatbok 03.
-->

---

# Lineær klassifikasjon

$$
Z=XW+b
$$

$$
[B,784]\;@\;[784,10]+[10]\;\longrightarrow\;[B,10]
$$

```python
flat_images = images.flatten(start_dim=1)
weights = torch.randn(784, 10) * 0.01
bias = torch.zeros(10)
scores = flat_images @ weights + bias
```

**Vekter** bestemmer bidragene. **Bias** gir ett konstantledd per klasse.

<!--
Hver rad er ett bilde, og hver kolonne i resultatet er en klasse. Utflating beholder alle pikselverdiene og batchaksen. Her gjenkjenner vi matriseproduktet fra første bolk. Vektene er tilfeldige og modellen har ennå ikke lært.
-->

---

# nn.Linear og nn.Sequential

```python
from torch import nn

model = nn.Sequential(nn.Flatten(), nn.Linear(784, 10))
scores = model(images)             # [B, 10]
predictions = scores.argmax(dim=1) # [B]
```

**`nn.Linear`** eier vekter og bias. **`nn.Sequential`** setter lag i rekkefølge.

Skårene kalles **logits** og er ikke sannsynligheter. Predikert klasse er indeksen til den høyeste skåren.

Nøyaktighet = antall riktige / antall eksempler.

<!--
Linear gjør den samme beregningen som vi nettopp skrev for hånd. Argmax velger klassekolonnen med størst skår for hvert bilde. Softmax kan gjøre skårene om til sannsynligheter, men er ikke nødvendig for å velge vinneren. Notatboken undersøker også antall parametere.
-->

---
class: exercise
---

# Oppgaver 03 · Prediksjoner

`oppgaver/03_prediksjoner.ipynb`

Vektede summer, klasseskårer og en lineær modell med `nn.Linear`.

<!--
Stopp forelesningen her og la studentene arbeide. Bruk eksemplene og hintene i notatboken ved behov.
-->

---

# Trening av modellparametere

<div class="flow"><div class="box">Bilder</div><span>→</span><div class="box">Modell</div><span>→</span><div class="box">Skårer</div><span>→</span><div class="box">Tap mot fasiten</div></div>

1. Beregn prediksjoner og tap (**forward**).
2. Beregn hvordan parameterne påvirker tapet (**backward**).
3. Juster vekter og bias (**optimizer**).

Treningen justerer parameterne for å redusere tapet på treningsdataene.

<!--
Start med tilfeldige vekter. Tapsfunksjonen gir et signal om hvor godt skårene passer til fasiten. Vi gjentar små oppdateringer på batcher. Backward regner ut gradienter; optimizer bruker dem til å endre parameterne.
-->

---

# Kryssentropi og nøyaktighet

Fasit: klasse 1.

| Sannsynligheter | Predikert klasse | Riktig? | Tap $-\log(p_y)$ |
|---|---|---|---:|
| `[0.4, 0.6]` | 1 | Ja | 0.51 |
| `[0.1, 0.9]` | 1 | Ja | 0.11 |

```python
loss_fn = nn.CrossEntropyLoss()
loss = loss_fn(scores, labels)
```

Send **rå skårer** `[B, 10]` og **klasseindekser** `[B]` inn i tapsfunksjonen.

<!--
Begge prediksjonene er riktige, men den andre støtter fasiten sterkere. Tabellen viser sannsynligheter for å forklare tapet. I koden sender vi logits direkte til CrossEntropyLoss, uten softmax eller argmax. Etikettene er int64. Resultatet er ett gjennomsnittlig tapstall for batchen.
-->

---

# Gradienter og læringsrate

Gradienten beskriver hvordan tapet endres ved små endringer i parameterne.

Enkel gradient descent:

$$
w_{\mathrm{ny}}=w-\eta\frac{\partial L}{\partial w}
$$

**Læringsraten** $\eta$ styrer størrelsen på steget.

```python
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
```

Vi bruker **Adam**, som også tar hensyn til tidligere gradienter.

<!--
Hvis gradienten er positiv, kan vi prøve å senke parameteren for å redusere tapet lokalt. Vi trenger ikke derivere nettverket for hånd: PyTorch gjør det. Formelen viser enkel gradient descent, ikke hele Adam-regelen. Et enkelt steg garanterer ikke bedre ytelse på usette data.
-->

---

# Én parameteroppdatering

```python {all|1|2-3|4|5|all}
optimizer.zero_grad()           # Nullstill gamle gradienter
scores = model(images)         # Beregn skårer
loss = loss_fn(scores, labels)  # Sammenlign med fasiten
loss.backward()                # Beregn gradienter
optimizer.step()               # Oppdater vekter og bias
```

**Batch:** én gruppe bilder per oppdatering.

**Epoke:** én gjennomgang av treningsutvalget.

I oppgavene: batchstørrelse **64**, **25** epoker.

<!--
Vis sammenhengen mellom teorien og de fem linjene. Nullstillingen fjerner gamle gradienter, ikke vektene. PyTorch akkumulerer ellers gradientene. Studentene bygger selv løkkene rundt dette i notatbok 04. Bruk ikke tid på å skrive hele løkken på tavlen.
-->

---

# Evaluering på testdata

```python
model.eval()
with torch.no_grad():
    scores = model(images)
    predictions = scores.argmax(dim=1)
    accuracy = (predictions == labels).float().mean().item()
```

Her er `images` og `labels` en **testbatch**. Hele testsettet må evalueres.

**`eval()`** velger evalueringsmodus. **`no_grad()`** slår av gradientregistrering.

Ingen parameteroppdateringer på testdata.

<!--
Dette viser evaluering på én batch, ikke hele testnøyaktigheten. Studentene samler antall riktige over alle testbatchene. Eval og no_grad har forskjellige roller. For våre enkle lag endrer ikke eval selve beregningen, men mønsteret er nyttig for andre lagtyper også.
-->

---
class: exercise
---

# Oppgaver 04 · Trening

`oppgaver/04_lineaer_klassifikator.ipynb`

Treningsløkke, tapskurve og testnøyaktighet for den lineære modellen.

<!--
Stopp forelesningen her og la studentene arbeide. Bruk eksemplene og hintene i notatboken ved behov.
-->

---

# Nettverk med ett skjult lag

<div class="flow"><div class="box">Piksler<br><strong>784</strong></div><span>→</span><div class="box">Skjult lag + ReLU<br><strong>128</strong></div><span>→</span><div class="box">Klasseskårer<br><strong>10</strong></div></div>

```python
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
)
```

Det skjulte laget lærer **mellomliggende representasjoner**.

<!--
Knytt dette til oversiktsbildet fra starten. Hvert skjult nevron beregner en vektet sum og bruker en aktivering. Vi gir ikke laget egen fasit; begge lagenes vekter læres fra klassifikasjonstapet. Utgangen er fortsatt ti rå skårer.
-->

---

# Aktiveringsfunksjoner: ReLU

$$
\operatorname{ReLU}(z)=\max(0,z)
$$

```python
values = torch.tensor([-2., -0.5, 0., 1., 3.])
torch.relu(values)  # tensor([0., 0., 0., 1., 3.])
```

ReLU lager et **knekkpunkt**: negative verdier blir null.

Flere lineære lag uten aktivering kan slås sammen til ett lineært lag.

<!--
ReLU endrer ikke formen og har ingen parametere som læres. Flere knekkpunkter kan kombineres til mer sammensatte funksjoner. La studentene gjøre den algebraiske begrunnelsen og utforske kurvefiguren i notatboken.
-->

---

# Trening og sammenligning av modeller

```python
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
```

Opprett optimizer med **parameterne til den nye modellen**.

Treningsstegene og tapsfunksjonen er de samme.

Sammenlign med den lineære modellen:

- Nøyaktighet på usette bilder
- Treningstid
- Hvilke klasser modellen forveksler

<!--
Notatbok 05 samler trening og evaluering i funksjoner, slik at de kan gjenbrukes. Hold hovedinnstillingene faste. La studentene regne parameterantallet selv. Ett forsøk er ikke nok til å si at én modelltype alltid er best.
-->

---

# Overtilpasning og generalisering

<LearningCurves />

**Trening:** lær parametere · **Validering:** velg modell · **Test:** sluttvurdering

<div class="small">Skjematiske kurver. Kurset bruker faste hovedinnstillinger og separate trenings- og testutvalg.</div>

<!--
Når treningstapet synker mens valideringstapet øker, kan det være overtilpasning. En treningskurve alene kan ikke avgjøre dette. Vi har ikke et eget valideringssett i hovedoppgavene. Før systematisk modellvalg bør vi sette av valideringsdata, i stedet for å velge etter testresultatene.
-->

---
class: exercise
---

# Oppgaver 05 · Nevrale nettverk

`oppgaver/05_nevralt_nettverk.ipynb`

Trening av nettverket, sammenligning med den lineære modellen og feilanalyse med forvekslingsmatrise.

8 skjulte nevroner og prosjektet i `06_bonus.ipynb` er valgfrie.

<!--
Stopp forelesningen her og la studentene arbeide. Bruk eksemplene og hintene i notatboken ved behov.
-->

---

# Oppsummering

| Del | PyTorch | Rolle |
|---|---|---|
| Data | `torch.Tensor`, `DataLoader` | Tall, former og batcher |
| Modell | `nn.Linear`, `nn.ReLU` | Inngang → skårer |
| Tap | `nn.CrossEntropyLoss` | Skårer og fasit → tap |
| Gradienter | `loss.backward()` | Deriver tapet med hensyn på parameterne |
| Oppdatering | `optimizer.step()` | Juster parameterne |
| Evaluering | `eval()`, `no_grad()` | Undersøk usette data |

<!--
Be studentene forklare beregningen fra ett bilde til en prediksjon, og hva som skjer i tillegg under trening. Neste steg er det valgfrie prosjektet: bruk den samme arbeidsflyten på nye data.
-->
