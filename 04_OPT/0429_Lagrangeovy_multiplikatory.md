# Lagrangeovy multiplikátory

Metoda Lagrangeových multiplikátorů slouží k hledání **extrémů funkce více proměnných s omezením**. Jedná se o **analytickou derivační metodu**, která umožňuje určit kandidáty minima nebo maxima na omezené množině.

## Základní úloha

- hledáme extrém funkce
$$
\min f(x)
$$
- za rovnostního omezení
$$
g(x) = 0
$$
- proměnná $x \in \mathbb{R}^n$

## Základní myšlenka

- pohybujeme se pouze po množině dané omezením
- v bodě extrému platí:
  - **gradient funkce je rovnoběžný s gradientem omezení**
- gradienty jsou tedy **lineárně závislé**

## Nutná podmínka extrému

- existuje skalár $\lambda$ tak, že
$$
\nabla f(x) = \lambda \nabla g(x)
$$
- $\lambda$ je **Lagrangeův multiplikátor**
- multiplikátor vyjadřuje citlivost extrému na změnu omezení

## Lagrangián

- zavede se pomocná funkce
$$
L(x,\lambda) = f(x) + \lambda g(x)
$$
- extrémy se hledají řešením soustavy rovnic
$$
\nabla L(x,\lambda) = 0
$$

## Postup výpočtu

1) zavedení Lagrangiánu  
2) výpočet parciálních derivací podle všech proměnných a multiplikátoru  
3) řešení soustavy rovnic  
4) získání **kandidátů extrému**

## Podmínky použití

- funkce $f(x)$ i omezení $g(x)$ jsou diferencovatelné
- gradient omezení není nulový
- metoda řeší **pouze rovnostní omezení**

## Vlastnosti metody

- **výhody**
  - elegantní
  - přesná
  - analytická

- **nevýhody**
  - složitější výpočty
  - neřeší nerovnostní omezení
  - poskytuje pouze kandidáty extrému

## Použití

- optimalizace více proměnných
- úlohy s rovnostním omezením
- známé analytické derivace

## Zařazení mezi metody

- metoda **s derivacemi**
- optimalizace **s omezením**
- analytická metoda

→ obecnější rámec optimalizace s omezeními je uveden v kapitole [Matematické programování](0430_Matematicke_programovani.md)
