---
theme: default
title: PyTorch 101 — Fra tall til prediksjoner
info: En introduksjon til tensorer, bilder og lineære modeller.
class: cover
colorSchema: light
fonts:
  provider: none
  sans: Aptos, Inter, Helvetica Neue, Arial
  mono: DejaVu Sans Mono, monospace
htmlAttrs:
  lang: nb
canvasWidth: 1100
aspectRatio: 16/9
transition: fade
highlighter: shiki
drawings:
  persist: false
---

<div class="eyebrow">PyTorch 101</div>

# Fra tall til<br>prediksjoner

<div class="lead">Tensorer · Bilder · Modeller</div>

<img src="/fashion-sneaker.svg" class="cover-art" alt="En joggesko fra Fashion-MNIST" />

<!--
Vi skal etter hvert lage en modell som kjenner igjen klær, sko og vesker. Først trenger vi
å forstå hvordan PyTorch lagrer tall, og hvordan vi regner med dem.
Begynn med kjente begreper. Ikke introduser klassifikasjon, parametere eller
funksjonsnotasjon før vi har bygget grunnlaget med konkrete tall.
-->

---
class: section
---

<div class="eyebrow">01 / Tensorer</div>

# Tall, lister<br>og tabeller.

<div class="big-index">01</div>

<!--
Bruk god tid på første bolk. Det er her grunnlaget for resten av kurset legges.
Spør om gruppen har sett matriser tidligere, men la gjennomgangen stå på egne ben.
-->

---

<div class="eyebrow">01 / Skalar</div>

# Vi begynner med ett tall

<div class="number-stage">7</div>

<div class="lead">Et enkelt tall kalles en <strong>skalar</strong>.</div>

<!--
Eksempler er en temperatur, en pris eller antall riktige svar.
Skalar beskriver at vi har én enkelt tallverdi uten akser. Det sier ikke om tallet er heltall eller desimaltall.
I PyTorch kan også et enkelt tall lagres som en tensor: torch.tensor(7).
Hold syntaksen muntlig; poenget er først å etablere begrepet.
-->

---

<div class="eyebrow">01 / Vektor</div>

# Flere tall i en bestemt rekkefølge

<div class="matrix-row" style="margin-top: 65px">
<TensorMatrix :rows="[[7,2,9,4]]" />
</div>

<div class="lead">En slik rekke med tall kalles en <strong>vektor</strong>.</div>

<!--
Fire målinger kan samles i én vektor. Rekkefølgen er viktig:
7,2,9,4 og 4,9,2,7 inneholder de samme tallene, men er forskjellige vektorer.
Visningen er vannrett, men en endimensjonal PyTorch-tensor har bare én akse,
ikke en egen radakse. Vi skiller mellom formen [4] og en matrise med formen [1,4].
-->

---

<div class="eyebrow">01 / Matrise</div>

# Tall ordnet i rader og kolonner

<div class="columns" style="margin-top: 45px">
<div>
<TensorMatrix :rows="[[7,2,9],[4,8,1]]" :selected="['0,0','0,1','0,2']" label="Den første raden er markert." />
</div>
<div>

**2 rader** går vannrett.

**3 kolonner** går loddrett.

Tabellen kalles en **matrise**.

</div>
</div>

<!--
Pek ut én rad og én kolonne fysisk. La gruppen si hvor mange tall tabellen inneholder.
Et mulig eksempel er to varer med tre egenskaper hver: pris, vekt og antall.
Matrise er organiseringen av tallene; hva radene og kolonnene betyr bestemmes av dataene.
-->

---

<div class="eyebrow">01 / Tensor</div>

# Tensor er fellesnavnet

<div class="concept-strip" style="margin-top: 60px">
<div><b>Skalar</b><span>Ett tall</span></div>
<div><b>Vektor</b><span>Én rekke med tall</span></div>
<div><b>Matrise</b><span>Rader og kolonner</span></div>
</div>

