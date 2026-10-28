---
theme: default
title: PyTorch 101
info: 51 lysbilder med talemanus. Omtrent 90–105 minutter, fordelt over kurset.
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

<div class="lead">Tensorer, bildemodeller og trening</div>

<!--
I dette kurset skal vi bygge og trene små modeller i PyTorch. Dere har møtt maskinlæring før. Nå skal vi se nærmere på hva som faktisk beregnes, og hvordan vi skriver det i kode. Vi begynner med vektorer og matriser. Derfra går vi til bilder, klassifikasjon og nevrale nettverk. Underveis jobber dere med notatbøkene.
-->

---

# Innhold

| Del | Tema |
|---|---|
| 01 | Matriser og tensoroperasjoner |
| 02 | Bilder og datasett |
| 03 | Lineære modeller og prediksjoner |
| 04 | Tap, optimalisering og evaluering |
| 05 | Nevrale nettverk |

Oppgaver etter hver del

<!--
Dette er rekkefølgen vi følger. Først trenger vi et felles språk for tall, akser og former. Så undersøker vi dataene, før vi lager en modell som gir skårer. Deretter trener vi modellen og vurderer resultatene. Til slutt legger vi til et skjult lag. Hver del etterfølges av oppgaver. Det siste prosjektet er valgfritt.
-->

---

# Skalarer og vektorer

<div class="cols"><div>

**Skalar**

$$
a=3\in\mathbb{R}
$$

Ett tall.

</div><div>

**Vektor**

$$
x=\begin{bmatrix}2\\4\\6\end{bmatrix}\in\mathbb{R}^{3}
$$

Tre komponenter i en bestemt rekkefølge.

</div></div>

<!--
En skalar er ett tall. En vektor inneholder flere komponenter i en bestemt rekkefølge. Her er det tre. De kan for eksempel være tre målinger fra samme observasjon. I lineær algebra kan vi også tegne vektoren som en pil, men når vi jobber med bilder blir antall komponenter stort. Da er det ofte mer nyttig å tenke på vektoren som en ordnet samling målinger. Plassen til hver verdi må ha en fast betydning.
-->

---

# Matriser og dimensjoner

$$
X=\begin{bmatrix}2&4&6\\3&5&7\end{bmatrix}\in\mathbb{R}^{2\times3}
$$

| | Matematikk | PyTorch |
|---|---|---|
| Form | $2\times3$ | `[2, 3]` |
| Ett element | $X_{ij}$ | `x[i, j]` |
| Antall elementer | $2\cdot3=6$ | `x.numel()` |

Rad = eksempel. Kolonne = måling.

<!--
Her har vi to rader og tre kolonner. Vi skriver at X ligger i R opphøyd i to ganger tre: en matrise med reelle tall. I kode beskrives formen som to komma tre. Vi kan tolke hver rad som et eksempel og hver kolonne som en måling. Da har vi to eksempler med tre målinger hver. X med indeks i,j betyr verdien i rad i og kolonne j. Matrisen inneholder seks tall, men har to akser.
-->

---

# Prikkprodukt

$$
x=\begin{bmatrix}1\\2\\3\end{bmatrix},\qquad
w=\begin{bmatrix}2\\1\\0\end{bmatrix}
$$

$$
x^\mathsf{T}w=\sum_{j=1}^{3}x_jw_j=1\cdot2+2\cdot1+3\cdot0=4
$$

To vektorer med samme lengde → én skalar.

```python
torch.dot(torch.tensor([1., 2., 3.]), torch.tensor([2., 1., 0.]))
```

<!--
Prikkproduktet er byggesteinen i matrisemultiplikasjon. Vi ganger sammen komponentene på tilsvarende plasser og summerer produktene. Her får vi to pluss to pluss null, altså fire. Begge vektorene må ha samme lengde. Resultatet er ett tall, ikke en ny vektor med tre tall. Hvis vi tolker w som vekter, er dette en vektet sum av x. Den samme operasjonen dukker opp i hver utgang fra et lineært lag.
-->

---

# Matrise–vektor-produkt

$$
\underbrace{\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}}_{A:\;2\times3}
\underbrace{\begin{bmatrix}2\\1\\0\end{bmatrix}}_{w:\;3\times1}
=\underbrace{\begin{bmatrix}4\\13\end{bmatrix}}_{Aw:\;2\times1}
$$

Ett prikkprodukt per rad.

$$
\mathbb{R}^{3}\;\longrightarrow\;\mathbb{R}^{2}
$$

<!--
Vi kan nå bruke den samme vektoren på hver rad i en matrise. Første rad gir fire, akkurat som på forrige lysbilde. Andre rad gir fire ganger to pluss fem ganger én pluss seks ganger null, altså tretten. Resultatet har ett tall per rad. En matrise med to rader og tre kolonner beskriver dermed en lineær avbildning fra tre komponenter til to. Når høyresiden har flere kolonner, gjentar vi denne beregningen for hver kolonne.
-->

---

# Matrisemultiplikasjon

$$
\underbrace{\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}}_{[2,3]}
\underbrace{\begin{bmatrix}2&0\\1&1\\0&2\end{bmatrix}}_{[3,2]}
=\underbrace{\begin{bmatrix}4&8\\13&17\end{bmatrix}}_{[2,2]}
$$

Første tall: $1\cdot2+2\cdot1+3\cdot0=4$.

$$
[B,D]\; @\; [D,K]\;\longrightarrow\;[B,K]
$$

<div class="note">Vi summerer over <strong>D</strong>. De to indre størrelsene må være like.</div>

