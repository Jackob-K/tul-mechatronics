# Variace konstant (lineární soustava s pravou stranou)

Uvažujme nehomogenní lineární soustavu diferenciálních rovnic prvního řádu
$$
y'(t) = A y(t) + g(t),
$$
kde $A$ je konstantní matice a $g(t)$ je daná vektorová funkce. Metoda variace konstant umožňuje nalézt řešení této soustavy pomocí fundamentální matice odpovídající homogenní soustavě.

Tento postup přímo navazuje na pojem fundamentální matice.

→ [[0003_Fundamentální_matice|fundamentální matice]]

## Homogenní soustava

Nejprve uvažujme homogenní soustavu
$$
y'(t) = A y(t).
$$

Jejím obecným řešením je
$$
y(t) = \Phi(t)\,c,
$$
kde $\Phi(t)$ je fundamentální matice a $c$ je konstantní vektor.

## Metoda variace konstant

V metodě variace konstant již vektor $c$ nepovažujeme za konstantní, ale za funkci času $c(t)$. Hledané řešení nehomogenní soustavy má tvar
$$
y(t) = \Phi(t)\,c(t).
$$

Dosazením tohoto tvaru do původní rovnice dostáváme vztah
$$
y(t) = \Phi(t)\left( \int \Phi^{-1}(t)\,g(t)\,dt + c \right).
$$

## Tvar fundamentální matice

Ve většině praktických případů platí
$$
\Phi(t) = e^{A t},
$$
odkud plyne
$$
\Phi^{-1}(t) = e^{-A t}.
$$

Například pro diagonální matici $A$ s vlastními čísly $\lambda_1, \lambda_2$ má fundamentální matice tvar
$$
\Phi(t) =
\begin{pmatrix}
e^{\lambda_1 t} & 0 \\
0 & e^{\lambda_2 t}
\end{pmatrix},
\qquad
\Phi^{-1}(t) =
\begin{pmatrix}
e^{-\lambda_1 t} & 0 \\
0 & e^{-\lambda_2 t}
\end{pmatrix}.
$$