<div class="rule lead" style="margin-top: 55px">En tensor kan også ha flere akser, som en stabel med bilder.</div>

<!--
I PyTorch brukes tensor om alle disse. Tensor betyr ikke nødvendigvis et stort eller komplisert objekt.
Når flere matriser stables, får vi en ekstra akse som velger matrise.
Vi bruker ordet slik det brukes i PyTorch, uten den mer generelle definisjonen fra fysikk og geometri.
-->

---

<div class="eyebrow">01 / Form</div>

# Formen forteller hvordan tallene er ordnet

| Tensor | Form | Akser | Antall tall |
|---|---|---|---|
| Skalar | `[]` | 0 | 1 |
| Vektor med fire tall | `[4]` | 1 | 4 |
| Matrise med to rader og tre kolonner | `[2, 3]` | 2 | 6 |

<div class="rule"><code>shape</code> gir formen. <code>ndim</code> teller aksene. <code>numel()</code> teller tallene.</div>

<!--
Forklar først formen til matrisen: antall rader, deretter antall kolonner.
En akse er en retning vi kan velge en posisjon langs. En vektor har én slik retning, en matrise to.
[] betyr at en skalar ikke har noen akser, ikke at den er tom.
Spør hva formen til en matrise med tre rader og fire kolonner blir. Svaret er [3,4], med 12 tall.
-->

---

<div class="eyebrow">01 / Posisjon</div>

# En rad og en kolonne velger ett tall

<div class="columns" style="margin-top: 40px">
<div>
<TensorMatrix :rows="[[7,2,9],[4,8,1]]" :selected="['1,2']" />
</div>
<div>

<div class="formula">matrix[1, 2] → 1</div>

Rad 1. Kolonne 2.

Vi teller fra **0**.

</div>
</div>

<!--
Følg først rad 1, deretter kolonne 2. Det markerer tallet 1.
Spør så hvordan de ville valgt tallet 2. Svaret er matrix[0,1].
Én indeks kan også velge en hel rad. Notatboka dekker detaljene om kolon og negative indekser.
-->

---

<div class="eyebrow">01 / Regning</div>

# Legg til samme tall på hver plass

<div class="matrix-row" style="margin-top: 55px">
<TensorMatrix :rows="[[7,2,9],[4,8,1]]" />
<span class="operator">+ 10 =</span>
<TensorMatrix :rows="[[17,12,19],[14,18,11]]" />
</div>

<div class="rule lead">Verdiene endres. Formen er fortsatt <code>[2, 3]</code>.</div>

<!--
Dette er et eksempel på elementvis regning. Vi gjør den samme operasjonen på alle plassene.
Med to matriser av samme form kan vi også legge sammen tallene som står på tilsvarende plass.
Vanlige operatorer som pluss, minus og elementvis gange følger denne tankegangen.
-->

---

<div class="eyebrow">01 / Gjennomsnitt</div>

# Ett svar per rad — eller per kolonne?

<div class="matrix-row">
<TensorMatrix :rows="[[2,6,4],[8,4,6]]" />
</div>

<div class="columns">
<div>

## Per rad

<div class="formula">[4, 6]</div>

To rader gir to gjennomsnitt.

</div>
<div>

## Per kolonne

<div class="formula">[5, 5, 5]</div>

Tre kolonner gir tre gjennomsnitt.

</div>
</div>

<!--
Regn første rad høyt: 2+6+4 er 12, delt på 3 gir 4.
Regn første kolonne: 2+8 er 10, delt på 2 gir 5.
Nå kan vi knytte begrepet akse til en konkret beregning: dim=1 regner innen hver rad;
dim=0 regner nedover hver kolonne. Den aksen vi regner over, fjernes normalt fra formen.
-->

---

<div class="eyebrow">01 / Broadcasting</div>

# Samme tillegg kan brukes på begge radene

