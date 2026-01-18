## Nelder–Meadova metoda (simplex)

Nelder–Meadova metoda je **bezderivační metoda** pro minimalizaci **funkce více proměnných bez omezení**. Využívá geometrickou představu **simplexu** a pracuje pouze s hodnotami funkce, nikoli s jejími derivacemi.

#### Základní úloha

- minimalizace funkce tvaru
$$
\min f(x), \quad x \in \mathbb{R}^n
$$
- funkce nemá omezení vazbami
- derivace nejsou známy nebo je nechceme používat

#### Základní myšlenka

- metoda pracuje s **simplexem**:
  - v $n$-rozměrném prostoru má simplex $n+1$ vrcholů
- v každém kroku se:
  - vyhodnotí funkční hodnoty ve vrcholech
  - porovnají se hodnoty
  - nejhorší bod je nahrazen lepším
- simplex se postupně posouvá směrem k minimu

#### Počáteční simplex

- volí se $n+1$ bodů:
  - musí vyplnit okolí hledaného minima
- kvalita počátečního simplexu výrazně ovlivňuje chování metody

#### Hodnocení bodů

- ve vrcholech simplexu se spočítají hodnoty funkce
- body se seřadí podle velikosti funkčních hodnot:
$$
f(x_{\text{nejlepší}}) < f(x_{\text{prostřední}}) < f(x_{\text{nejhorší}})
$$

#### Základní operace se simplexem

###### Reflexe

- **základní krok metody**
- nejhorší bod se odrazí přes těžiště zbylých bodů
- pokud je nový bod lepší než prostřední, je přijat

###### Expanze

- pokud je reflexní bod lepší než nejlepší
- simplex se zkusí rozšířit dále stejným směrem
- typický koeficient:
$$
\alpha > 1 \quad (\text{často } \alpha = 2)
$$

###### Kontrakce

- pokud reflexe nepřinese zlepšení
- simplex se zmenší směrem k lepším bodům
- typický koeficient:
$$
\beta \in (0,1) \quad (\text{často } \beta = 0{,}5)
$$

###### Redukce

- použije se, pokud selžou předchozí kroky
- celý simplex se smrskne k nejlepšímu bodu
- používá se výjimečně

#### Podmínky použití

- funkce musí být **spočitatelná**
- derivace nejsou potřeba
- metoda je vhodná pro:
  - malé dimenze (typicky $n < 10$)

#### Přesnost a ukončení

- výpočet se ukončí, pokud platí
$$
\max f(x_i) - \min f(x_i) < \varepsilon
$$
- nebo po dosažení maximálního počtu iterací

#### Vlastnosti metody

- **výhody**
  - jednoduchá implementace
  - bez derivací
  - použitelná pro složité funkce

- **nevýhody**
  - pomalá
  - nespolehlivá ve vyšších dimenzích
  - nemá teoretické záruky konvergence

#### Zařazení mezi metody

- metoda **bez derivací**
- minimalizace **více proměnných**
- geometrická metoda (simplex)

→ alternativa k derivačním metodám, zejména [Metodě největšího spádu](0423_Nejvetsi_spad.md)