<!--
Når vi multipliserer to matriser, gjør vi ett prikkprodukt for hver plass i resultatet. Første rad møter først første kolonne, så andre kolonne. Vi får fire og åtte. Så gjør vi det samme med neste rad. Den første matrisen har tre kolonner og den andre tre rader. Det er disse størrelsene som må stemme, fordi vi multipliserer og summerer tre par av tall. Resultatet beholder antall rader fra venstre og antall kolonner fra høyre.
-->

---

# Elementvis produkt og matriseprodukt

```python
import torch

x = torch.tensor([[1., 2.], [3., 4.]])
weights = torch.tensor([[2., 0.], [1., 3.]])

x * weights   # tensor([[ 2.,  0.], [ 3., 12.]])
x @ weights   # tensor([[ 4.,  6.], [10., 12.]])
```

`*` multipliserer **element for element**.

`@` beregner **vektede summer**.

<!--
Disse operasjonene er forskjellige selv når formene er like. Stjernen multipliserer verdiene på samme plass. Krøllalfa beregner et matriseprodukt, med summer av produkter. Se på øverste høyre tall: med stjerne får vi to ganger null, altså null. Med matriseprodukt får vi én ganger null pluss to ganger tre, altså seks. Begge er gyldige beregninger, så vi må velge ut fra hva vi vil regne ut.
-->

---

# Tensorer

| Antall akser | Eksempel | Form |
|---|---|---|
| 0 | Skalar | `[]` |
| 1 | Vektor | `[3]` |
| 2 | Matrise | `[2, 3]` |
| 3 | Fargebilde | `[3, H, W]` |
| 4 | Gruppe med fargebilder | `[B, 3, H, W]` |

En tensor i PyTorch er en flerdimensjonal samling tall.

<!--
I PyTorch bruker vi ordet tensor for alle disse tilfellene. En skalar har null akser, en vektor én og en matrise to. Flere akser gir oss for eksempel kanaler, høyde og bredde, og en ekstra akse for flere bilder. En vektor i R i tredje har tre komponenter, men er en tensor med bare én akse. Ordet dimensjon kan derfor bety litt forskjellige ting. Her bruker vi antall akser og størrelsen langs hver akse for å være presise.
-->

---

# Hva PyTorch gir oss

| Del | Oppgave |
|---|---|
| `torch.Tensor` | Tall og tensoroperasjoner på CPU eller GPU |
| `torch.autograd` | Automatisk gradientberegning |
| `torch.nn` | Lag, modeller og tapsfunksjoner |
| `torch.optim` | Oppdatering av modellparametere |
| `torch.utils.data` | Datasett og batcher |

<!--
PyTorch gir oss flere deler som vi bruker sammen. Tensorene representerer både data og modellparametere. Autograd holder orden på beregninger slik at vi kan finne gradienter. nn gir oss ferdige lag og tapsfunksjoner, mens optim gir oss metoder for å oppdatere parametrene. Data-verktøyene hjelper oss å hente eksempler og sette dem sammen i batcher. Vi begynner med tensorene; resten kommer når vi har en modell å trene.
-->

---

# Opprette tensorer

```python
import torch

values = torch.tensor([[1., 2., 3.], [4., 5., 6.]])
zeros = torch.zeros(2, 3)
ones = torch.ones(2, 3)
random_values = torch.randn(2, 3)
sequence = torch.arange(6)
```

`tensor`: fra data · `zeros` / `ones`: fra form · `randn`: tilfeldige tall

<!--
Vi importerer torch og lager en tensor fra vanlige Python-lister. En liste inni en liste blir her en matrise. Vi kan også lage en tensor ved å angi formen og hvordan den skal fylles. zeros gir nuller, ones gir enere, og randn trekker normalfordelte tilfeldige tall. Tilfeldige tall bruker vi blant annet når vi oppretter modellvekter. arange gir en tallfølge. Legg merke til at en tensor med heltall som standard får en annen datatype enn en tensor med desimaltall.
-->

---

# Form, datatype og enhet

```python
values = torch.tensor([[1., 2., 3.], [4., 5., 6.]])
values.shape    # torch.Size([2, 3])
values.dtype    # torch.float32
values.device   # device(type='cpu')
```

| Egenskap | Betydning |
|---|---|
| `shape` | Størrelse langs hver akse |
| `dtype` | Hvordan tallene representeres |
| `device` | Hvor tensoren lagres og beregnes |

<!--
Disse tre egenskapene er nyttige å undersøke når noe feiler. Formen sier hvordan tallene er organisert. Datatypen sier hvordan de representeres: for eksempel desimaltall i float32 eller heltall i int64. Enheten forteller hvor tensoren ligger. Vi bruker CPU her. Ved bruk av GPU må både modellparametere og inndata flyttes til riktig enhet. Vi kan ikke uten videre blande tensorer på CPU og GPU i samme beregning.
-->

---

# Indeksering og akser

$$
X=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}
$$

| Uttrykk | Resultat | Form |
|---|---|---|
| `values[0, 1]` | `2.` | `[]` |
| `values[0]` | `[1., 2., 3.]` | `[3]` |
| `values[:, 1]` | `[2., 5.]` | `[2]` |
| `values[0:1]` | `[[1., 2., 3.]]` | `[1, 3]` |

Heltallsindeks fjerner en akse. Et utsnitt beholder den.

<!--
Indeksene starter på null. Et kolon betyr alle verdiene langs den aksen. Når vi velger rad null med en heltallsindeks, får vi en vektor med tre verdier. Hvis vi i stedet bruker utsnittet null til én, har vi fortsatt en radakse, men den har størrelse én. Tallene er de samme, mens formen er forskjellig. Det er en viktig forskjell når neste operasjon forventer en batchakse eller en bestemt matriseform.
-->

