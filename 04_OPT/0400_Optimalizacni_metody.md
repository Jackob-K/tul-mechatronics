# Optimalizační metody

Optimalizační metody slouží k hledání minima nebo maxima účelové funkce
$$
\min f(x).
$$
Tato kapitola představuje **přehledovou mapu témat**, nikoli detailní výklad. Slouží k rychlé orientaci a připomenutí hlavních oblastí předmětu.

#### Základní rozdělení metod

- [**Metody bez derivací**](0410_Metody_bez_derivaci.md)
  → nevyžadují znalost derivací, pracují pouze s hodnotami funkce  
  → typicky minimalizace jedné proměnné  
  → unimodalita, interval ⟨a,b⟩ 

- [**Metody s derivacemi**](0420_Metody_s_derivacemi.md)
  → využívají první a často i druhou derivaci  
  → hledání kořenů a minim pomocí iteračních metod

#### Minimalizace podle počtu proměnných

- **Jedna proměnná**  
  → základní principy optimalizace  
  → interval, přesnost, unimodalita  
  → bezderivační a derivační metody

- **Více proměnných (bez omezení)**  
  → proměnná $x \in \mathbb{R}^n$  
  → gradient, Hessova matice  
  → gradientní metody, Newtonovy metody  
  → přehled v souboru [Metody s více proměnnými](0425_Metody_s_vice_promennymi.md)

#### Optimalizace s omezením

- **Rovnostní omezení**  
  → pohyb po omezené množině  
  → kolmost gradientů  
  → metoda [Lagrangeových multiplikátorů](0429_Lagrangeovy_multiplikatory.md)

#### Matematické programování

- **Lineární programování (LP)**  
  → lineární účelová funkce  
  → lineární omezení  

- **Kvadratické programování (QP)**
  → kvadratická účelová funkce  
  → pozitivně definitivní matice  

- **Nelineární programování (NLP)**  
  → nelineární funkce a omezení  
  → více lokálních extrémů  

→ shrnuto v souboru [Matematické programování](0430_Matematicke_programovani.md)

Tento soubor slouží jako **orientační uzel (mapa)**, ze kterého vedou odkazy na jednotlivá detailní témata.
