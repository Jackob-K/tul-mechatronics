# Proměnné odpory a řazení odporů

Proměnné odpory se používají k regulaci průtoku v hydraulických obvodech. Ideálním požadavkem je, aby regulační součást měla co nejmenší styk s kapalinou a aby průtok nebyl významně ovlivněn změnou viskozity. Z praktických důvodů se regulace průtoku realizuje pomocí škrticích prvků s ostrými hranami. Škrticí součást může mít nulový, kladný i záporný překryv.
## Hydraulické odpory

Hydraulické odpory způsobují tlakové ztráty při proudění tekutiny. Podle charakteru vzniku se rozlišují odpory rozložené a místní.

### Rozložené odpory

Rozložené odpory vznikají v přímých úsecích potrubí vlivem viskózního tření mezi tekutinou a stěnou potrubí.

Při laminárním proudění platí vztah
$$
\Delta p = R_i \, Q.
$$

Při turbulentním proudění platí nelineární závislost
$$
\Delta p = R_i \, Q^{1{,}75}.
$$

### Místní odpory

Místní odpory vznikají v tvarovkách a při změnách geometrie proudění. Jsou způsobeny změnou velikosti nebo směru vektoru rychlosti proudění, například při změně průřezu, zakřivení nebo větvení potrubí.

Tlaková ztráta je popsána vztahem
$$
\Delta p = D \, Q^2.
$$

## Výpočet odporu

Pro určení charakteru proudění se zavádí kritický průtok
$$
Q_{krit} = 0{,}109 \, d_i \, \nu,
$$
kde $d_i$ je vnitřní průměr trubky a $\nu$ kinematická viskozita.

### Laminární proudění

Tlaková ztráta při laminárním proudění v přímém potrubí je dána vztahem
$$
\Delta p_l = \frac{8{,}78 \, l \, \rho}{d_i^4} \, Q \cdot 10^{-3}.
$$

### Turbulentní proudění

Tlaková ztráta při turbulentním proudění je popsána empirickým vztahem
$$
\Delta p_t = \frac{59 \, l \, \rho \, \nu^{0{,}25}}{d_i^{4{,}75}} \, Q^{1{,}75} \cdot 10^{-3}.
$$

| Veličina |         Popis          |  Jednotka  |
| :------: | :--------------------: | :--------: |
|  $d_i$   | vnitřní průměr potrubí |    $mm$    |
|   $Q$    |    objemový průtok     | $dm^3/min$ |
|  $\nu$   | kinematická viskozita  |  $mm^2/s$  |
|  $\rho$  |        hustota         |  $kg/m^3$  |
|   $l$    |     délka potrubí      |    $m$     |

## Řazení odporů

Hydraulické odpory lze v obvodu zapojovat sériově nebo paralelně. Výsledné tlakové ztráty a průtoky závisí na charakteru proudění.

### Sériové řazení

Při sériovém zapojení protéká všemi odpory stejný průtok $Q$. Celkový tlakový spád je dán součtem dílčích tlakových ztrát.
![Schéma sériového zapojení odporů|300](Schema_seriove_odpory.png)
$$\Delta p_A=\Delta p_1+\Delta p_2+\dots+\Delta p_i$$
![](Graf_Seriove_odpory.png)
#### i) Laminární proudění

$$
\Delta p_i = R_i \, Q
$$
$$
\Delta p = \sum_{i=1}^{n} \Delta p_i = \sum_{i=1}^{n} R_i \, Q
$$

#### ii) Turbulentní proudění

$$
\Delta p_i = R_i \, Q^2
$$
$$
\Delta p = \sum_{i=1}^{n} R_i \, Q^2
$$

### Paralelní řazení

Při paralelním zapojení je na všech větvích stejný tlakový spád $\Delta p$, celkový průtok je dán součtem průtoků jednotlivými větvemi.
![Paralelní zapojení odporů|300](Schema_Paralelni_odpory.png)
$$
\begin{aligned}
Q &= Q_1 + Q_2 + \dots + Q_n \\
\Delta p &= p_2-p_1
\end{aligned}
$$
![](Graf_Paralelni_odpory.png)
#### i) Laminární proudění

$$
\Delta p = R_i \, Q_i
$$
$$
\frac{1}{R_{ekv}} = \sum_{i=1}^{n} \frac{1}{R_i}
$$

#### ii) Turbulentní proudění

$$
\Delta p = R_i \, Q_i^2
$$
$$
\frac{1}{\sqrt{R_{ekv}}} = \sum_{i=1}^{n} \frac{1}{\sqrt{R_i}}
$$

## Odpory shrnutí

- odpor $R$ se projevuje vždy, když $Q \neq 0$  
- dochází k přeměně tlakové energie na tepelnou energii, která se projeví tlakovým spádem a zvýšením teploty kapaliny  
- disipace tlakové energie se promítá do snížení hydraulické účinnosti $\eta_{hm}$  
- na odporech $R_s$ a kapacitách $G_s$ dochází ke ztrátě objemu, což ovlivňuje objemovou účinnost $\eta_v$  
- rozložené odpory $R_L$, $R_T$, místní i svodové odpory jsou pasivní prvky  
- vždy negativně ovlivňují přenášený výkon  
- proměnné odpory slouží k řízení přenášeného výkonu  
- k regulaci je nutný tlakový spád, jedná se o ztrátovou regulaci