---

# Reduksjoner langs en akse

<div class="cols">
<div>

$$
\begin{bmatrix}2&4&6\\3&5&7\end{bmatrix}
$$

```python
measurements.mean(dim=1)
# tensor([4., 5.])

measurements.mean(dim=0)
# tensor([2.5, 4.5, 6.5])
```

</div>
<div>

**`dim=1`**: gjennomsnitt innen hver rad.

`[2, 3] → [2]`

**`dim=0`**: gjennomsnitt nedover hver kolonne.

`[2, 3] → [3]`

</div>
</div>

<div class="note"><code>dim</code> angir aksen vi reduserer. Med <code>keepdim=True</code> beholdes den med størrelse 1.</div>

<!--
En reduksjon samler flere tall til færre tall. Hvis vi tar gjennomsnitt over dim én, regner vi over kolonnene innen hver rad. Da får vi fire og fem, ett tall per rad. Med dim null regner vi over radene, og får ett tall per kolonne. Aksen vi reduserer forsvinner vanligvis. keepdim beholder den som en akse med størrelse én. Det endrer formen, men ikke selve gjennomsnittsverdiene.
-->

---

# Broadcasting

```python
row_means = measurements.mean(dim=1, keepdim=True)
# tensor([[4.], [5.]])     form [2, 1]

centered = measurements - row_means
# tensor([[-2., 0., 2.], [-2., 0., 2.]])
```

$$
[2,3]-[2,1]\;\longrightarrow\;[2,3]
$$

Sammenlign formene **fra høyre**. Størrelsene må være like, eller én må være 1.

<div class="note">Hvorfor feiler <code>[2, 3] - [2]</code>?</div>

<!--
Vi vil trekke hver rads gjennomsnitt fra alle verdiene i den raden. Gjennomsnittene har formen to ganger én. PyTorch kan bruke den ene verdien flere steder langs kolonneaksen. Dette kalles broadcasting. Reglene sjekkes fra høyre: størrelsene må være like, eller én må være én. Med formen to alene møter to kolonnestørrelsen tre, og operasjonen feiler. keepdim gir oss akkurat den formen vi trenger her.
-->

---

# Transponering og reshape

<div class="cols">
<div>

```python
weights = torch.tensor([
    [1., 2., 3.],
    [4., 5., 6.],
])
weights.T
# [[1., 4.],
#  [2., 5.],
#  [3., 6.]]
```

**`.T`** bytter rader og kolonner i en matrise.

</div>
<div>

```python
weights.reshape(3, 2)
# [[1., 2.],
#  [3., 4.],
#  [5., 6.]]
```

**`reshape`** gir tallene en ny form i leserekkefølge.

Lik form betyr ikke lik beregning.

</div>
</div>

<!--
Transponering bytter om rad- og kolonneaksen. Én, to og tre sto på samme rad; nå står de i samme kolonne. reshape beholder tallene i leserekkefølge og deler dem inn etter den nye formen. Begge resultatene har tre rader og to kolonner, men tallene står forskjellig. Derfor kan vi ikke reparere en transponeringsfeil bare ved å bruke reshape. Antall elementer må alltid være det samme når vi omformer.
-->

---

# Samle og dele opp tensorer

```python
first = torch.tensor([1., 2., 3.])
second = torch.tensor([4., 5., 6.])

torch.stack([first, second]).shape   # [2, 3]
torch.cat([first, second]).shape     # [6]
first.unsqueeze(0).shape            # [1, 3]
```

**`stack`**: ny akse · **`cat`**: eksisterende akse

**`unsqueeze`**: legg til akse · **`squeeze`**: fjern akse med størrelse 1

<!--
stack og cat kombinerer tensorer på forskjellige måter. stack lager en ny akse: to vektorer blir her en matrise med to rader. cat legger verdiene etter hverandre langs en eksisterende akse: vi får én vektor med seks tall. DataLoader samler bilder på en måte som tilsvarer stack. Under evaluering bruker vi cat til å samle prediksjoner fra flere batcher. unsqueeze legger til en akse med størrelse én. Bruk gjerne en eksplisitt akse med squeeze, så dere ikke fjerner batchaksen ved et uhell når batchen har bare ett bilde.
-->

---
class: exercise
---

# Oppgaver 01 · Tensorer

`oppgaver/01_tensorer.ipynb`

Tensorer · indeksering · reduksjoner · broadcasting · matriseprodukt

$$
[8,3]\;@\;[3,5]+[5]\;\longrightarrow\;?
$$

<!--
Åpne notatbok 01. Her skal dere bruke operasjonene vi nettopp har sett. Skriv gjerne den forventede formen før dere kjører. I uttrykket her blir resultatet åtte ganger fem, og bias med fem verdier brukes på hver rad. Hvis dere får en formfeil, skriv ut formene på begge sider av operasjonen og sammenlign aksene.
-->

---

<div class="kicker">02 · Bilder</div>

# Bilder som matriser

<div class="cols">
<div>
<PixelGrid />
</div>
<div>

Én piksel = én lysstyrke i et gråtonebilde.

**0 er svart. 1 er hvitt.**

`image[row, column]` velger én piksel i denne matrisen.

Et RGB-bilde har tre kanaler: rødt, grønt og blått.

</div>
</div>

<!--
Et gråtonebilde er et rutenett med lysstyrker. Her har vi bare seksten piksler. Null er svart, én er hvitt, og verdier mellom dem er gråtoner. Rad null ligger øverst. Hvis vi endrer verdien øverst til venstre fra null til én, blir den pikselen hvit. Et fargebilde trenger flere tall på hvert sted. I et vanlig RGB-bilde er det tre kanaler, én for rødt, én for grønt og én for blått.
-->

