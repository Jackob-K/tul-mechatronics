## Elektromagnetická optika
- Pomocí vlnové optiky nelze vysvětlit jevy jako polarizace nebo dvojlom v anizotropním prostředí
- Světlo proto musí být popsáno jako elektromagnetické vlnění
- Na rozdíl od vlnové optiky není světlo popsáno skalární funkcí, ale vektorovým polem

### Postuláty elektromagnetické optiky

1) Světlo je elektromagnetické vlnění popsané Maxwellovými rovnicemi  
- Pro látkové prostředí bez volných nábojů platí

$$
\operatorname{rot}\,\vec{H} =
\frac{\partial \vec{D}}{\partial t}
$$

$$
\operatorname{rot}\,\vec{E} =
- \frac{\partial \vec{B}}{\partial t}
$$

$$
\operatorname{div}\,\vec{D} = 0
$$

$$
\operatorname{div}\,\vec{B} = 0
$$

$$
\vec{D} = \varepsilon_0 \varepsilon_r \vec{E}
$$

$$
\vec{B} = \mu_0 \mu_r \vec{H}
$$

- Pro vakuum lze vztahy zjednodušit
$$
\vec{D} = \varepsilon_0 \vec{E}
$$
$$
\vec{B} = \mu_0 \vec{H}
$$

2) Elektrické a magnetické pole splňují vlnovou rovnici  
- Každá složka vektorů $\vec{E}$ a $\vec{H}$ vyhovuje vlnové rovnici

$$
\nabla^2 \vec{E} -
\frac{1}{c^2}
\frac{\partial^2 \vec{E}}{\partial t^2}
= 0
$$

$$
\nabla^2 \vec{H} -
\frac{1}{c^2}
\frac{\partial^2 \vec{H}}{\partial t^2}
= 0
$$

- Rychlost šíření elektromagnetické vlny je dána vztahem
$$
c =
\frac{1}{\sqrt{\varepsilon_0 \varepsilon_r \mu_0 \mu_r}}
$$

- Pro vakuum platí
$$
c_0 =
\frac{1}{\sqrt{\varepsilon_0 \mu_0}}
$$

- Index lomu lze vyjádřit vztahem
$$
n = \sqrt{\varepsilon_r}
$$

3) Platí princip superpozice

### Maxwellovy rovnice
- Maxwellovy rovnice představují kompletní klasický popis elektromagnetického pole
- Jsou zde uvedeny v nejjednodušším tvaru pro vakuum
- Platí podmínky $\varepsilon_r = 1$ a $\mu_r = 1$

1) Rotace magnetického pole je vyvolána elektrickým proudem a časovou změnou elektrického pole
$$
rot \, \vec{B} = \mu_0 \left( \vec{j} + \varepsilon_0 \frac{\partial \vec{E}}{\partial t} \right)
$$

| Symbol          | Význam                      |
| --------------- | --------------------------- |
| $\vec{B}$       | magnetická indukce          |
| $\vec{j}$       | proudová hustota            |
| $\vec{E}$       | intenzita elektrického pole |
| $\mu_0$         | permeabilita vakua          |
| $\varepsilon_0$ | permitivita vakua           |
| $t$             | čas                         |

***

 2) Časová změna magnetické indukce vyvolává elektrické pole
$$
rot \, \vec{E} = - \frac{\partial \vec{B}}{\partial t}
$$

| Symbol | Význam |
|------|--------|
| $\vec{E}$ | intenzita elektrického pole |
| $\vec{B}$ | magnetická indukce |
| $t$ | čas |

***

 3) Zdrojem elektrického pole jsou prostorově rozložené elektrické náboje
$$
div \, \vec{E} = \frac{\rho}{\varepsilon_0}
$$

| Symbol | Význam |
|------|--------|
| $\vec{E}$ | intenzita elektrického pole |
| $\rho$ | hustota elektrického náboje |
| $\varepsilon_0$ | permitivita vakua |

***

 4) Neexistují magnetické monopóly a magnetické pole nemá zdrojové částice
$$
div \, \vec{B} = 0
$$

### Helmholtzova rovnice v elektromagnetické optice

- Protože jednotlivé složky vektorů elektrického a magnetického pole splňují vlnovou rovnici
- Každá z těchto složek musí vyhovovat také Helmholtzově rovnici

$$
(\nabla^2 + k^2) \cdot U = 0
$$

| Symbol | Význam |
|------|--------|
| $U$ | skalární funkce reprezentující jednu složku pole |
| $\nabla^2$ | Laplaceův operátor |
| $k$ | vlnové číslo |

- Skalární funkce $U$ reprezentuje vždy jednu ze šesti složek vektorů $\vec{E}$ a $\vec{H}$

- Pro vakuum je vlnové číslo dáno vztahem
$$
k = \omega \sqrt{\varepsilon_0 \mu_0}
$$

| Symbol | Význam |
|------|--------|
| $k$ | vlnové číslo |
| $\omega$ | kruhová frekvence |
| $\varepsilon_0$ | permitivita vakua |
| $\mu_0$ | permeabilita vakua |

### Monochromatická elektromagnetická vlna
- Pro monochromatickou elektromagnetickou vlnu jsou všechny složky elektrického i magnetického pole harmonickými funkcemi času

$$
\vec{E}(\vec{r}, t) = \operatorname{Re} \left\{ \hat{\vec{E}}(\vec{r}) \cdot e^{i \omega t} \right\}
$$

$$
\vec{H}(\vec{r}, t) = \operatorname{Re} \left\{ \hat{\vec{H}}(\vec{r}) \cdot e^{i \omega t} \right\}
$$