<div class="matrix-row" style="margin-top: 50px">
<TensorMatrix :rows="[[7,2,9],[4,8,1]]" label="[2, 3]" />
<span class="operator">+</span>
<TensorMatrix :rows="[[10,20,30]]" label="Vektor: [3]" />
<span class="operator">=</span>
<TensorMatrix :rows="[[17,22,39],[14,28,31]]" label="[2, 3]" />
</div>

<div class="rule lead">Tillegget gjentas over radene. Dette kalles <strong>broadcasting</strong>.</div>

<!--
Første kolonne får 10, andre får 20 og tredje får 30. Det samme skjer på hver rad.
Generelt sammenlignes størrelsene fra høyre. De må være like, eller én må være 1.
En verdi per rad trenger formen [antall rader,1]. keepdim=True kan bevare denne eneraksen.
La den formelle regelen stå i notatboka; her skal de forstå hvorfor gjentakelsen gir mening.
-->

---

<div class="eyebrow">01 / Matrisemultiplikasjon</div>

# Vi skal gange disse to matrisene

<div class="matrix-row" style="margin-top: 60px">
<TensorMatrix :rows="[[2,1,3],[1,0,2]]" label="A: to rader, tre kolonner" />
<span class="operator">@</span>
<TensorMatrix :rows="[[1,2],[3,0],[2,1]]" label="B: tre rader, to kolonner" />
</div>

<div class="rule lead">Hvert tall i svaret kommer fra én rad og én kolonne.</div>

<!--
Introduser @ som PyTorch-operatoren for matrisemultiplikasjon.
Vi har valgt andre tall enn i notatbøkene. Ikke vis den generelle regelen først.
Pek på første rad i A og første kolonne i B. Neste lysbilde viser akkurat den beregningen.
-->

---

<div class="eyebrow">01 / Første tall</div>

# Gang parvis. Legg sammen.

<div class="matrix-row">
<TensorMatrix :rows="[[2,1,3],[1,0,2]]" :selected="['0,0','0,1','0,2']" label="Første rad" />
<span class="operator">@</span>
<TensorMatrix :rows="[[1,2],[3,0],[2,1]]" :selected="['0,0','1,0','2,0']" label="Første kolonne" />
<span class="operator">=</span>
<TensorMatrix :rows="[['?', '·'],['·','·']]" :selected="['0,0']" label="Første plass i svaret" />
</div>

<div class="arithmetic">2 · 1 + 1 · 3 + 3 · 2 <span v-click>= 11</span></div>

<!--
Pek på de tre parene i rekkefølge. Det er 2 ganger 1, 1 ganger 3 og 3 ganger 2.
La gruppen regne ut 2+3+6 før du viser 11. Dette kalles et prikkprodukt eller indreprodukt.
Poenget er selve operasjonen; vi trenger ikke introdusere summetegn eller vinkler.
Det ene tallet plasseres i rad 0, kolonne 0 i resultatet.
-->

---

<div class="eyebrow">01 / Resten av produktet</div>

# Samme regning for hver plass

<div class="matrix-row">
<TensorMatrix :rows="[[2,1,3],[1,0,2]]" />
<span class="operator">@</span>
<TensorMatrix :rows="[[1,2],[3,0],[2,1]]" />
<span class="operator">=</span>
<TensorMatrix :rows="[[11,7],[5,4]]" />
</div>

<div class="multiplication-steps">
<div><b>Øverst til høyre</b><span>2 · 2 + 1 · 0 + 3 · 1 = 7</span></div>
<div><b>Nederst til venstre</b><span>1 · 1 + 0 · 3 + 2 · 2 = 5</span></div>
<div><b>Nederst til høyre</b><span>1 · 2 + 0 · 0 + 2 · 1 = 4</span></div>
</div>

<!--
Gå gjennom én ny plass om gangen. Pek på raden og kolonnen som hører til.
La gjerne gruppen forklare siste tall selv. Dette er fremdeles samme operasjon,
ikke en ny regel for hver plass. Resultatet har én rad per rad i A og én kolonne per kolonne i B.
-->

---