---

# Fashion-MNIST

<img src="/fashion-mnist.png" class="h-75 mx-auto" alt="Ett treningsbilde fra hver av de ti Fashion-MNIST-klassene" />

<div class="small">Kurset bruker faste utvalg: <strong>20 000 treningsbilder</strong> og <strong>1 000 testbilder</strong>. Hvert bilde er 28 × 28 piksler.</div>

<div class="small">Bilder: <a href="https://github.com/zalandoresearch/fashion-mnist">Zalando Research · Fashion-MNIST</a> · MIT</div>

<!--
Dette er faktiske bilder fra Fashion-MNIST. Hvert bilde har tjueåtte ganger tjueåtte piksler og tilhører én av ti klasser. Legg merke til at noen klasseskiller er vanskelige å se, særlig skjorte, genser og T-skjorte. Originaldatasettet har seksti tusen treningsbilder og ti tusen testbilder. Vi bruker faste utvalg på tjue tusen og tusen, slik at treningstiden blir håndterbar.
-->

---

# Kanaler og bildebatcher

<div class="flow">
<div class="box">Gråtonebilde<br><code>[1, H, W]</code></div>
<div class="box">RGB-bilde<br><code>[3, H, W]</code></div>
<div class="box">Batch<br><code>[B, C, H, W]</code></div>
</div>

$$
[64,1,28,28]\quad\Rightarrow\quad64\cdot1\cdot28\cdot28=50\,176\text{ tall}
$$

Etikettene ligger separat: `[64]`.

<!--
En bildebatch har fire akser i den konvensjonen vi bruker: antall bilder, kanaler, høyde og bredde. Én kanal er gråtoner, mens tre kan være RGB. En batch med 64 Fashion-MNIST-bilder inneholder litt over femti tusen pikselverdier. Etikettene har bare én akse, fordi hvert bilde har ett klassenummer. Andre biblioteker kan plassere kanalaksen sist. Derfor må vi kjenne betydningen av aksene, ikke bare antall tall.
-->

---

# Dataset og transformasjoner

<div class="flow">
<div class="box">Indeks <code>i</code></div><span>→</span>
<div class="box">Les eksempel</div><span>→</span>
<div class="box">Transformasjon</div><span>→</span>
<div class="box"><code>(image, label)</code></div>
</div>

| Operasjon | Betydning |
|---|---|
| `len(dataset)` | Antall eksempler |
| `dataset[i]` | Ett eksempel med tilhørende fasit |

Transformasjoner kan endre datatype, skala eller bildestørrelse.

<!--
Et vanlig indekserbart datasett har to hovedoppgaver: fortelle hvor mange eksempler det inneholder, og hente ett eksempel når vi gir en indeks. Det kan hente fra minnet eller lese en fil. Før eksemplet returneres, kan en transformasjon behandle det. I kurset bruker vi en enkel transformasjon til tensor og skala null til én. Datasettet bestemmer ikke batchstørrelsen eller treningsløkken. Det gjør at vi kan gjenbruke samme datasett med forskjellige lastere og modeller.
-->

---

# Datasett i PyTorch

```python
from pytorch_101.utils import CLASS_NAMES, download_fashion_mnist

train_data, test_data = download_fashion_mnist()
image, label = train_data[0]

image.shape          # torch.Size([1, 28, 28])
image.dtype          # torch.float32
CLASS_NAMES[label]   # Klassenavnet; label er et heltall fra 0 til 9
```

<div class="flow">
<div class="box">Råbilde<br><strong>0–255</strong></div>
<span>→</span>
<div class="box"><code>ToTensor()</code></div>
<span>→</span>
<div class="box">Én kanal, 28 × 28<br><strong>0–1</strong></div>
</div>

<!--
Et datasett lar oss hente ett bilde og den tilhørende etiketten med en indeks. image inneholder pikselverdiene; label er et klassenummer. Navnet henter vi fra CLASS_NAMES. Hjelpefunksjonen i kurset laster ned dataene og bruker ToTensor. For disse råbildene betyr det at heltall fra null til 255 blir float32 mellom null og én, og at vi får en kanalakse først. Formen blir én, tjueåtte, tjueåtte.
-->

---

# DataLoader

```python
from torch.utils.data import DataLoader

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
images, labels = next(iter(train_loader))

images.shape   # [64, 1, 28, 28]: bilder, kanaler, høyde, bredde
labels.shape   # [64]: én riktig klasse per bilde
```

**Dataset:** henter ett eksempel. **DataLoader:** samler flere eksempler.

`shuffle=True` stokker rekkefølgen for hver gjennomgang.



<!--
Dataset og DataLoader har forskjellige roller. Datasettet gir oss ett eksempel. Lasteren henter flere eksempler og samler dem i tensorer. Her får vi opptil 64 bilder og 64 etiketter. shuffle gjør at bildene kommer i ny rekkefølge for hver gjennomgang. Batchaksen er den første aksen. Hvis vi endrer batchstørrelsen, endrer vi antall bilder i gruppen, ikke oppløsningen på hvert bilde. Den siste gruppen kan være mindre. I notatbok 02 undersøker vi enkeltbilder; i 03 bruker vi lasteren til å sende batcher gjennom modellen.
-->

---
class: exercise
---

# Oppgaver 02 · Bilder

`oppgaver/02_bilder.ipynb`

Pikselverdier · visualisering · klassefordeling

