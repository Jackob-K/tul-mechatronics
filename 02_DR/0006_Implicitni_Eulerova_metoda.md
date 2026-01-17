# Implicitní Eulerova metoda
Implicitní Eulerova metoda je numerická metoda pro řešení Cauchyovy úlohy
$$
y'(t) = f(t,y), \qquad y(t_0) = y_0.
$$
Oproti explicitní Eulerově metodě je stabilnější a je vhodná zejména pro tuhé rovnice.
Viz [[0008_Stabilita_Stiff_problemy|stabilita a tuhé rovnice]]

## Základní vzorec
Implicitní Eulerova metoda je dána vztahem
$$
y_{n+1} = y_n + h f(t_{n+1}, y_{n+1}).
$$
Na pravé straně se již vyskytuje hodnota $y_{n+1}$, proto není vzorec přímo použitelný a je nutné řešit rovnici pro $y_{n+1}$.

## Postup výpočtu
#### 1)
Dosadíme do implicitního vztahu.
#### 2)
Vznikne (obecně nelineární) rovnice pro $y_{n+1}$.
#### 3)
Rovnici vyřešíme (ručně nebo numericky).
#### 4)
S vypočtenou hodnotou pokračujeme na další krok.

## Příklad
Uvažujme Cauchyovu úlohu
$$
y' = y,\qquad y(0) = 1,\qquad h = 0{,}1.
$$
Použitím implicitního Eulerova vzorce dostaneme
$$
y_{n+1} = y_n + h y_{n+1}.
$$
Po úpravě
$$
y_{n+1} - h y_{n+1} = y_n,
$$
$$
y_{n+1}(1 - h) = y_n,
$$
tedy
$$
y_{n+1} = \frac{y_n}{1 - h}.
$$

## Řešení nelineární rovnice
V obecném případě může vzniknout nelineární rovnice, například
$$
y_{n+1} = y_n + h (y_{n+1})^2.
$$
V takovém případě se hodnota $y_{n+1}$ určuje numericky, typicky pomocí [[0007_Newtonova_metoda|Newtonovy metody]].
