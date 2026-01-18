# Metody s více proměnnými

Metody s více proměnnými se zabývají minimalizací funkcí, jejichž argumentem je vektor proměnných. Navazují na metody jedné proměnné, ale pracují s geometricky složitějšími objekty, jako jsou gradienty a matice druhých derivací.

### Základní formulace úlohy

- obecná optimalizační úloha má tvar
$$
\min f(x), \quad x \in \mathbb{R}^n
$$
- proměnná $x$ je vektor
- úloha **nemá omezení vazbami**
- hledáme lokální nebo globální minimum funkce

### Minimum funkce více proměnných

- minimum je bod, kde má funkce nejmenší hodnotu v okolí
- nutná podmínka minima
$$
\nabla f(x^*) = 0
$$
- postačující podmínka (lokální minimum)
  - Hessova matice je **pozitivně definitní**

### Gradient

- **gradient** je vektor prvních parciálních derivací
$$
\nabla f(x) =
\begin{pmatrix}
\frac{\partial f}{\partial x_1} \\
\vdots \\
\frac{\partial f}{\partial x_n}
\end{pmatrix}
$$
- určuje směr **největšího růstu** funkce
- směr největšího poklesu je opačný směr gradientu

### Hessova matice

- **Hessova matice** je matice druhých parciálních derivací
$$
H(x) =
\begin{pmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{pmatrix}
$$
- popisuje lokální zakřivení funkce
- používá se v Newtonových metodách

### Základní skupiny metod

- **Gradientní metody**
  - využívají pouze gradient
  - jednoduché, ale pomalejší
  - viz [Metoda největšího spádu](0426_Nejvetsi_spad.md)

- **Newtonovy metody**
  - využívají gradient i Hessovu matici
  - velmi rychlé v okolí minima
  - viz [Newtonova–Rhapsonova metoda](0427_Newton_rhapsonova.md)

- **Bezderivační metody**
  - nevyžadují derivace
  - pracují pouze s hodnotami funkce
  - vhodné pro malé dimenze
  - viz [Nelder–Meadova metoda](0428_Nelder_meadova_simplex.md)

### Charakteristika metod

- metody jsou většinou **iterační**
- vyžadují **počáteční bod** $x_0$
- konvergence závisí na:
  - vlastnostech funkce
  - volbě počátečního bodu
  - použité metodě
