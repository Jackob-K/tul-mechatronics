## Fibonacciho metoda

Fibonacciho metoda je **bezderivační intervalová metoda** pro minimalizaci **unimodální funkce jedné proměnné**. Představuje optimalizovanou variantu metody zlatého řezu, která využívá **Fibonacciho posloupnost** k přesně řízenému zmenšování intervalu.

#### Základní myšlenka

- minimum funkce leží v intervalu $\langle a,b \rangle$
- počet iterací je **předem dán**
- interval se zužuje pomocí poměrů vycházejících z Fibonacciho posloupnosti
- metoda minimalizuje počet výpočtů funkčních hodnot

#### Fibonacciho posloupnost

- posloupnost je definována vztahem
$$
F_0 = 0,\quad F_1 = 1,\quad F_k = F_{k-1} + F_{k-2}
$$
- poměry po sobě jdoucích členů se blíží zlatému poměru
- tyto poměry určují polohu testovacích bodů v intervalu

#### Volba bodů v intervalu

- pro zvolený počet kroků $N$ se v každé iteraci určují body pomocí poměrů
$$
u = a + \frac{F_{N-2}}{F_N}(b-a), \quad v = a + \frac{F_{N-1}}{F_N}(b-a)
$$
- porovnávají se hodnoty $f(u)$ a $f(v)$
- interval se zúží podobně jako u zlatého řezu

#### Rozhodovací pravidlo

- pokud $f(u) < f(v)$  
  → minimum leží v intervalu $\langle a,v \rangle$

- pokud $f(u) > f(v)$  
  → minimum leží v intervalu $\langle u,b \rangle$

- jeden bod se přenáší do další iterace

#### Přesnost a ukončení

- počet iterací $N$ se volí tak, aby výsledná délka intervalu splňovala
$$
|a-b| < \varepsilon
$$
- přesnost je tedy **řízena dopředu** volbou $N$
- výsledkem je interval obsahující bod minima

#### Podmínky použití

- funkce je:
  - spojitá
  - **unimodální** na intervalu $\langle a,b \rangle$
- derivace nejsou potřeba
- známe požadovanou přesnost $\varepsilon$

#### Vlastnosti metody

- **výhody**
  - velmi efektivní
  - minimální počet výpočtů $f(x)$
  - přesně řízená přesnost

- **nevýhody**
  - složitější implementace
  - nutnost znát požadovanou přesnost předem
  - méně flexibilní než zlatý řez

#### Zařazení mezi metody

- metoda **bez derivací**
- minimalizace **jedné proměnné**
- intervalová metoda
