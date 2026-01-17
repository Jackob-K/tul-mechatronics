# Hydrogenerátory

Hydrogenerátor převádí mechanickou energii na energii hydraulickou. Základní vlastnosti hydrogenerátoru jsou popsány statickou, průtokovou a výkonovou charakteristikou, účinnostmi a možnostmi regulace. Hydrogenerátory se používají především v hydrostatických převodech a v hydraulických regulačních obvodech.

## Statická charakteristika

Statická charakteristika vyjadřuje závislost průtoku hydrogenerátoru $Q_g$ na tlakovém spádu při zatížení. Průtok hydrogenerátoru je obecně funkcí:
- tlaku $p_g$  
- otáček $n_g$  
- vlastností pracovní kapaliny (kinematická viskozita $\nu$, teplota $T$)

Obecný vztah má tvar
$$
Q_g = Q(p_g, n_g, \nu, T).
$$

Pro hydrogenerátor s konstantním geometrickým objemem platí
$$
Q_g = V_{0g} \cdot n_g - C_g \cdot p_g,
$$
zatímco pro hydrogenerátor s proměnným geometrickým objemem
$$
Q_g = V_{0g} \cdot \varphi_g \cdot n_g - C_g \cdot p_g.
$$

Ve vztazích vystupují:
- $V_{0g}$ – geometrický objem hydrogenerátoru  
- $C_g$ – koeficient vnitřních netěsností  
- $\varphi_g$ – regulační parametr hydrogenerátoru  

Statická charakteristika vyjadřuje úbytek dodávaného průtoku vlivem vnitřních netěsností, které se se vzrůstajícím tlakem zvětšují.

![|250](Schema_HG_vypocetni.png)

## Průtoková charakteristika

Průtoková charakteristika popisuje změnu průtoku hydrogenerátoru:
- v závislosti na tlakovém spádu  
- při konstantních otáčkách  
- při konstantním nastavení regulačního parametru  

Charakteristika má přibližně lineární průběh. Její sklon je ovlivněn:
- velikostí vnitřních netěsností  
- viskozitou pracovní kapaliny  

![|450](Graf_HG_prutokova_charka.png)

## Regulační parametr hydrogenerátoru

Regulační parametr $\varphi_g$ vyjadřuje relativní změnu geometrického objemu hydrogenerátoru.

Platí:
- pro jednosměrný hydrogenerátor
$$
\varphi_g \in \langle 0, 1 \rangle,
$$
- pro obousměrný hydrogenerátor
$$
\varphi_g \in \langle -1, 1 \rangle.
$$

Změnou regulačního parametru se mění dodávaný průtok při stejných otáčkách, čímž je umožněna plynulá regulace hydraulického výkonu.

## Typy hydrogenerátorů

Hydrogenerátory se konstrukčně provádějí zejména jako:
- zubové  
- lamelové  
- axiální pístové  
- radiální pístové  

Jednotlivé typy se liší:
- dosažitelným pracovním tlakem  
- účinností  
- rozsahem regulace  
- provozními otáčkami  

![|400](Tabulka_HG_typy_3.png)
![|400](Tabulka_HG_typy_6.png)
![|400](Tabulka_HG_typy_9.png)
![|400](Tabulka_HG_typy_12.png)

## Výkonová charakteristika hydrogenerátoru

Výkonová charakteristika udává průběh výkonu hydrogenerátoru:
- v závislosti na tlakovém zatížení  
- při daných otáčkách  

Při konstantních otáčkách a teplotě má ideálně lineární průběh. Výkon na hřídeli musí překonat:
- užitečný točivý moment daný tlakovým spádem  
- moment pasivních odporů $M_{p0}$  

Celkový moment na hřídeli hydrogenerátoru je
$$
M = M_t + M_{p0} = \frac{V_{0g}}{2\pi} \cdot p_g + M_{p0}.
$$

Výkon hydrogenerátoru je dán vztahem
$$
P = 2\pi \cdot n_g \cdot M.
$$

## Účinnosti hydrogenerátoru

Účinnosti hydrogenerátoru se stanovují experimentálně a vyjadřují vliv jednotlivých druhů ztrát.

Objemová účinnost vyjadřuje vliv vnitřních netěsností
$$
\eta_v = \frac{Q_0 - Q_z}{Q_0} = \frac{Q_g}{Q_0} = \frac{Q_g}{V_{0g} \cdot n_g}.
$$

Hydromechanická účinnost vyjadřuje vliv mechanických ztrát
$$
\eta_{hm} = \frac{M_t}{M_t + M_{p0}} = \frac{M_t}{M}.
$$

Po dosazení platí
$$
\eta_{hm} = \frac{V_{0g} \cdot p_g}{2\pi \cdot M}.
$$

Celková účinnost hydrogenerátoru je dána součinem objemové a hydromechanické účinnosti.

### Kvalitativní průběh účinnosti
![|450](Graf_HG_Kvalitativni_ucinnosti.png)

