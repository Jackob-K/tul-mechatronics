## Metoda největšího spádu

Metoda největšího spádu je **iterační derivační metoda** pro minimalizaci **funkce více proměnných bez omezení**. Patří mezi základní gradientní metody a slouží jako výchozí nástroj pro pochopení chování optimalizačních algoritmů ve vícerozměrném prostoru.

#### Základní úloha

- minimalizace funkce tvaru
$$
\min f(x), \quad x \in \mathbb{R}^n
$$
- funkce nemá omezení vazbami
- gradient funkce je znám

#### Základní myšlenka

- **gradient** určuje směr největšího růstu funkce
- pro minimalizaci se postupuje **opačným směrem**
- v každém kroku se provede posun ve směru záporného gradientu

#### Iterační vztah

- obecný tvar kroku
$$
x_{k+1} = x_k - \alpha_k \nabla f(x_k)
$$
- $\alpha_k$ je **velikost kroku**
- volba kroku zásadně ovlivňuje chování metody

#### Volba velikosti kroku

- **konstantní krok**
  - jednoduchý
  - může vést k pomalé konvergenci nebo kmitání

- **proměnný krok**
  - volen např. minimalizací podél směru gradientu
  - stabilnější chování metody

#### Podmínky použití

- gradient existuje v celé oblasti řešení
- funkce je:
  - spojitá
  - diferencovatelná
- metoda konverguje zejména pro **konvexní funkce**

#### Vlastnosti metody

- **výhody**
  - jednoduchá
  - robustní
  - levná jedna iterace

- **nevýhody**
  - pomalá konvergence
  - klikatí se v úzkých údolích
  - silná závislost na volbě kroku

#### Přesnost a ukončení

- výpočet se ukončí, pokud platí
$$
|\nabla f(x_k)| < \varepsilon
$$
nebo
$$
|x_{k+1}-x_k| < \varepsilon
$$
- případně po dosažení maximálního počtu iterací

#### Zařazení mezi metody

- metoda **s derivacemi**
- minimalizace **více proměnných**
- gradientní metoda

→ rychlejší, ale náročnější alternativa je [Newtonova–Rhapsonova metoda](0427_Newton_rhapsonova.md)