<div class="eyebrow">01 / Hvorfor formene må passe</div>

# Raden og kolonnen må ha like mange tall

<div class="flow" style="margin-top: 65px">
<div><small>A</small><b>2 × <em>3</em></b></div>
<span>@</span>
<div><small>B</small><b><em>3</em> × 2</b></div>
<span>→</span>
<div><small>Resultat</small><b>2 × 2</b></div>
</div>

<div class="lead">Tre par skal ganges og summeres.</div>

<div class="rule">De indre størrelsene må være like. De ytre gir formen til svaret.</div>

<!--
Nå kommer formregelen etter at vi har sett hva beregningen gjør.
Hvis raden hadde tre tall og kolonnen to, ville vi manglet et par.
Spør hva en matrise med fire rader og tre kolonner gir ganget med B. Svaret er fire rader og to kolonner.
Det er ikke nødvendig å innføre bokstaver for alle dimensjonene her.
-->

---

<div class="eyebrow">01 / To typer gange</div>

# `*` og `@` gjør forskjellige ting

<div class="columns">
<div>

## Elementvis: `A * A`

<TensorMatrix :rows="[[4,1,9],[1,0,4]]" />

Hvert tall ganges med tallet på samme plass.

</div>
<div>

## Matriseprodukt: `A @ B`

<TensorMatrix :rows="[[11,7],[5,4]]" />

Hver rad og kolonne gir én sum.

</div>
</div>

<!--
A er fortsatt [[2,1,3],[1,0,2]], og B er matrisen fra forrige lysbilde.
Vi bruker A*A for at elementvis gange skal ha to like former.
Elementvis gange mellom A og B fungerer ikke her: [2,3] og [3,2] passer ikke med broadcasting.
Dette er to forskjellige operasjoner med forskjellige regler, selv om begge omtales som gange.
-->

---

<div class="eyebrow">01 / Transponering</div>

# Rader blir kolonner

<div class="matrix-row" style="margin-top: 50px">
<TensorMatrix :rows="[[2,1,3],[1,0,2]]" :selected="['0,0','0,1','0,2']" label="A: [2, 3]" />
<span class="operator">→</span>
<TensorMatrix :rows="[[2,1],[1,0],[3,2]]" :selected="['0,0','1,0','2,0']" label="A.T: [3, 2]" />
</div>

<div class="rule lead">Første rad blir første kolonne. Tallene beholder sammenhengen sin.</div>

<!--
Følg den markerte raden gjennom transponeringen.
Reshape gjør noe annet: den grupperer elementene i leserekkefølge til en ny form.
Studentene undersøker forskjellen selv i notatboka. Ikke regn ut den oppgaven her.
.T brukes her på en todimensjonal matrise, ikke som en generell operasjon på bildedata med flere akser.
-->

---
class: exercise
---

<div class="eyebrow">Selvstendig arbeid</div>

# Tensorer

<div class="task-path">oppgaver/01_tensorer.ipynb</div>

<!--
Pause til notatbok 01. Notatboka er selvstendig og dekker den konkrete PyTorch-syntaksen.
Be studentene knytte formene til rader og kolonner. Bruk gjerne rad-ganget-med-kolonne
som forklaring når noen står fast i et matriseprodukt.
-->

---
class: section
---

<div class="eyebrow">02 / Bilder</div>

# Et bilde er også<br>en tabell med tall.

<div class="big-index">02</div>

<!--
Vi bruker nå matrisebegrepet på noe de allerede kjenner: et gråtonebilde.
Ingen nye matematiske symboler er nødvendige for å forstå dette.
-->

---

<div class="eyebrow">02 / Piksler</div>

# Ett tall bestemmer lysstyrken til én piksel

<div class="columns" style="margin-top: 40px">
<div>
<TensorMatrix :rows="[[0,0,0],[0,128,255],[0,255,0]]" />
</div>
<div>
<div class="pixel-patch" role="img" aria-label="De samme ni verdiene vist som svarte, grå og hvite piksler">
<span v-for="(value, i) in [0,0,0,0,128,255,0,255,0]" :key="i" :style="{ background: `rgb(${value}, ${value}, ${value})` }"></span>
</div>
</div>
</div>