## Parametry hydrogenerátoru

Základními jmenovitými a mezními parametry hydrogenerátoru jsou:
- geometrický objem $V_0$  
- jmenovité otáčky $n_n$  
- minimální otáčky $n_{min}$  
- maximální otáčky $n_{max}$  
- jmenovitý tlak $p_n$  
- maximální tlak $p_{max}$  

Tyto parametry vymezují oblast bezpečného a hospodárného provozu hydrogenerátoru.

## Objemové řízení otáček a průtoku

Objemové řízení otáček nebo průtoku se realizuje kombinací hydrogenerátoru a hydromotoru:
- s konstantním geometrickým objemem  
- s proměnným geometrickým objemem  

Rozlišují se tyto typy zapojení obvodů:
- otevřený  
- uzavřený  
- polootevřený  

Změna otáček se dosahuje:
- změnou dodávaného průtoku  
- změnou geometrického objemu některého ze strojů  

![|500](Schema_HG_typy_obvodu.png)

### Hydrogenerátor a hydromotor s konstantním $V_0$
![|500](Schema_HG_HM_konstantni_V0.png)

### Hydrogenerátor s proměnným $V_0$ a hydromotorem s konstantním $V_0$
![|500](Schema_HG_promenny_V0_HM.png)
### Hydrogenerátor s konstantním $V_0$ a hydromotorem s proměnným $V_0$
![|500](Schéma_HG_HM_promenny_V0.png)
### Hydrostatický převod
![|500](Schema_Hydrostaticky_prevod.png)
## Řízení rychlosti a pohybové frekvence

Rychlost pohybu je dána:
- průtokem $Q_m$  
- velikostí činné plochy u přímočarého pohybu  
- geometrickým objemem u rotačního pohybu  

Platí vztahy
$$
v = \frac{Q_m}{S_m}, \quad \omega = \frac{2\pi}{V_{0m}} \cdot Q_m, \quad n = \frac{Q_m}{V_{0m}}.
$$

Změna průtoku se zajišťuje:
- škrcením  
- změnou geometrického objemu hydrogenerátoru  
- změnou geometrického objemu hydromotoru  
- kombinací uvedených způsobů  

Změna rychlosti může být:
- plynulá  
- stupňovitá  
- kombinovaná  
## Omezení regulačního rozsahu hydromotoru

Při objemové regulaci hydromotoru s proměnným geometrickým objemem dochází ke zvýšení otáček při snižování regulačního parametru $\varphi_m$. Pro velmi malé hodnoty $\varphi_m$ dochází k nárůstu otáček nad přípustnou mez.

Z tohoto důvodu se regulační parametr hydromotoru omezuje na interval
$$
\varphi_m \in \langle \varphi_{min}, 1 \rangle,
$$
aby nedošlo k překročení maximálních dovolených otáček $n_{max}$. Omezení regulačního rozsahu je nutné zejména při konstantním přiváděném průtoku.
![|500](Graf_HM_Omezeni_regulacniho_rozsahu.png)
## Momentová charakteristika hydromotoru

Skutečný výstupní moment hydromotoru je roven teoretickému momentu sníženému o moment pasivních odporů
$$
M = M_t - M_{p0} = \frac{V_{0m}}{2\pi} \cdot p_m - M_{p0}.
$$

Moment pasivních odporů je součtem jednotlivých složek
$$
M_{po} = M_c + M_s + M_b + M_p.
$$
![](Rovnice_HM_pasivni_odpory.png)
Jednotlivé složky představují:
- $M_c$ – konstantní složku danou konstrukcí, technologií výroby a zaběhnutím  
- $M_f$ – složku tření závislou na tlaku (tření v těsněních, rozvodech a opěrných deskách)
  – pro malé rychlosti nelineární
  – po překročení $M_{fs}$ (statický) se začne převodník otáčet
![](Graf_HM_Moment_po_rychlost.png)
- $M_b$ – složku způsobenou viskozitou kapaliny a třením v uložení vzájemně se pohybujících částí
- $M_\rho$ – složku danou hmotností kapaliny, která zvyšuje odpor prostředí kladený rotujícím částem  

Při malých otáčkách je průběh momentové charakteristiky nelineární. Po překonání statické složky tření $M_s$ se hydromotor začne otáčet, jeho moment nejprve klesá a s rostoucími otáčkami opět roste.

## Experimentální stanovení charakteristik

Momentové a ztrátové charakteristiky hydromotoru se stanovují experimentálně. Tyto charakteristiky:
- nelze přesně vypočítat analyticky  
- jsou nutné pro správný návrh hydrostatického převodu  
- umožňují posouzení provozních vlastností a účinnosti systému  

Získaná data slouží jako podklad pro volbu regulačního rozsahu a dimenzování hydraulického obvodu.
## Vztahy pro hydrogenerátor
![](Tabulka_Hydrogenerator_vztahy.png)
