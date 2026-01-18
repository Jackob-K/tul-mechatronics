# Metody bez derivací

Metody bez derivací slouží k minimalizaci funkce jedné proměnné v situacích, kdy nejsou k dispozici derivace nebo je nechceme používat. Pracují výhradně s hodnotami funkce a jejich cílem je postupně zúžit interval, ve kterém se nachází minimum.

#### Základní úloha

- hledáme minimum funkce jedné proměnné
- obecný tvar úlohy
$$
\min f(x), \quad x \in \langle a,b \rangle \text{ nebo } x \in \mathbb{R}
$$
- výsledkem je hodnota $x^*$, pro kterou má funkce nejmenší hodnotu

#### Unimodalita funkce

- **unimodální funkce** má právě jedno minimum
- funkce:
  - nejprve klesá
  - poté roste
- unimodalita je **základní podmínkou** použití metod bez derivací
- minimum je bod, kde se chování funkce mění z klesajícího na rostoucí

#### Interval řešení

- **interval $\langle a,b \rangle$** určuje oblast, ve které minimum hledáme
- funkce musí být:
  - spojitá
  - ideálně unimodální v celém intervalu
- metody bez derivací:
  - interval postupně zmenšují
  - minimum zůstává vždy uvnitř aktuálního intervalu

#### Kritérium ukončení

- Kritérium ukončení je dáno požadovanou přesností
- vyjadřuje, jak „dost dobrý“ výsledek požadujeme

Používaná kritéria:

- **Délka intervalu**
$$
|a-b| < \epsilon
$$

- **Velikost derivace**  
  → používá se hlavně u metod s derivacemi
$$
|f'(x)| < \epsilon
$$

- **Změna mezi iteracemi**
$$
|x_{k+1}-x_k| < \epsilon
$$

#### Charakteristika metod bez derivací

- **nevyžadují derivace**
- pracují pouze s hodnotami $f(x)$
- porovnávají funkční hodnoty v různých bodech
- iterativně zužují interval s minimem
- jsou:
  - robustní
  - jednoduché na pochopení
- nevýhody:
  - pomalejší než derivační metody
  - použitelné především pro jednu proměnnou

#### Přehled základních metod

- [**Trisekce**](0411_Trisekce.md)
  → rozdělení intervalu na třetiny  
  → jednoduchá, ale pomalejší  

- Zlatý řez
  → efektivní rozdělení intervalu pomocí konstantního poměru  
  → méně výpočtů funkčních hodnot  

- Fibonacciho metoda
  → optimalizovaná varianta zlatého řezu  
  → vyšší přesnost  
  → složitější implementace 