<div class="rule">0 er svart. 255 er hvitt. Verdiene imellom er gråtoner.</div>

<!--
La gruppen finne den grå pikselen i både matrisen og bildet.
Plasseringen i matrisen er plasseringen i bildet. Rad 0 ligger øverst.
Dette lille eksemplet er forskjellig fra pikseloppgaven i notatboka.
Vi bruker her vanlige 8-bit gråtoneverdier, ikke en universell skala for alle bildeformater.
-->

---

<div class="eyebrow">02 / Skala og kanaler</div>

# Samme bilde, en annen tallskala

<div class="columns" style="margin-top: 35px">
<div>

| Før | Delt på 255 |
|---|---|
| 0 | 0.0 |
| 128 | omtrent 0.5 |
| 255 | 1.0 |

</div>
<div>

**Gråtone:** én verdi per piksel.

**RGB:** tre verdier per piksel — rødt, grønt og blått.

</div>
</div>

<div class="rule">Et Fashion-MNIST-bilde i PyTorch: <code>[1, 28, 28]</code> — kanal, rader, kolonner.</div>

<!--
Vi går fra heltallsverdier til desimaltall mellom 0 og 1. Lysstyrken representerer det samme.
Datahjelperen gjør dette med ToTensor. Vi trenger ikke gå gjennom kode for konverteringen her.
Den første eneraksen er gråtonekanalen. Et vanlig RGB-bilde ville hatt tre kanaler.
Skalering med 255 er ikke det samme som å sentrere eller standardisere dataene.
-->

---

<div class="eyebrow">02 / Fra matrise til vektor</div>

# Les radene etter hverandre

<div class="matrix-row" style="margin-top: 45px">
<TensorMatrix :rows="[[1,2,3],[4,5,6]]" :selected="['0,0','0,1','0,2']" />
<span class="operator">→</span>
<TensorMatrix :rows="[[1,2,3,4,5,6]]" :selected="['0,0','0,1','0,2']" />
</div>

<div class="lead">For Fashion-MNIST: 28 · 28 = <strong>784 tall</strong> per bilde.</div>

<div class="rule">Alle verdiene er med. Rader og kolonner er samlet til én akse.</div>

<!--
Dette kalles å flate ut bildet. Illustrasjonen viser et lite eksempel med seks tall.
Tallene 1–6 er valgt for å gjøre rekkefølgen synlig, ikke som skalerte pikselverdier.
Vi kan bygge opp bildet igjen hvis vi kjenner formen og rekkefølgen.
Modellen får likevel ingen innebygd regel om å behandle nabopiksler sammen.
-->

---

<div class="eyebrow">02 / Plassering</div>

# Samme joggesko, andre pikselverdier

<SpatialShift />

<div class="rule lead">Modellen bør kjenne igjen skoen også når den flytter seg litt.</div>

<!--
Joggeskoen er forskjøvet to piksler mot høyre. For oss er betydningen den samme,
men mange verdier har byttet plass i pikselvektoren.
En enkel lineær modell har ikke denne robustheten innebygd.
Dette kan senere motivere dataaugmentering og konvolusjoner, men introduser ikke nye lag her.
-->

---

<div class="eyebrow">02 / Klassefordeling</div>

# 90 % riktige kan være en dårlig modell

<div class="columns" style="margin-top: 35px">
<div>

## Et tenkt datasett

<div class="distribution-bar"><span style="width:90%">90 % A</span><span style="width:10%">B</span></div>

Modellen gjetter alltid A.

</div>
<div>

<div class="formula" style="font-size: 46px">90 %</div>

samlet nøyaktighet

<div class="formula" style="font-size: 46px">0 %</div>

av B-eksemplene blir riktige

</div>
</div>

