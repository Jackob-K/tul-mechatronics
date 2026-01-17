# Elektrické pole
- Elektrické pole je prostor obklopující elektricky nabité těleso
- V tomto prostoru se projevuje působení elektrické síly
- Elektrické pole definuje [Elektrická intenzita](0206_Elektricka_intenzita.md), v něm se nachází [elektrický náboj](0209_Elektricky_naboj.md) mezi kterými působí [Elektrická síla](0210_Elektricka_sila.md)
- V případě, že se jednotlivé náboje uspořádaně pohybují, vzniká [Elektrický proud](0213_Elektricky_proud.md)
- Následně platí, že pokud definujeme referenční bod, lze do elektrického pole vynést [Elektrický potenciál](0211_Elektricky_potencial.md), který přímo definuje elektrické napětí
- Jakmile výše uvedené pojmy známe, lze definovat [kapacitu](0212_Elektricka_kapacita.md), která vyjadřuje míru schopnosti materiálu pojmout elektrický náboj

## Elektrické pole v látkách

### Permitivita – $\varepsilon$
- Permitivita je fyzikální veličina popisující schopnost prostředí reagovat na elektrické pole
- Vyjadřuje míru polarizace prostředí vlivem elektrického pole
- Určuje vztah mezi elektrickou intenzitou a elektrickou indukcí v daném prostředí

$$
\vec{D} = \varepsilon \vec{E}
$$

- V obecném případě platí
$$
\varepsilon = \varepsilon_0 \varepsilon_r
$$

| Symbol | Význam |
|------|--------|
| $\varepsilon$ | permitivita prostředí |
| $\varepsilon_0$ | permitivita vakua |
| $\varepsilon_r$ | relativní permitivita prostředí |

- Permitivita vakua je konstantní
$$
\varepsilon_0 = 8{,}85 \cdot 10^{-12}\,\mathrm{F \cdot m^{-1}}
$$

- Relativní permitivita charakterizuje elektrické vlastnosti látky
- Pro vakuum platí $\varepsilon_r = 1$
- V lineárním izotropním prostředí je permitivita skalární konstanta
- V nehomogenním prostředí může permitivita záviset na poloze
$$
\varepsilon = \varepsilon(\vec{r})
$$

- Permitivita ovlivňuje:
  - velikost elektrické intenzity v prostředí
  - kapacitu kondenzátorů
  - šíření elektromagnetických vln v látkách

### Dielektrická prostředí
**a) Lineární prostředí**
- Vztah mezi vektorem elektrické polarizace a intenzitou elektrického pole je lineární
$$
\vec{P} = k \cdot \vec{E} = \varepsilon_0 \chi \vec{E}
$$

| Symbol | Význam |
|------|--------|
| $\vec{P}$ | vektor elektrické polarizace |
| $\vec{E}$ | intenzita elektrického pole |
| $k$ | konstanta úměrnosti |
| $\chi$ | elektrická susceptibilita |
| $\varepsilon_0$ | permitivita vakua |

***

**b) Nedisperzní prostředí**
- Permitivitа prostředí nezávisí na frekvenci $\nu$
- Polarizace v čase $t$ závisí pouze na intenzitě elektrického pole ve stejném čase $t$

***

**c) Izotropní prostředí**
- Vektor elektrické polarizace je rovnoběžný s vektorem intenzity elektrického pole
$$
\vec{P} \parallel \vec{E}
$$

- Prostředí má ve všech směrech stejné vlastnosti

***

**d) Homogenní prostředí**
- Permitivitа je konstantní v celém objemu
$$
\varepsilon = \text{konst.}
$$

***

**e) Nehomogenní prostředí**
- Permitivitа závisí na poloze v prostoru
$$
\varepsilon = \varepsilon(\vec{r})
$$

- Prostředí lze považovat za lokálně homogenní, pokud je permitivitа konstantní na oblasti o rozměru srovnatelném s vlnovou délkou $\lambda$

***

- Nejjednodušším příkladem dielektrického prostředí je vakuum
- Vakuum je lineární, nedisperzní, izotropní a homogenní