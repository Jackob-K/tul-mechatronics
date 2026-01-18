# Matematické programování

Matematické programování představuje obecný rámec optimalizace s omezeními, ve kterém hledáme minimum nebo maximum účelové funkce při splnění rovnostních a nerovnostních vazeb. Na rozdíl od klasických optimalizačních metod zde není kladen důraz na konkrétní iterační algoritmus, ale na **strukturu optimalizační úlohy** a vlastnosti řešení.

## Základní formulace úlohy

- obecná optimalizační úloha má tvar
$$
\min f(x)
$$
- za podmínek
$$
g(x)=0, \quad h(x)\le 0
$$
- proměnné jsou omezeny vazbami
- řešení leží v **přípustné oblasti**

## Lineární omezení

- lineární omezení mají tvar
$$
Ax \le b
$$
- vytvářejí oblast přípustných řešení
- geometrická interpretace:
  - v 2D mnohoúhelník
  - ve vyšších dimenzích polyedr
- optimalizace probíhá pouze uvnitř této oblasti

## Lineární účelová funkce

- lineární účelová funkce je:
  - přímka v rovině
  - rovina v prostoru
- minimum nebo maximum vzniká na **hranici přípustné oblasti**
- vnitřek oblasti není překážkou

## Lineární programování (LP)

- účelová funkce:
  - lineární
- omezení:
  - lineární
- proměnné:
  - spojité

Použití:
- ekonomika
- plánování výroby
- alokace zdrojů

Vlastnosti:
- úloha je **konvexní**
- platí:
  - lokální minimum = globální minimum

## Kvadratické programování (QP)

- účelová funkce:
  - kvadratická
$$
\min \frac{1}{2} x^T Q x + c^T x
$$
- omezení:
  - lineární

Použití:
- výskyt kvadratických členů v zadání
- aproximace nelineárních úloh

Vlastnosti:
- pokud je matice $Q$ pozitivně definitivní
  - úloha je konvexní
  - řešení je jednoznačné

## Nelineární programování (NLP)

- účelová funkce:
  - nelineární
- omezení:
  - lineární i nelineární

Použití:
- výskyt funkcí typu
  - $\sin$, $\cos$, $\exp$
  - vyšší mocniny

Vlastnosti:
- může existovat více lokálních minim
- bez konvexity:
  - není zaručeno globální řešení
- často se používají Lagrangeovy multiplikátory

## Charakteristika matematického programování

- optimalizace s omezeními
- důraz na:
  - strukturu účelové funkce
  - typ omezení
- volba metody závisí na:
  - linearitě
  - konvexitě
  - rozměru úlohy