<!--
I notatbok 02 skal dere undersøke bildene og klassefordelingen. Før vi trener, trenger vi en enkel referanse. Uniform tilfeldig gjetting har ti prosent forventet nøyaktighet når det er ti klasser. En annen referanse er alltid å gjette den vanligste klassen. Den avhenger av klassefordelingen. Resultatet på et endelig utvalg blir ikke nødvendigvis akkurat ti prosent.
-->

---

<div class="kicker">03 · Prediksjoner</div>

# Lineære modeller

For én inngang: $z=wx+b$.
Med flere innganger summerer vi bidragene:

$$
z=w_1x_1+w_2x_2+b
$$

$$
x=(2,3),\quad w=(0.5,-1),\quad b=0.2
$$

$$
z=0.5\cdot2-1\cdot3+0.2=\mathbf{-1.8}
$$

**Vekter** bestemmer bidragene. **Bias** flytter skåren med et konstantledd.

<!--
En lineær modell begynner med en vektet sum. Med én inngang kjenner dere uttrykket w ganger x pluss b. Med flere innganger har hver inngang sin egen vekt. Her bidrar den første med én og den andre med minus tre. Bias legger til null komma to, så svaret er minus én komma åtte. Hvis vi øker den første vekten med én, øker skåren med to, fordi den første inngangen er to. Under trening er det vektene og bias vi endrer.
-->

---

# Klassifikasjon

$$
f_\theta:\mathbb{R}^{784}\longrightarrow\mathbb{R}^{10}
$$

| Symbol | Betydning |
|---|---|
| $x$ | Pikselverdier for ett bilde |
| $\theta$ | Modellens parametere |
| $z=f_\theta(x)$ | Én skår per klasse |
| $\hat y=\arg\max_k z_k$ | Predikert klasse |

Fasiten $y$ er en klasseindeks fra 0 til 9.

<!--
Nå kan vi beskrive klassifikasjon mer generelt. Modellen er en funksjon fra et bilde til ti tall, ett for hver klasse. Theta er en samlebetegnelse for alle parameterne i modellen. Vi bruker en hatt over y for å skille prediksjonen fra den faktiske etiketten y. Modellen beregner først skårer. Deretter velger vi klassen med størst skår. Det er nyttig å holde disse stegene atskilt, fordi tapsfunksjonen trenger mer informasjon enn bare vinnerklassen.
-->

---

# Fra bilder til klasseskårer

<div class="flow">
<div class="box">Bilder<br><code>[B, 1, 28, 28]</code></div>
<span>→</span>
<div class="box">Flate bilder<br><code>[B, 784]</code></div>
<span>→</span>
<div class="box">Klasseskårer<br><code>[B, 10]</code></div>
</div>

```python
flat_images = images.flatten(start_dim=1)
weights = torch.randn(784, 10) * 0.01
bias = torch.zeros(10)
scores = flat_images @ weights + bias
```

$$
[B,784]\; @\; [784,10]+[10]\;\longrightarrow\;[B,10]
$$

<!--
Hvert bilde har 784 piksler. Vi flater ut kanal-, høyde- og breddeaksen, men beholder batchaksen. Nå har vi én rad per bilde. Vi multipliserer med en matrise som har én kolonne per klasse, og legger til ett konstantledd per klasse. Resultatet har B rader og ti kolonner. De samme vektene brukes på alle bildene. Å flate ut fjerner ingen piksler, men bildeformen er ikke lenger eksplisitt i tensorens akser.
-->

---

# Prediksjon og nøyaktighet

```python
scores = torch.tensor([[0.2, 2.1, -0.4], [3.0, 0.5, 1.2]])
labels = torch.tensor([1, 2])
predictions = scores.argmax(dim=1)       # tensor([1, 0])
correct = predictions == labels         # tensor([True, False])
accuracy = correct.float().mean().item() # 0.5
```

Nøyaktighet = antall riktige / antall eksempler.

<!--
I dette lille eksemplet har vi to bilder og tre klasser. Første rad har størst skår i kolonne én, og andre rad i kolonne null. argmax gir disse indeksene. Så sammenligner vi med fasiten: ett av to er riktig. Når vi gjør den boolske tensoren om til desimaltall, blir sann én og usann null. Gjennomsnittet er da andelen riktige. dim én betyr at vi velger blant klassekolonnene innen hvert bilde.
-->

---

# Logits og softmax

$$
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}}
$$

| Klasse | Logit $z_k$ | Softmax $p_k$ |
|---|---:|---:|
| 0 | 0 | 0.09 |
| 1 | 2 | 0.67 |
| 2 | 1 | 0.24 |

Logits er rå skårer. Softmax gir positive verdier som summerer til 1.

<!--
Skårene fra det siste lineære laget kalles logits. De kan være negative og trenger ikke summere til noe bestemt. Softmax omformer dem til verdier som summerer til én. Her er klasse én størst både før og etter omformingen. Vi trenger derfor ikke softmax for å velge klassen. Disse tallene kan tolkes som modellens sannsynligheter, men en høy verdi garanterer ikke at modellen har rett eller at sannsynligheten er godt kalibrert.
-->

---

# Moduler og parametere

**`nn.Module`** er grunnklassen for lag og modeller.

| Del | Rolle |
|---|---|
| Parametere | Tensorer som læres fra data |
| `forward` | Beregningen fra inngang til utgang |
| `model(x)` | Kjør modellen på `x` |
| `model.parameters()` | Hent parameterne til optimizer |

`nn.Sequential` er en modul som kjører andre moduler etter hverandre.

