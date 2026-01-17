## Paprsková optika

### Postuláty paprskové optiky

1) Světlo se skrz optické prostředí šíří ve formě paprsků  
- Paprsky jsou emitovány světelnými zdroji  
- Paprsky lze pozorovat po dopadu na optický detektor (oko, CCD čip)

***

1) Optické prostředí je charakterizováno indexem lomu
$$
n = \frac{c_0}{c}
$$

| Symbol | Význam |
|------|--------|
| $n$ | index lomu prostředí |
| $c_0$ | rychlost světla ve vakuu |
| $c$ | rychlost světla v prostředí |

- Index lomu splňuje $n \geq 1$
- V obecném nehomogenním prostředí platí $n = n(\vec{r})$

***

3) Délka optické dráhy – $l$
- Optická dráha vyjadřuje **čas šíření světla**, nikoli skutečnou geometrickou délku trajektorie
- Je definována jako vzdálenost, kterou by světlo **urazilo ve vakuu za stejný čas**, jaký potřebuje k průchodu daným prostředím
- Slouží k porovnání šíření světla v různých prostředích z hlediska doby šíření

$$
l = \int_A^B n(\vec{r}) \cdot ds
$$

| Symbol | Význam |
|------|--------|
| $l$ | délka optické dráhy |
| $n(\vec{r})$ | prostorově závislý index lomu |
| $ds$ | element trajektorie |
| $A, B$ | krajní body dráhy |

- Index lomu $n$ vyjadřuje, **kolikrát je světlo v prostředí pomalejší než ve vakuu**
- V prostředí s větším indexem lomu se světlo šíří pomaleji, a proto má **větší optickou dráhu**
- Ve vakuu ($n = 1$) je optická dráha **nejkratší**, protože světlo se šíří nejrychleji

- V homogenním prostředí s konstantním indexem lomu platí
$$
l = n \cdot s
$$

| Symbol | Význam                  |
| ------ | ----------------------- |
| $s$    | geometrická délka dráhy |
| $n$    | index lomu prostředí    |

- Pro stejnou geometrickou dráhu $s$ platí:
  - větší $n$ → větší $l$ → delší doba šíření
  - menší $n$ → menší $l$ → kratší doba šíření
- Optická dráha je klíčová veličina ve Fermatově principu, kde světlo volí trajektorii s **extrémní (nejčastěji minimální) optickou dráhou**
***

4) **Fermatův princip**
- Paprsek se šíří mezi dvěma body po takové dráze, aby **optická dráha** měla extrémní hodnotu
- Ve většině fyzikálních situací se jedná o **minimum optické dráhy**
- Princip je ekvivalentní tvrzení, že **světlo se šíří po dráze s extrémní (nejčastěji minimální) dobou šíření**

$$
\delta \int_A^B n(\vec{r}) \cdot ds = 0
$$

| Symbol | Význam |
|------|--------|
| $\delta$ | variace dráhy |
| $n(\vec{r})$ | prostorově závislý index lomu |
| $ds$ | element trajektorie |
| $A, B$ | krajní body dráhy |

- Index lomu určuje rychlost šíření světla v prostředí
$$
n = \frac{c_0}{c}
$$

- V prostředí s větším indexem lomu se světlo šíří pomaleji
- Pokud světlo vstoupí do prostředí s vyšším indexem lomu, **nemůže si dovolit „zdržovat se“ dlouhou geometrickou dráhou**
- Proto volí takovou trajektorii, aby byla **optická dráha minimální**, i za cenu změny směru šíření

- Lom světla je přímým důsledkem Fermatova principu:
  - změna indexu lomu vede ke změně rychlosti šíření
  - světlo mění směr tak, aby minimalizovalo optickou dráhu (resp. dobu šíření)

- V homogenním prostředí s konstantním indexem lomu platí
$$
n = \text{konst.}
$$

- Potom Fermatův princip přechází v přímočaré šíření světla, protože nejkratší optická dráha odpovídá nejkratší geometrické dráze
### Odraz světla

- Úhel dopadu je roven úhlu odrazu
$$
\alpha = \alpha'
$$
- Dopadající paprsek, odražený paprsek a kolmice k rozhraní leží v jedné rovině

### Lom světla

- Lom světla nastává na rozhraní dvou optických prostředí s indexy lomu $n_1$ a $n_2$
- Lom je popsán Snellovým zákonem

#### Snellův zákon
$$
\frac{\sin \alpha_1}{\sin \alpha_2} = \frac{n_2}{n_1} = n_{21}
$$

| Symbol | Význam |
|------|--------|
| $\alpha_1$ | úhel dopadu |
| $\alpha_2$ | úhel lomu |
| $n_1$ | index lomu prvního prostředí |
| $n_2$ | index lomu druhého prostředí |
| $n_{21}$ | relativní index lomu |

#### Komplexní index lomu
- Používá se pro popis ztrátového optického prostředí
- Umožňuje současně popsat:
  - rychlost šíření světla v prostředí
  - zeslabení amplitudy vlivem absorpce

$$
\hat{n} = n + i \cdot \beta
$$

| Symbol | Význam |
|------|--------|
| $\hat{n}$ | komplexní index lomu |
| $n$ | reálná část indexu lomu |
| $\beta$ | koeficient absorpce (extinkční koeficient) |

- Reálná část $n$ určuje rychlost šíření světla v prostředí
$$
c = \frac{c_0}{n}
$$

- Imaginární část $\beta$ popisuje absorpci záření v prostředí
- Přítomnost $\beta \neq 0$ vede k exponenciálnímu poklesu amplitudy elektromagnetické vlny
- Pro neztrátové prostředí platí
$$
\beta = 0
$$

### Totální reflexe
- Nastává při přechodu světla z opticky hustšího prostředí do opticky řidšího
- Mezní úhel nastává v případě, kdy
$$
\alpha_2 = \frac{\pi}{2}
$$

- Platí vztah pro mezní úhel
$$
\sin \alpha_m = \frac{n_2}{n_1}
$$

| Symbol | Význam |
|------|--------|
| $\alpha_m$ | mezní úhel |
| $n_1$ | index lomu hustšího prostředí |
| $n_2$ | index lomu řidšího prostředí |

- Při překročení mezního úhlu dochází k totální reflexi
- Paprsek se zcela odrazí zpět do prvního prostředí