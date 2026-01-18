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

# Metody s více proměnnými

Metody s více proměnnými se zabývají minimalizací funkcí, jejichž argumentem je vektor proměnných. Navazují na metody jedné proměnné, ale pracují s geometricky složitějšími objekty, jako jsou gradienty a matice druhých derivací.

### Základní formulace úlohy

- obecná optimalizační úloha má tvar
$$
\min f(x), \quad x \in \mathbb{R}^n
$$
- proměnná $x$ je vektor
- úloha **nemá omezení vazbami**
- hledáme lokální nebo globální minimum funkce

### Minimum funkce více proměnných

- minimum je bod, kde má funkce nejmenší hodnotu v okolí
- nutná podmínka minima
$$
\nabla f(x^*) = 0
$$
- postačující podmínka (lokální minimum)
  - [Hessova matice](0002_Hessova_matice.md) je **pozitivně definitní**

### Základní skupiny metod

- **Gradientní metody**
  - využívají pouze [gradient](0003_Gradient.md)
  - jednoduché, ale pomalejší
  - viz Metoda největšího spádu

- **Newtonovy metody**
  - využívají gradient i Hessovu matici
  - velmi rychlé v okolí minima
  - viz Newton-Rhapsonova

- **Bezderivační metody**
  - nevyžadují derivace
  - pracují pouze s hodnotami funkce
  - vhodné pro malé dimenze
  - viz Nelder-Meadova

### Charakteristika metod

- metody jsou většinou **iterační**
- vyžadují **počáteční bod** $x_0$
- konvergence závisí na:
  - vlastnostech funkce
  - volbě počátečního bodu
  - použité metodě


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
