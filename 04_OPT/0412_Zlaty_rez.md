## Zlatý řez

Metoda zlatého řezu je **bezderivační intervalová metoda** pro minimalizaci **unimodální funkce jedné proměnné**. Oproti trisekci je efektivnější, protože **znovu využívá již vypočtené funkční hodnoty** a snižuje počet volání funkce.

#### Základní myšlenka

- minimum funkce leží v intervalu $\langle a,b \rangle$
- interval se zužuje pomocí **pevného poměru**
- v každé iteraci se zahazuje část intervalu, ve které minimum neleží
- jedna funkční hodnota se přenáší do další iterace

#### Zlatý poměr

- používá se konstanta
$$
\varphi = \frac{\sqrt{5}-1}{2} \approx 0{,}618
$$
- doplňkový poměr
$$
1-\varphi \approx 0{,}382
$$

#### Volba bodů v intervalu

V každé iteraci se volí body:
$$
u = a + (1-\varphi)(b-a), \quad v = a + \varphi(b-a)
$$

- platí $a < u < v < b$
- počítají se hodnoty $f(u)$ a $f(v)$
- při zúžení intervalu se **jeden z bodů znovu použije**

#### Rozhodovací pravidlo

- pokud $f(u) < f(v)$  
  → minimum leží v intervalu $\langle a,v \rangle$

- pokud $f(u) > f(v)$  
  → minimum leží v intervalu $\langle u,b \rangle$

- nový interval je kratší než původní v konstantním poměru

#### Podmínky použití

- funkce je:
  - spojitá
  - **unimodální** na intervalu $\langle a,b \rangle$
- derivace nejsou potřeba
- známe interval obsahující minimum

#### Přesnost a ukončení

- algoritmus se ukončí, pokud platí
$$
|a-b| < \varepsilon
$$
- výsledkem je interval obsahující minimum
- aproximací minima je obvykle střed intervalu

#### Vlastnosti metody

- **výhody**
  - méně výpočtů funkčních hodnot než trisekce
  - efektivní a stabilní
  - jednoduchá implementace

- **nevýhody**
  - pomalejší než derivační metody
  - použitelná pouze pro jednu proměnnou

#### Zařazení mezi metody

- metoda **bez derivací**
- minimalizace **jedné proměnné**
- intervalová metoda

→ efektivnější varianta metody [Trisekce](0411_Trisekce.md)  
→ základ pro [Fibonacciho metodu](0413_Fibonacci.md)