<!--
En modell i PyTorch er vanligvis en Module. Den samler beregningen og parameterne som hører til. forward beskriver hvordan utdata beregnes fra inndata. Når vi skriver model parentes x, kjører vi denne beregningen gjennom modulens vanlige kall. Linear er en Module, og Sequential er også en Module. Vi trenger ikke skrive en egen modellklasse i disse oppgavene, men en slik klasse lar oss definere mer sammensatte beregninger senere.
-->

---

# nn.Linear og nn.Sequential

```python
from torch import nn

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 10),
)
scores = model(images)

```

**7 850 parametere:** $784\cdot10+10$. Før trening er vektene tilfeldige.

<!--
Linear er et lag som eier vekter og bias, og beregner en vektet sum. Sequential setter sammen lag i rekkefølge. Her flater vi først ut bildet og beregner så ti skårer. PyTorch lagrer Linear-vektene med utganger først, altså ti ganger 784. Derfor er den eksplisitte beregningen X ganger den transponerte vektmatrisen. Det er 784 vekter og ett bias for hver klasse, totalt 7850 parametere. Ingen av dem er trent ennå.
-->

---
class: exercise
---

# Oppgaver 03 · Prediksjoner

`oppgaver/03_prediksjoner.ipynb`

Vektede summer · batcher · klasseskårer · `nn.Linear`

<!--
I notatbok 03 skal dere regne med vekter selv og deretter bygge en modell med PyTorch-lag. Følg formene gjennom beregningen. Hver rad i resultatet er ett bilde, og hver kolonne er en klasseskår. Modellen gir et svar allerede før trening, men svaret kommer fra tilfeldige startvekter.
-->

---

# Trening som et optimeringsproblem

$$
\theta^*=\arg\min_\theta\;\frac{1}{N}\sum_{i=1}^{N}
\ell\bigl(f_\theta(x_i),y_i\bigr)
$$

| Størrelse | Under trening |
|---|---|
| Bilder $x_i$ og fasit $y_i$ | Gitt av datasettet |
| Parametere $\theta$ | Justeres |
| Tap $\ell$ | Måler avviket fra fasiten |

I praksis tar vi mange små oppdateringssteg med batcher.

<!--
Målet med trening er å finne parametere som gir lavt gjennomsnittlig tap på treningsdataene. Dette uttrykket sier nettopp det. For hvert eksempel beregner vi modellens utgang, sammenligner med fasiten og tar gjennomsnittet av tapene. Bildene og etikettene er gitt. Parameterne er det vi kan endre. Vi løser ikke dette uttrykket direkte med én formel. I stedet starter vi med noen vekter og gjør mange små oppdateringer basert på batcher.
-->

---

<div class="kicker">04 · Trening</div>

# Forward og backward

<div class="flow">
<div class="box">Bilder</div><span>→</span>
<div class="box">Modell<br><strong>vekter og bias</strong></div><span>→</span>
<div class="box">Skårer</div><span>→</span>
<div class="box">Tap<br>mot fasiten</div>
</div>

**Forward pass:** regn fra bilder til skårer og tap.

**Backward pass:** beregn hvordan tapet påvirkes av hver parameter.

**Oppdatering:** bruk gradientene til å justere parametrene.



<!--
Vi kaller beregningen fra inngang til utgang en forward pass. Under trening bruker vi utgangen og fasiten til å beregne et tap. Deretter regner backward ut gradientene til tapet med hensyn på parametrene. Backpropagation er metoden som fører denne informasjonen bakover gjennom beregningen. PyTorch gjør derivasjonen for oss. Til slutt bruker optimizer gradientene til å endre parametrene. Backward og parameteroppdatering er altså to forskjellige operasjoner.
-->

---

# Tap og nøyaktighet

Fasit: klasse 1. To prediksjoner med samme vinnerklasse:

| | Sannsynligheter | Riktig? | $-\log(p_y)$ |
|---|---|---|---:|
| A | `[0.4, 0.6]` | Ja | 0.51 |
| B | `[0.1, 0.9]` | Ja | 0.11 |

Nøyaktigheten er lik. Tapet er lavere for B.

For ett eksempel: $\ell=-\log(p_y)$.

<!--
Begge disse prediksjonene velger riktig klasse. Nøyaktigheten er derfor den samme. Likevel støtter den andre prediksjonen riktig klasse sterkere. Kryssentropitapet er minus logaritmen til sannsynligheten modellen gir den riktige klassen. Med null komma seks blir tapet omtrent null komma fem én, og med null komma ni omtrent null komma én én. Dette gir et mer finmasket signal enn bare riktig eller feil. Hvis sannsynligheten for riktig klasse nærmer seg null, blir tapet stort.
-->

---

# Kryssentropi i PyTorch

```python
loss_fn = nn.CrossEntropyLoss()
loss = loss_fn(scores, labels)
```

| Inndata | Form og innhold |
|---|---|
| `scores` | `[B, 10]`, rå skårer som desimaltall |
| `labels` | `[B]`, riktige klasseindekser som `int64` |
| `loss` | Ett tall, gjennomsnitt over batchen |

<div class="note">Send rå skårer direkte til <code>CrossEntropyLoss</code>. Den håndterer normaliseringen selv.</div>

<!--
I PyTorch bruker vi CrossEntropyLoss direkte på rå skårer. Skårene har én rad per bilde og én kolonne per klasse. Fasiten har bare én klasseindeks per bilde, som int64. Resultatet er som standard gjennomsnittstapet over batchen. Vi skal ikke legge softmax på modellutgangen først: tapsfunksjonen håndterer den tilhørende normaliseringen på en numerisk stabil måte. Vi skal heller ikke sende argmax-resultatet inn som skårer.
-->

