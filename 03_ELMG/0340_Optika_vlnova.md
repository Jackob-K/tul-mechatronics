## Vlnová optika

- Paprsková optika je mezním případem vlnové optiky pro vlnovou délku $\lambda \to 0$
- Toto přiblížení je vhodné, pokud jsou rozměry objektů mnohem větší než vlnová délka světla
- Ve vlnové optice je světlo popsáno skalární vlnovou funkcí

### Postuláty vlnové optiky

1) Světlo se šíří ve formě vln  
	- Ve vakuu se šíří rychlostí $c_0$

1) Homogenní prostředí je charakterizováno indexem lomu $n$

2) Optická vlna je popsána vlnovou funkcí $u(\vec{r}, t)$  
	- Funkce vyhovuje vlnové rovnici
	- Platí princip superpozice

### Vlnová funkce – $u(\vec{r}, t)$
- Světlo je popsáno reálnou funkcí polohy a času
- Polohový vektor je definován jako $\vec{r} = (x, y, z)$
- Vlnová funkce splňuje vlnovou rovnici

$$
\nabla^2 u - \frac{1}{c^2} \frac{\partial^2 u}{\partial t^2} = 0
$$

| Symbol | Význam |
|------|--------|
| $u(\vec{r}, t)$ | vlnová funkce |
| $\nabla^2$ | Laplaceův operátor |
| $c$ | rychlost šíření světla |
| $t$ | čas |

- Každá funkce splňující tuto rovnici popisuje možnou optickou vlnu
- Vlnová rovnice je lineární, platí princip superpozice

### Komplexní vlnová funkce – $\hat{U}(\vec{r}, t)$
- Pro zjednodušení výpočtů se zavádí komplexní formalismus
- Reálná vlnová funkce je vyjádřena pomocí komplexní funkce

$$
\hat{U}(\vec{r}, t) = a(\vec{r}) \cdot e^{i\varphi(\vec{r})} \cdot e^{i2\pi \nu t}
$$

- Reálná vlnová funkce je dána reálnou částí komplexní funkce
$$
u(\vec{r}, t) = \frac{1}{2} \left[ \hat{U}(\vec{r}, t) + \hat{U}^*(\vec{r}, t) \right]
$$

| Symbol             | Význam                    |
| ------------------ | ------------------------- |
| $\hat{U}$          | komplexní vlnová funkce   |
| $\hat{U}^*$        | komplexně sdružená funkce |
| $a(\vec{r})$       | amplituda                 |
| $\varphi(\vec{r})$ | fáze                      |
| $\nu$              | frekvence                 |

### Optická intenzita – $I \; [W \cdot m^{-2}]$
- Fyzikální smysl vlnové funkce není přímo definován
- Měřitelnou veličinou je optická intenzita
- Vyjádřená jako [časové středování](0000_Stredovani_funkce.md) vlnové funkce

$$
I(\vec{r}, t) = 2 \cdot \langle u^2(\vec{r}, t) \rangle
$$

| Symbol | Význam |
|------|--------|
| $I$ | optická intenzita |
| $u(\vec{r}, t)$ | vlnová funkce |
| $\langle \cdot \rangle$ | časové středování |

- Optická intenzita je optický výkon na jednotku plochy

### Helmholtzova rovnice
- Komplexní vlnová funkce splňuje vlnovou rovnici
- Předpokládáme **časově harmonické (stacionární) řešení**, kdy časová závislost má harmonický tvar
- Oddělením časové a prostorové závislosti dostáváme Helmholtzovu rovnici

$$
\hat{U}(\vec{r}, t) = \hat{U}(\vec{r}) \cdot e^{i 2\pi \nu t}
$$

- Funkce $\hat{U}(\vec{r})$ je komplexní amplituda, která **nezávisí na čase**
- Časová závislost je plně obsažena v exponenciálním členu

Dosazením do vlnové rovnice získáme prostorovou rovnici

$$
(\nabla^2 + k^2) \cdot \hat{U}(\vec{r}) = 0
$$

| Symbol | Význam |
|------|--------|
| $\hat{U}(\vec{r})$ | komplexní amplituda |
| $k$ | vlnové číslo |
| $\nabla^2$ | Laplaceův operátor |

- Vlnové číslo je definováno vztahem
$$
k = \frac{2\pi \nu}{c} = \frac{\omega}{c} = \frac{2\pi}{\lambda}
$$

| Symbol | Význam |
|------|--------|
| $k$ | vlnové číslo |
| $\nu$ | frekvence |
| $\omega$ | kruhová frekvence |
| $c$ | rychlost šíření vlny |
| $\lambda$ | vlnová délka |

### Monochromatická vlna
- Monochromatická vlna má jedinou frekvenci
- Vlnová funkce má harmonickou časovou závislost

$$
u(\vec{r}, t) = a(\vec{r}) \cdot \cos \left[ 2\pi \nu t + \varphi(\vec{r}) \right]
$$

