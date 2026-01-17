# Převod ODR vyššího řádu na soustavu 1. řádu
Numerické metody jsou standardně formulovány pro diferenciální rovnice prvního řádu. Proto je nutné obyčejné diferenciální rovnice vyššího řádu převést na soustavu rovnic prvního řádu. Tento postup přímo navazuje na obecný pojem [[0000_ODR|obyčejné diferenciální rovnice]].

## Obecný tvar ODR vyššího řádu
Uvažujme obyčejnou diferenciální rovnici $n$-tého řádu ve tvaru
$$
y^{(n)} = f(t, y, y', \dots, y^{(n-1)})
$$
Cílem je přepsat tuto rovnici jako soustavu rovnic prvního řádu.

## Zavedení nových proměnných
Zavedeme nové proměnné odpovídající jednotlivým derivacím funkce $y(t)$
$$
\begin{aligned}
y_1 &= y, \\
y_2 &= y', \\
y_3 &= y'', \\
\vdots \\
y_n &= y^{(n-1)}
\end{aligned}
$$
Tímto způsobem lze vyjádřit všechny derivace až do řádu $n-1$. Následně zapíšeme derivace jednotlivých proměnných
$$
\begin{aligned}
y'_1 &= y_2, \\
y'_2 &= y_3, \\
\vdots \\
y'_{n-1} &= y_n, \\
y'_n &= f(t, y_1, y_2, \dots, y_n).
\end{aligned}
$$

## Příklad převodu – obecná nelineární rovnice
Uvažujme rovnici
$$
y'' = t + y
$$
Zavedeme nové proměnné
$$
\begin{aligned}
y_1 &= y, \\
y_2 &= y'
\end{aligned}
$$
a zapíšeme odpovídající soustavu rovnic prvního řádu
$$
\begin{aligned}
y_1' &= y_2, \\
y_2' &= t + y_1.
\end{aligned}
$$

## Příklad převodu – lineární homogenní rovnice
Uvažujme lineární diferenciální rovnici druhého řádu
$$
y'' + 3y' + 2y = 0
$$
Zavedeme nové proměnné
$$
\begin{aligned}
y_1 &= y, \\
y_2 &= y'
\end{aligned}
$$
Po úpravě dostaneme soustavu rovnic prvního řádu
$$
\begin{aligned}
y_1' &= y_2, \\
y_2' &= -3y_2 - 2y_1.
\end{aligned}
$$
---
Takto získaná soustava může být dále řešena [[0002_Lineární_soustavy_konstantní_koeficienty|analyticky]] nebo [[0005_Explicitni_Eulerova_metoda|numericky]] podle jejího typu.
