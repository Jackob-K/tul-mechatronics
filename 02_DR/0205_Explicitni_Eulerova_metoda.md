# Explicitní Eulerova metoda
Explicitní Eulerova metoda je numerická metoda pro přibližné řešení Cauchyovy úlohy
$$
y'(t) = f(t,y), \qquad y(t_0) = y_0.
$$
Místo přesného řešení získáváme pouze aproximace řešení v diskrétních časových bodech.

## Základní vzorec
Aproximační vztah má tvar
$$
y_{n+1} = y_n + h f(t_n, y_n),
$$
kde $h$ je krok metody, $t_n = t_0 + n h$ a $y_n$ je aproximace řešení v čase $t_n$.

## Postup výpočtu
#### 1)
Je dána rovnice
$$
y'(t) = f(t,y).
$$
#### 2)
Zvolíme krok metody $h$.
#### 3)
Vyjdeme z počáteční podmínky
$$
y_0 = y(t_0).
$$
#### 4)
Vypočteme
$$
y_{n+1} = y_n + h f(t_n, y_n).
$$
#### 5)
Aktualizujeme čas
$$
t_{n+1} = t_n + h.
$$
#### 6)
Postup opakujeme pro zadaný počet kroků.

## Příklad
Uvažujme Cauchyovu úlohu
$$
y' = y,\qquad y(0) = 1,\qquad h = 0{,}1.
$$
#### 1) Krok 0
$$
t_0 = 0,\qquad y_0 = 1.
$$
#### 2) Krok 1
$$
y_1 = y_0 + h y_0 = 1 + 1 \cdot 0{,}1 = 1{,}1.
$$
#### 3) Krok 2
$$
y_2 = y_1 + h y_1 = 1{,}1 + 1{,}1 \cdot 0{,}1 = 1{,}21.
$$
#### 4) Krok 3
$$
y_3 = y_2 + h y_2 = 1{,}21 + 1{,}21 \cdot 0{,}1 = 1{,}331.
$$
V bodě $t = 0{,}3$ tedy platí aproximace
$$
y(0{,}3) \approx 1{,}331.
$$

## Eulerova metoda pro soustavy
Uvažujme soustavu
$$
\begin{cases}
y_1' = f_1(t, y_1, y_2), \\
y_2' = f_2(t, y_1, y_2).
\end{cases}
$$
Explicitní Eulerova metoda se aplikuje na každou rovnici zvlášť
$$
y_{1,n+1} = y_{1,n} + h f_1(t_n, y_{1,n}, y_{2,n}),
$$
$$
y_{2,n+1} = y_{2,n} + h f_2(t_n, y_{1,n}, y_{2,n}).
$$
---
Explicitní Eulerova metoda je jednoduchá, ale může být nestabilní pro některé typy úloh.  
→ [[0006_Implicitni_Eulerova_metoda|implicitní Eulerova metoda]]  
→ [[0008_Stabilita_Stiff_problemy|stabilita a stiff problémy]]