---

# Gradient og læringsrate

For én parameter $w$ gir $\frac{\partial L}{\partial w}$ den lokale endringsraten til tapet.

$$
w_{\mathrm{ny}}=w-\eta\frac{\partial L}{\partial w}
$$

Enkelt eksempel på gradient descent:

$$
w=1.0,\qquad\frac{\partial L}{\partial w}=2.0,\qquad\eta=0.1
\quad\Rightarrow\quad w_{\mathrm{ny}}=0.8
$$

$\eta$ er læringsraten. I oppgavene bruker vi **Adam**.

<!--
Gradienten forteller hvordan tapet endrer seg lokalt når en parameter endres. Hvis den deriverte er positiv, øker tapet lokalt når vi øker parameteren. Da kan vi prøve å redusere parameteren. Formelen her viser vanlig gradient descent: trekk fra læringsraten ganger gradienten. I eksemplet går vekten fra én til null komma åtte. Adam bruker en mer sammensatt oppdateringsregel med gradienthistorikk, men trenger de samme gradientene. Vi skal ikke utlede hvordan backpropagation beregner dem.
-->

---

# Én parameteroppdatering

```python {all|1|2-3|4|5|all}
optimizer.zero_grad()           # 1. Nullstill gamle gradienter
scores = model(images)         # 2. Beregn skårer (forward)
loss = loss_fn(scores, labels)  # 3. Sammenlign med fasiten
loss.backward()                # 4. Beregn gradienter (backward)
optimizer.step()               # 5. Oppdater vekter og bias
```

`backward()` beregner gradienter. `step()` endrer parametrene.



<!--
Her er de fem stegene i kode. Først fjerner vi gamle gradienter. Deretter beregner modellen skårer, og tapsfunksjonen sammenligner med fasiten. backward fyller inn gradientene til parametrene. Først når vi kaller step, endrer optimizer vektene og bias. PyTorch legger nye gradienter til de som allerede ligger der. I denne treningsløkken vil vi bruke bare den nye batchen, og derfor nullstiller vi først. Det er ikke vektene som nullstilles.
-->

---

# Batcher og epoker

```python
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
```

| Hyperparameter | Betydning |
|---|---|
| Batchstørrelse **64** | Opptil 64 bilder per oppdatering |
| **25** epoker | 25 gjennomganger av treningsutvalget |
| Læringsrate **0.001** | Styrer størrelsen på Adams oppdateringer |

20 000 bilder gir **313 oppdateringer per epoke**



<!--
En batch er en gruppe eksempler som vi bruker til ett oppdateringssteg. En epoke er én gjennomgang av hele treningsutvalget. Med tjue tusen bilder og grupper på 64 får vi 312 fulle grupper og én gruppe med 32 bilder. Det er 313 oppdateringer per epoke. Vi bruker 25 epoker. Læringsraten er en innstilling vi velger. Adam bruker også historikk fra gradientene til å tilpasse oppdateringene for de forskjellige parametrene.
-->

---

# Treningsløkken

```python
training_loss = []
for epoch in range(25):
    model.train()
    loss_sum = 0.0
    for images, labels in train_loader:
        optimizer.zero_grad()
        scores = model(images)
        loss = loss_fn(scores, labels)
        loss.backward()
        optimizer.step()
        loss_sum += loss.item() * len(images)
    training_loss.append(loss_sum / len(train_data))
```

<div class="small">Vi vekter batchtapet med antall bilder, slik at den siste, mindre batchen teller riktig.</div>

<!--
Den indre løkken er de fem stegene vi nettopp gikk gjennom. Den ytre løkken gjentar dette over flere epoker. train setter modellen i treningsmodus; det er ikke et kall som trener modellen alene. Vi samler tapet for å kunne plotte utviklingen. Hvert batchtap er et gjennomsnitt, så vi ganger med antall bilder før vi summerer. Til slutt deler vi på totalt antall treningsbilder. Da teller den siste, mindre batchen riktig.
-->

---

# Evaluering

```python
model.eval()
num_correct = 0
with torch.no_grad():
    for images, labels in test_loader:
        scores = model(images)
        predictions = scores.argmax(dim=1)
        num_correct += (predictions == labels).sum().item()
accuracy = num_correct / len(test_data)
```

**`eval()`** setter evalueringsmodus. **`no_grad()`** slår av gradientregistrering.

<!--
Ved evaluering kjører vi fremover gjennom modellen og teller riktige svar. Vi beregner ikke gradienter og gjør ingen parameteroppdatering. eval velger evalueringsmodus, mens no_grad slår av registrering for gradientberegning. De to gjør forskjellige ting. For akkurat våre lag endrer ikke eval selve beregningen, men andre lagtyper kan oppføre seg forskjellig under trening og test. Det er derfor vi bruker dette mønsteret konsekvent.
-->

---
class: exercise
---

# Oppgaver 04 · Trening

`oppgaver/04_lineaer_klassifikator.ipynb`

Tren den lineære modellen. Tegn tapskurven. Mål testnøyaktigheten.


<!--
Nå skal dere trene den lineære modellen i notatbok 04. Bruk de oppgitte innstillingene, tegn tapskurven og mål testnøyaktigheten. Ta vare på resultatene, for vi skal sammenligne med et nevralt nettverk senere. Før dere begynner: hvilken linje beregner gradientene, og hvilken endrer parametrene? Det er backward og step.
-->

---

<div class="kicker">05 · Nevralt nettverk</div>

# Nevrale nettverk

