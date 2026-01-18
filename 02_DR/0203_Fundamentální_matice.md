# Fundamentální matice

Uvažujme soustavu lineárních obyčejných diferenciálních rovnic prvního řádu
$$
y'(t) = A\,y(t),
$$
kde $A$ je konstantní matice.  
V tomto případě lze řešení popsat pomocí **fundamentální matice** $\Phi(t)$, což je matice, jejíž sloupce tvoří lineárně nezávislá řešení dané soustavy.

Obecné řešení má tvar
$$
y(t) = \Phi(t)\,c,
$$
kde $c$ je konstantní vektor.

## Konstrukce fundamentální matice

Uvažujme soustavu
$$
y'(t) =
\begin{pmatrix}
1 & 0 \\
0 & 2
\end{pmatrix}
y(t).
$$

#### 1) Vlastní čísla
$$
\lambda_1 = 1,\quad \lambda_2 = 2
$$

#### 2) Vlastní vektory
$$
v_1 =
\begin{pmatrix}
1\\
0
\end{pmatrix},
\quad
v_2 =
\begin{pmatrix}
0\\
1
\end{pmatrix}
$$

#### 3) Jednotlivá řešení
$$
y_1(t) = e^{t}
\begin{pmatrix}
1\\
0
\end{pmatrix},
\quad
y_2(t) = e^{2t}
\begin{pmatrix}
0\\
1
\end{pmatrix}
$$

#### 4) Fundamentální matice  
(sloupce odpovídají jednotlivým řešením)
$$
\Phi(t) =
\begin{pmatrix}
e^{t} & 0 \\
0 & e^{2t}
\end{pmatrix}
$$

#### 5) Obecné řešení
$$
y(t) = \Phi(t)\,c =
\begin{pmatrix}
e^{t} & 0 \\
0 & e^{2t}
\end{pmatrix}
\begin{pmatrix}
c_1\\
c_2
\end{pmatrix}
$$

## Tahák

**Fundamentální matice** je matice řešení lineární soustavy.  
Její sloupce tvoří lineárně nezávislá řešení a obecné řešení lze vždy zapsat ve tvaru
$$
y(t) = \Phi(t)\,c.
$$
Fundamentální matice se konstruuje z vlastních čísel a příslušných vlastních vektorů matice $A$.

Fundamentální matice se využívá zejména při řešení nehomogenních soustav metodou [variace konstant](0204_Variace_konstant.md)