<!--
Dette er et hypotetisk eksempel, ikke Fashion-MNIST-fordelingen studentene skal måle.
En modell kan få høy samlet nøyaktighet bare ved å velge den vanligste klassen.
Derfor trenger vi en enkel referanse og bør også se på resultatene per klasse.
La gruppen forklare hva denne modellen faktisk har lært om bildene: ingenting.
-->

---

<div class="eyebrow">02 / Nye data</div>

# Vi vil kjenne igjen bilder vi ikke har sett før

<div class="columns" style="margin-top: 50px">
<div>

## Treningsdata

Bildene modellen lærer av.

</div>
<div>

## Testdata

Andre bilder som brukes til å vurdere resultatet.

</div>
</div>

<div class="rule lead">Å huske treningsbildene er ikke nok.</div>

<!--
Bruk analogien med å øve til en eksamen: å huske øvingssvar er ikke det samme som å forstå nye spørsmål.
Vi ønsker at modellen fungerer på nye, relevante bilder. Det kalles generalisering.
Testbildene skal ikke styre trening eller modellvalg. Ved systematisk modellvalg brukes et eget valideringssett.
Hold den siste presiseringen muntlig og kort; begynnere trenger først skillet mellom trening og test.
-->

---
class: exercise
---

<div class="eyebrow">Selvstendig arbeid</div>

# Bilder og datasett

<div class="task-path">oppgaver/02_bilder.ipynb</div>

<!--
Pause til notatbok 02. Studentene undersøker selv piksler, visning av bilder og klassefordeling.
-->

---
class: section
---

<div class="eyebrow">03 / Prediksjoner</div>

# Bruk tallene til<br>å velge en klasse.

<div class="big-index">03</div>

<!--
Vi har nå et bilde representert som en vektor. Neste steg bygger på den samme
rad-ganget-med-kolonne-beregningen som vi allerede har gjort.
-->

---

<div class="eyebrow">03 / Vektet sum</div>

# Noen verdier skal telle mer enn andre

<div class="matrix-row" style="margin-top: 40px">
<TensorMatrix :rows="[[2,1,3]]" label="Tre inngangsverdier" />
<span class="operator">@</span>
<TensorMatrix :rows="[[1],[3],[2]]" label="Tre vekter" />
<span class="operator">→ 11</span>
</div>

<div class="arithmetic">2 · 1 + 1 · 3 + 3 · 2 = 11</div>

<div class="rule">En vekt bestemmer hvor mye én inngangsverdi påvirker summen.</div>

<!--
Dette er første resultattall fra matriseproduktet tidligere i forelesningen.
Nå tolker vi tallene som innganger og vekter. Den andre inngangen teller tre ganger,
mens den første teller én gang. Negative vekter trekker ned når inngangene er positive.
Vektene er delt av alle eksemplene, men hver observasjon har egne inngangsverdier.
-->

---

<div class="eyebrow">03 / Konstantledd</div>

# Legg til et fast tillegg

<div class="arithmetic" style="margin-top: 65px">11 + (−2) = 9</div>

<div class="lead">Konstantleddet kalles <strong>bias</strong>.</div>

<div class="rule">Vektene bestemmer påvirkningen fra inngangene.<br>Bias gir et tillegg uavhengig av inngangene.</div>

<!--
Vi bygger opp modellen ett ledd om gangen. Den vektede summen var 11; med bias -2 blir skåren 9.
Tenk på bias som et utgangspunkt som ikke krever at noen piksel er lys.
En vektet sum pluss bias kalles vanligvis en lineær modell. Formelt er den affin,
men det begrepsskillet trenger ikke være en del av lysbildet.
-->

---

<div class="eyebrow">03 / Klassevalg</div>

# Én skår for hver mulig klasse

| Bilde | Klasse A | Klasse B | Klasse C | Valg |
|---|---|---|---|---|
| Første | **9** | 4 | −1 | A |
| Andre | 2 | **6** | 3 | B |

