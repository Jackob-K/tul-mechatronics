# Lineární soustavy s konstantními koeficienty

Uvažujme lineární soustavu diferenciálních rovnic prvního řádu ve tvaru
$$
y'(t) = A y(t),
$$
kde $y(t) \in \mathbb{R}^n$ je vektor neznámých funkcí a $A$ je konstantní matice. Řešení této soustavy je určeno vlastnostmi matice $A$, zejména jejími vlastními čísly a vlastními vektory.

## Vlastní čísla matice $A$

Vlastní čísla matice $A$ jsou dána charakteristickou rovnicí
$$
\det(A - \lambda I) = 0.
$$

Na základě vlastních čísel lze určit tvar obecného řešení soustavy.

## Typ řešení podle vlastních čísel

| Typ vlastních čísel                     | Tvar řešení |
| --------------------------------------- | ----------- |
| Reálná různá $\lambda_1, \lambda_2$     | $y = c_1 e^{\lambda_1 t} v_1 + c_2 e^{\lambda_2 t} v_2$ |
| Reálná stejná $\lambda_1 = \lambda_2$   | $y = (c_1 v + c_2 (t v + w)) e^{\lambda t}$ |
| Komplexní $\lambda = \alpha \pm i\beta$ | $y = e^{\alpha t} \left[ c_1 (v_1 \cos \beta t - v_2 \sin \beta t) + c_2 (v_1 \sin \beta t + v_2 \cos \beta t) \right]$ |

Vektory $v$, $v_1$, $v_2$ označují vlastní (popř. zobecněné vlastní) vektory odpovídající příslušným vlastním číslům.

## Příklad – reálná vlastní čísla

Uvažujme soustavu
$$
y' =
\begin{pmatrix}
2 & 0 \\
0 & 1
\end{pmatrix}
y.
$$

Charakteristický polynom je
$$
\det(A - \lambda I) = (2 - \lambda)(1 - \lambda),
$$
odkud dostáváme vlastní čísla
$$
\lambda_1 = 2,\quad \lambda_2 = 1.
$$

Příslušné vlastní vektory jsou
$$
v_1 =
\begin{pmatrix}
1 \\
0
\end{pmatrix},
\quad
v_2 =
\begin{pmatrix}
0 \\
1
\end{pmatrix}.
$$

Obecné řešení má tvar
$$
y(t) = c_1 e^{2t}
\begin{pmatrix}
1 \\
0
\end{pmatrix}
+ c_2 e^{t}
\begin{pmatrix}
0 \\
1
\end{pmatrix}.
$$

## Příklad – komplexní vlastní čísla

Uvažujme soustavu
$$
y' =
\begin{pmatrix}
0 & -1 \\
1 & 0
\end{pmatrix}
y.
$$

Charakteristická rovnice má tvar
$$
\det(A - \lambda I) = \lambda^2 + 1 = 0,
$$
odkud plyne
$$
\lambda = \pm i,\quad \alpha = 0,\ \beta = 1.
$$

Obecné řešení soustavy lze zapsat ve tvaru
$$
y(t) =
c_1
\begin{pmatrix}
\cos t \\
\sin t
\end{pmatrix}
+
c_2
\begin{pmatrix}
-\sin t \\
\cos t
\end{pmatrix}.
$$
Takto získaná lineárně nezávislá řešení lze uspořádat do sloupců fundamentální matice soustavy.
→ [[0003_Fundamentální_matice|fundamentální matice]]