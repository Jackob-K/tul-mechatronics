# Newtonova metoda
Newtonova metoda je numerická metoda pro řešení rovnice
$$
F(x) = 0,
$$
kde $x$ je neznámá a $F(x)$ je (skalární nebo vektorová) funkce. Metoda je založena na lineární aproximaci funkce v okolí aktuálního odhadu řešení.

## Iterační vzorec
Základní iterační vztah Newtonovy metody má tvar
$$
x_{k+1} = x_k - J^{-1}(x_k) F(x_k),
$$
kde $x_k$ je aktuální odhad řešení, $F(x_k)$ je hodnota funkce v bodě $x_k$ a $J(x_k)$ je Jacobiho matice funkce $F$ v bodě $x_k$.

## Jacobiho matice
Jacobiho matice je matice parciálních derivací složek funkce $F$. Pro funkci
$$
F(x,y) =
\begin{pmatrix}
F_1(x,y) \\
F_2(x,y)
\end{pmatrix}
$$
má Jacobiho matice tvar
$$
J =
\begin{pmatrix}
\frac{\partial F_1}{\partial x} & \frac{\partial F_1}{\partial y} \\
\frac{\partial F_2}{\partial x} & \frac{\partial F_2}{\partial y}
\end{pmatrix}.
$$

## Použití v implicitní Eulerově metodě
Při použití implicitní Eulerovy metody
$$
y_{n+1} = y_n + h f(t_{n+1}, y_{n+1})
$$
nelze hodnotu $y_{n+1}$ určit přímo, protože se vyskytuje na obou stranách rovnice. Rovnici proto přepíšeme do tvaru
$$
F(y_{n+1}) = y_{n+1} - y_n - h f(t_{n+1}, y_{n+1}) = 0,
$$
kterou řešíme Newtonovou metodou (viz implicitní Eulerova metoda).

## Postup Newtonovy metody
#### 1)
Sestavíme rovnici
$$
F(x) = 0.
$$
#### 2)
Vypočteme Jacobiho matici $J(x)$.
#### 3)
Zvolíme počáteční odhad řešení, typicky $x_0 = y_n$.
#### 4)
Použijeme iterační vzorec
$$
x_{k+1} = x_k - J^{-1}(x_k) F(x_k).
$$

## Příklad (skalární rovnice)
Uvažujme rovnici
$$
F(x) = x - h x^2 - 1 = 0.
$$
Derivace má tvar
$$
F'(x) = 1 - 2hx.
$$
Newtonova iterace je dána vztahem
$$
x_{k+1} = x_k - \frac{x_k - h x_k^2 - 1}{1 - 2 h x_k}.
$$
