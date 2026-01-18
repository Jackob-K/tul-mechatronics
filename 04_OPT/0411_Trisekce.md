## Trisekce

Metoda trisekce je **bezderivační metoda** pro minimalizaci **unimodální funkce jedné proměnné**. Patří mezi nejjednodušší intervalové metody a slouží především k pochopení základního principu zúžování intervalu s minimem.

Tato metoda může být dále optimalizována viz metoda [Zlatého řezu](0412_Zlaty_rez.md) nebo [Fibonacciho](0413_Fibonacci.md)

### Základní myšlenka

- minimum funkce leží v intervalu $\langle a,b \rangle$
- interval se v každém kroku rozdělí na **tři části**
- porovnáním funkčních hodnot se jedna třetina intervalu zahodí
- minimum zůstává vždy uvnitř nového, menšího intervalu

### Rozdělení intervalu

V každé iteraci se zvolí dva body:
$$
u = a + \frac{b-a}{3}, \quad v = b - \frac{b-a}{3}
$$

- platí $a < u < v < b$
- spočítají se hodnoty $f(u)$ a $f(v)$

### Rozhodovací pravidlo

- pokud $f(u) < f(v)$  
  → minimum leží v intervalu $\langle a,v \rangle$

- pokud $f(u) > f(v)$  
  → minimum leží v intervalu $\langle u,b \rangle$

- v každém kroku se délka intervalu zmenší na $\frac{2}{3}$ původní délky

### Podmínky použití

- funkce je:
  - **spojitá**
  - **unimodální** na intervalu $\langle a,b \rangle$
- derivace nejsou potřeba
- známe počáteční interval, ve kterém leží minimum

### Přesnost a ukončení

- algoritmus končí, pokud:
$$
|a-b| < \epsilon
$$
- výsledkem je interval obsahující bod minima
- za aproximaci minima se často bere střed intervalu

### Vlastnosti metody

- **výhody**
  - velmi jednoduchá
  - snadná implementace
  - robustní

- **nevýhody**
  - pomalejší než zlatý řez
  - v každé iteraci vyžaduje dva nové výpočty $f(x)$
  - nevyužívá dříve vypočtené hodnoty

### Zařazení mezi metody

- metoda **bez derivací**
- minimalizace **jedné proměnné**
- intervalová metoda