| Symbol | Význam |
|------|--------|
| $u(\vec{r}, t)$ | reálná vlnová funkce |
| $a(\vec{r})$ | amplituda vlnění |
| $\nu$ | frekvence |
| $\varphi(\vec{r})$ | fáze vlny |

### Rovinná vlna
- Nejjednodušší řešení Helmholtzovy rovnice v homogenním prostředí

$$
\hat{U}(\vec{r}) = A_0 \cdot e^{-i \vec{k} \cdot \vec{r}}
$$

| Symbol | Význam |
|------|--------|
| $A_0$ | komplexní obálka |
| $\vec{k}$ | vlnový vektor |
| $\vec{r}$ | polohový vektor |

- Platí vztah $|\vec{k}| = k$
- Vlnoplochy jsou roviny kolmé na vlnový vektor
- Směr $\vec{k}$ určuje směr šíření vlny
- Vzdálenost vlnoploch odpovídá vlnové délce

### Sférická vlna
- Další jednoduché řešení Helmholtzovy rovnice
- Vlna se šíří radiálně od bodového zdroje

$$
\hat{U}(\vec{r}) = \frac{A_0}{r} \cdot e^{-i k r}
$$

| Symbol | Význam |
|------|--------|
| $\hat{U}(\vec{r})$ | komplexní amplituda vlny |
| $A_0$ | komplexní obálka |
| $r$ | vzdálenost od zdroje |
| $k$ | vlnové číslo |

- Vlnoplochy jsou kulové plochy
- Vlnoplochy jsou od sebe vzdáleny o vlnovou délku $\lambda$
- Vlna se šíří fázovou rychlostí $c$
### Fresnelovo přiblížení
- Uvažujme sférickou vlnu vznikající v počátku souřadné soustavy
- Vlna je pozorována:
  - dostatečně daleko od zdroje
  - v bodech blízko osy $z$

- Platí aproximační podmínka
$$
\sqrt{x^2 + y^2} \ll z
$$

- Sférickou vlnu lze aproximovat parabolickou vlnou
$$
\hat{U}(\vec{r}) \approx
\frac{A_0}{z}
\cdot e^{-i k z}
\cdot e^{-i k \frac{x^2 + y^2}{2z}}
$$

| Symbol | Význam |
|------|--------|
| $x, y, z$ | kartézské souřadnice |
| $A_0$ | komplexní obálka |
| $k$ | vlnové číslo |
| $z$ | vzdálenost ve směru šíření |

### Interference
- Interference vzniká při skládání dvou nebo více vln
- Pro vznik interference musí být splněny následující podmínky:
  - zdroje vlnění jsou koherentní (stejná frekvence a fáze)
  - vlnění je monochromatické
  - platí princip superpozice
  - vlny mají stejnou polarizaci
- Za běžných podmínek (např. sluneční světlo) interference obvykle pozorovatelná není

### Interferenční rovnice
- Výsledná intenzita interferujících vln není prostým součtem jejich intenzit
- Mějme dvě monochromatické vlny s komplexními amplitudami $\hat{U}_1(\vec{r})$ a $\hat{U}_2(\vec{r})$
- Výsledná komplexní amplituda je dána superpozicí
$$
\hat{U}(\vec{r}) = \hat{U}_1(\vec{r}) + \hat{U}_2(\vec{r})
$$

- Výsledná intenzita je dána vztahem
$$
I = |\hat{U}(\vec{r})|^2
$$

- Po dosazení dostáváme interferenční rovnici
$$
I = I_1 + I_2 + 2 \cdot \sqrt{I_1 I_2} \cdot \cos \varphi
$$

| Symbol | Význam |
|------|--------|
| $I$ | výsledná intenzita |
| $I_1, I_2$ | intenzity jednotlivých vln |
| $\varphi$ | fázový rozdíl vln |

- Fázový rozdíl je definován vztahem $\varphi = \varphi_2 - \varphi_1$

- Pro $\varphi = 0$ nastává konstruktivní interference
- Pro $\varphi = \pi$ nastává destruktivní interference

### Interference dvou rovninných vln
- Mějme dvě rovinné vlny, obě s intenzitou $I_0$
- Obě vlny se šíří ve směru osy $z$
- Jedna vlna je vůči druhé posunuta o vzdálenost $d$

- Komplexní amplitudy obou vln lze zapsat ve tvaru
$$
\hat{U}_1 = \sqrt{I_0} \cdot e^{-i k z}
$$
$$
\hat{U}_2 = \sqrt{I_0} \cdot e^{-i k (z - d)}
$$

- Dosazením do interferenční rovnice dostáváme výslednou intenzitu
$$
I = 2 I_0 \left[ 1 + \cos \left( \frac{2\pi d}{\lambda} \right) \right]
$$

| Symbol | Význam |
|------|--------|
| $I$ | výsledná intenzita |
| $I_0$ | intenzita jednotlivé vlny |
| $d$ | rozdíl optických drah |
| $\lambda$ | vlnová délka |

- Výsledná intenzita je velmi citlivá na změny $d$ v řádu vlnové délky
- Tento jev se využívá v interferometrech