## Newtonova–Rhapsonova metoda

Newtonova–Rhapsonova metoda je **iterační derivační metoda** pro minimalizaci **funkce více proměnných bez omezení**. Oproti gradientním metodám využívá kromě gradientu také **Hessovu matici**, což jí umožňuje velmi rychlou konvergenci v okolí minima.

#### Základní úloha

- minimalizace funkce tvaru
$$
\min f(x), \quad x \in \mathbb{R}^n
$$
- funkce nemá omezení vazbami
- gradient i Hessova matice jsou známy

#### Základní myšlenka

- funkce je v okolí aktuálního bodu **nahrazena kvadratickou aproximací**
- minimum této aproximace lze určit analyticky
- nový bod vznikne skokem přímo k minimu aproximující funkce

#### Iterační vztah

- obecný iterační krok má tvar
$$
x_{k+1} = x_k - H^{-1}(x_k)\nabla f(x_k)
$$
- $H(x_k)$ je Hessova matice funkce v bodě $x_k$
- metoda využívá informaci o zakřivení funkce

#### Podmínky použití

- funkce je:
  - diferencovatelná
  - alespoň dvakrát diferencovatelná v okolí řešení
- gradient existuje
- Hessova matice:
  - je invertibilní
  - je ideálně **pozitivně definitní**

#### Pozitivně definitní Hessova matice

- v bodě minima musí platit
$$
v^T H v > 0, \quad v \neq 0
$$
- funkce má v okolí bodu **miskovitý tvar**
- všechna vlastní čísla Hessovy matice jsou kladná
- v opačném případě může metoda směřovat:
  - k maximu
  - k sedlovému bodu

#### Počáteční bod

- volba počátečního bodu $x_0$ je **kritická**
- metoda:
  - je velmi rychlá blízko minima
  - může selhat daleko od minima
- špatný počátek může vést k divergenci

#### Přesnost a ukončení

- výpočet se ukončí při splnění některého z kritérií:
$$
|\nabla f(x_k)| < \varepsilon
$$
$$
|x_{k+1}-x_k| < \varepsilon
$$
- případně po dosažení maximálního počtu iterací

#### Vlastnosti metody

- **výhody**
  - velmi rychlá konvergence (kvadratická)
  - malý počet iterací

- **nevýhody**
  - drahý výpočet (Hessova matice, inverze)
  - citlivost na počáteční bod
  - může selhat mimo okolí minima

#### Zařazení mezi metody

- metoda **s derivacemi**
- minimalizace **více proměnných**
- Newtonova metoda

→ bezderivační alternativa je [Nelder–Meadova metoda](0414_Nelder_meadova_simplex.md)