<div class="flow">
<div class="box">Piksler<br><strong>784</strong></div><span>→</span>
<div class="box">Linear + ReLU<br><strong>128</strong></div><span>→</span>
<div class="box">Linear<br><strong>10 skårer</strong></div>
</div>

$$
h=\operatorname{ReLU}(xW_1+b_1),\qquad z=hW_2+b_2
$$

Hvert skjult nevron beregner en vektet sum, så en aktivering.


<!--
Et nevralt nettverk setter sammen flere lag. I dette nettverket beregner vi først 128 mellomverdier fra pikslene. Så bruker vi disse mellomverdiene som innganger til laget som gir klasseskårene. Hvert skjult nevron er en vektet sum etterfulgt av en aktivering. Skjult betyr at vi ikke har en egen fasit for mellomverdiene. Begge lagenes vekter læres fra det samme klassifikasjonstapet på slutten.
-->

---

# Aktiveringsfunksjoner

$$
\operatorname{ReLU}(a)=\max(0,a)
$$

```python
values = torch.tensor([-2., -0.5, 0., 1., 3.])
torch.relu(values)  # tensor([0., 0., 0., 1., 3.])
```

Uten aktivering kan to lineære lag slås sammen:

$$
(xW_1+b_1)W_2+b_2=x(W_1W_2)+(b_1W_2+b_2)
$$

<div class="note">Ulineære aktiveringsfunksjoner gjør det mulig å lære mer enn én samlet lineær transformasjon.</div>

<!--
ReLU beholder positive verdier og setter negative verdier til null. Den endrer ikke formen på tensoren. Hvorfor legger vi den mellom lagene? Hvis vi bare bruker to lineære lag, kan vi gange sammen vektmatrisene og samle konstantleddene. Da er hele modellen fortsatt én affin transformasjon. ReLU gjør at dette ikke lenger er mulig. Det gir nettverket mulighet til å beskrive andre sammenhenger. ReLU har ingen parametere som skal læres.
-->

---

# Nettverket i PyTorch

```python
model = nn.Sequential(
    nn.Flatten(),         # [B, 1, 28, 28] → [B, 784]
    nn.Linear(784, 128),  # [B, 784] → [B, 128]
    nn.ReLU(),           # [B, 128] → [B, 128]
    nn.Linear(128, 10),   # [B, 128] → [B, 10]
)
```

**101 770 parametere:** $(784\cdot128+128)+(128\cdot10+10)$


<!--
I kode legger vi til et Linear-lag og en ReLU før det siste laget. Følg formene: først 784 verdier, så 128, fortsatt 128 etter ReLU, og til slutt ti klasseskårer. Det er litt over hundre tusen parametere, mot 7850 i den lineære modellen. Treningsløkken kan være den samme. Vi må bare opprette optimizer med parametrene til den nye modellen. Flere parametere gir større kapasitet, men garanterer ikke bedre testresultat.
-->

---

# Trening, validering og test

| Data | Brukes til |
|---|---|
| Trening | Lære vekter og bias |
| Validering | Velge innstillinger og modell |
| Test | Sluttevaluering |

I kurset: faste hovedinnstillinger og separate trenings- og testutvalg.

<!--
Treningsdata brukes til å lære parameterne. Valideringsdata brukes når vi velger for eksempel læringsrate eller antall epoker. Testdata bør brukes til den endelige evalueringen. Hvis vi prøver mange innstillinger og beholder den som gir best testresultat, har testsettet påvirket modellvalget. I notatbøkene holder vi hovedinnstillingene faste og har ikke et eget valideringssett. Hvis vi vil utvikle modellen videre, bør vi først sette av valideringsdata.
-->

---

# Overfitting

<LearningCurves />

Treningstap alene er ikke nok til å si hvor god modellen er på usett data.

<!--
Her fortsetter treningstapet å synke, mens tapet på valideringsdata etter hvert øker. Det er et typisk tegn på overtilpasning: modellen tilpasser seg treningsutvalget uten å bli bedre på nye eksempler. Kurvene er skjematiske, ikke resultater fra notatbøkene. For å undersøke dette trenger vi målinger på data som ikke brukes til parameteroppdatering. En synkende treningskurve alene kan verken bekrefte god generalisering eller avsløre overtilpasning.
-->


class: exercise
---

# Oppgaver 05 · Nevrale nettverk

`oppgaver/05_nevralt_nettverk.ipynb`

Trening · sammenligning · feilbilder · forvekslingsmatrise

<!--
I notatbok 05 skal dere samle trenings- og evalueringskoden i funksjoner og trene nettverket med 128 skjulte nevroner. Sammenlign med den lineære modellen, både i nøyaktighet og tidsbruk. Se på feilbilder og lag en forvekslingsmatrise. Bruk deres egne målinger i oppsummeringen. Sammenligningen med åtte nevroner og prosjektet i 06 er valgfrie hvis dere har tid.
-->

---

# Oppsummering

| Begrep | Rolle |
|---|---|
| Tensor | Data og parametere |
| Modell | Inngang → skårer |
| Tapsfunksjon | Skårer og fasit → tap |
| `backward()` | Tap → gradienter |
| Optimizer | Gradienter → parameteroppdatering |
| Evaluering | Måle ytelse på egne datautvalg |

<!--
La oss knytte dette sammen. Bildet blir en tensor, modellen beregner skårer, og argmax velger en klasse. Under trening måler vi et tap, beregner gradienter med backward og oppdaterer parametrene med step. Deretter undersøker vi ytelsen på andre bilder enn dem vi trente på. Hvis dere kan forklare disse overgangene og formene underveis, har dere grunnlaget for å bygge og undersøke flere typer modeller.
-->
