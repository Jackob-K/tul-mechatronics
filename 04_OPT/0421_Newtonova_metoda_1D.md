## Newtonova metoda (1D)

Newtonova metoda je **iterační derivační metoda** používaná pro hledání **kořene funkce** nebo **minima funkce jedné proměnné**. Patří mezi nejdůležitější metody optimalizace díky své **rychlé konvergenci** v okolí řešení.

#### Základní princip

- metoda vychází z **lokální lineární aproximace** funkce
- v každém kroku se:
  - aproximuje funkce tečnou
  - průsečík tečny s osou $x$ určí nový odhad řešení
- metoda vyžaduje **počáteční bod** $x_0$

#### Newtonova metoda pro hledání kořene

- hledáme bod, kde platí
$$
f(x) = 0
$$
- iterační vztah má tvar
$$
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}
$$

###### Vlastnosti
- velmi rychlá konvergence v okolí kořene
- citlivá na volbu počátečního bodu
- může divergovat nebo konvergovat k jinému kořeni

#### Newtonova metoda pro hledání minima

- minimum funkce nastává v bodě, kde
$$
f'(x^*) = 0
$$
- úloha se převede na hledání kořene derivace
- iterační vztah má tvar
$$
x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}
$$

#### Podmínky použití

- funkce je:
  - diferencovatelná
  - ideálně **alespoň dvakrát diferencovatelná**
- v bodě minima platí
$$
f''(x^*) > 0
$$
- derivace existují v okolí řešení

#### Počáteční bod

- volba počátečního bodu $x_0$ je **kritická**
- špatná volba může vést:
  - ke konvergenci k maximu
  - k inflexnímu bodu
  - k divergenci metody
- počáteční bod volíme:
  - v blízkosti očekávaného minima
  - v oblasti, kde existují derivace

#### Přesnost a ukončení

- výpočet se ukončí, pokud platí alespoň jedna z podmínek:
$$
|x_{k+1}-x_k| < \varepsilon
$$
$$
|f'(x_k)| < \varepsilon
$$
- případně po dosažení maximálního počtu iterací

#### Výhody a nevýhody

- **výhody**
  - velmi rychlá konvergence
  - vysoká přesnost
- **nevýhody**
  - nutnost znalosti derivací
  - citlivost na počáteční bod
  - může selhat daleko od řešení

#### Zařazení mezi metody

- metoda **s derivacemi**
- minimalizace **jedné proměnné**
- iterační metoda