| Symbol | Význam |
|------|--------|
| $\vec{E}(\vec{r}, t)$ | elektrické pole |
| $\vec{H}(\vec{r}, t)$ | magnetické pole |
| $\hat{\vec{E}}(\vec{r})$ | komplexní amplituda elektrického pole |
| $\hat{\vec{H}}(\vec{r})$ | komplexní amplituda magnetického pole |
| $\omega$ | kruhová frekvence |

### Poyntingův vektor – $\vec{S} \; [W \cdot m^{-2}]$
- Poyntingův vektor udává plošnou hustotu toku výkonu
- Směr vektoru určuje směr šíření energie elektromagnetické vlny

$$
\vec{S}(\vec{r}, t) = \vec{E}(\vec{r}, t) \times \vec{H}(\vec{r}, t)
$$

| Symbol | Význam |
|------|--------|
| $\vec{S}$ | Poyntingův vektor |
| $\vec{E}$ | elektrické pole |
| $\vec{H}$ | magnetické pole |

### Optická intenzita – $I \; [W \cdot m^{-2}]$
- Optická intenzita je definována jako časová střední hodnota Poyntingova vektoru

$$
I = \langle \vec{S}_0 \rangle
$$

- Po vyjádření pomocí komplexních amplitud platí
$$
I =
\frac{1}{4}
\left(
\hat{\vec{E}} \times \hat{\vec{H}}^* +
\hat{\vec{E}}^* \times \hat{\vec{H}}
\right)
=
\frac{1}{2}
\left(
\vec{S}_0 + \vec{S}_0^*
\right)
=
\operatorname{Re} \left\{ \vec{S}_0 \right\}
$$

| Symbol      | Význam                      |
| ----------- | --------------------------- |
| $I$         | optická intenzita           |
| $\vec{S}_0$ | komplexní Poyntingův vektor |
| $^*$        | komplexně sdružená hodnota  |

### Interakce záření s hmotou

1) **Comptonův jev**
- Interakce fotonu s volným nebo slabě vázaným elektronem
- Dochází k dokonale nepružné srážce
- Část energie fotonu se předá elektronu ve formě hybnosti
- Výsledkem je změna vlnové délky záření
![|300](Compton-scattering.svg)

***

2) **Fotoelektrický jev**
- Emise původně vázaného elektronu z hmoty vlivem absorpce záření
- Elektron získá dostatečnou energii k opuštění atomu

***

3) **Vznik párů**
- Při průletu fotonu s dostatečnou energií v dosahu Coulombovského pole jádra
- Energie fotonu se využije na vznik páru elektron–pozitron
$$
h \nu \rightarrow e^- + e^+
$$
- Zbylá energie se změní na kinetickou energii jádra

***

4) **Excitace elektronu**
- Přechod vázaného elektronu na vyšší energetickou hladinu
- Elektron přechází ze základního stavu $E_1$ do excitovaného stavu $E_2$
- Změna je vyvolána absorpcí fotonu
- Energie fotonu se spotřebuje na přechod mezi energetickými hladinami
![](3.svg)

***

5) **Spontánní emise**
- Inverzní jev k excitaci
- Po určité době dochází k samovolnému návratu elektronu do základního stavu
- Energie je vyzářena ve formě fotonu
- Vlnová délka fotonu odpovídá energetickému rozdílu $\Delta E$
![](5.svg)

***

6) **Stimulovaná emise**
- Fyzikální proces, kdy foton vyvolá přechod elektronu z excitovaného stavu do základního
- Při přechodu dojde k emisi fotonu
- Energie emitovaného fotonu odpovídá rozdílu energií energetických hladin
![](8.svg)

### Laser
- Laser je optický oscilátor generující záření pomocí stimulované emise fotonů
- Za běžných podmínek se většina elektronů v atomech aktivního prostředí nachází v základním stavu
- Dodáním energie do aktivního prostředí (čerpáním, buzením) dochází k inverzi populace
- Inverze populace je stav, kdy je většina elektronů v excitovaném stavu
- V aktivním prostředí následně dochází ke stimulované emisi fotonů
- Emise může být vyvolána externím fotonem nebo fotonem vzniklým spontánní emisí

#### Princip činnosti laseru
- Zrcadla tvoří optický rezonátor
- Energie akumulovaná v aktivním prostředí je vyzářena ve formě laserového paprsku
![](Laser-oscillator-cavity.png)

#### Vlastnosti laserového paprsku

1) Paprsek je kolimovaný  
- Nerozbíhá se
- Energie je soustředěna na malou plochu

2) Paprsek je monochromatický  
- Fotony mají stejnou frekvenci
- Odpovídá jediné vlnové délce

3) Paprsek je koherentní  
- Všechny fotony jsou ve fázi

#### Laser jako optický oscilátor

- Laser lze popsat jako optický oscilátor se zpětnou vazbou
- Skládá se z:
  - rezonančního optického zesilovače
  - optického rezonátoru
![](Snímek%20obrazovky%202026-01-04%20v%2019.38.51.png)
- Výstupní signál zesilovače je zpětnou vazbou přiveden zpět na vstup
- Pokud na vstupu není žádný signál, není ani na výstupu
- Sebemenší šum iniciuje vznik oscilací

- Signál je opakovaně zesilován
- Růst amplitudy je omezen saturací zisku zesilovače
- Systém dosáhne ustáleného stavu

#### Podmínky vzniku oscilací

1) Zisk zesilovače musí být větší než ztráty zpětné vazby  
- Při jednom oběhu rezonátorem musí být dosažen čistý zisk

2) Celková změna fáze při jednom oběhu musí být celočíselným násobkem $2\pi$  
- Signál zpětné vazby je sfázovaný se vstupním signálem