<div class="rule lead">Klassen med høyest skår blir modellens prediksjon.</div>

<!--
Hver klasse har sine egne vekter og sin egen bias. Derfor får samme bilde flere skårer.
For Fashion-MNIST trenger vi ti skårer, én per klasse. Her bruker vi tre klasser for å gjøre valget lett å lese.
PyTorch kaller operasjonen som finner posisjonen til høyeste verdi argmax.
Skår er et rått tall. Det kan være negativt og er ikke automatisk en sannsynlighet.
-->

---

<div class="eyebrow">03 / Flere bilder samtidig</div>

# Hver rad er ett bilde

<div class="flow" style="margin-top: 60px">
<div><small>Åtte bilder</small><b>[8, 784]</b></div>
<span>@</span>
<div><small>Vekter for ti klasser</small><b>[784, 10]</b></div>
<span>→</span>
<div><small>Ti skårer per bilde</small><b>[8, 10]</b></div>
</div>

<div class="rule lead">Samme vekter brukes på alle bildene.</div>

<!--
Nå skalerer vi opp akkurat samme matriseprodukt. Hver rad inneholder 784 piksler.
Hver kolonne i vektmatrisen inneholder vektene til én klasse.
Et konstantledd per klasse legges til etterpå, på samme måte som broadcasting-eksemplet.
En gruppe bilder kalles en batch. Den første størrelsen kan variere uten at modellen endres.
-->

---

<div class="eyebrow">03 / PyTorch</div>

# Et lineært lag samler vekter og bias

<div class="columns" style="margin-top: 40px">
<div>

```python
layer = nn.Linear(4, 3)
```

Fire inngangsverdier.<br>Tre skårer ut.

</div>
<div>

**Per utgang:** fire vekter og én bias.

**Til sammen:** 3 · 5 = 15 parametere.

</div>
</div>

<div class="rule">Trening justerer disse tallene. Når laget opprettes, er de ikke lært ennå.</div>

<!--
Dette er broen til biblioteket, med andre størrelser enn oppgaven studentene skal løse.
Et parameter er et tall modellen kan tilpasse under trening.
PyTorch lagrer vektene med én rad per utgang. Detaljen om transponering står i notatboka.
Ikke vis den ferdige Fashion-MNIST-modellen her; la studentene sette den sammen selv.
-->

---
class: exercise
---

<div class="eyebrow">Selvstendig arbeid</div>

# Prediksjoner

<div class="task-path">oppgaver/03_prediksjoner.ipynb</div>

<!--
Pause til notatbok 03. Studentene bygger fremoverberegningen selv.
Be dem koble kode og former til matriseproduktet vi har gjort med små tall.
-->

---

<div class="eyebrow">Neste steg</div>

# Hvordan finner vi gode vekter?

<div class="flow" style="margin-top: 60px">
<div><small>1</small><b>Lag en prediksjon</b></div>
<span>→</span>
<div><small>2</small><b>Mål hvor feil den er</b></div>
<span>→</span>
<div><small>3</small><b>Juster vektene</b></div>
</div>

<div class="rule lead">Gjenta på mange eksempler. Vurder deretter på nye data.</div>

<!--
Vi har foreløpig forklart beregningen fremover, ikke hvordan modellen lærer.
Neste bolk introduserer tap, gradienter og trening. Forklar rollen til disse med ord
før eventuell matematikk: et mål på feilen, en retning for endring og et lite oppdateringssteg.
-->

---

<div class="eyebrow">Referanser</div>

# Videre lesing

- [PyTorch: Tensorer](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)
- [PyTorch: Broadcasting](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)
- [PyTorch: Datasett og DataLoader](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html)
- [PyTorch: nn.Linear](https://docs.pytorch.org/docs/stable/generated/torch.nn.Linear.html)
- [3Blue1Brown: Matrisemultiplikasjon](https://www.3blue1brown.com/lessons/matrix-multiplication)

<!--
Oppslag etter forelesningen.
-->
