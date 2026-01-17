# Stabilita a stiff problémy

## Testovací rovnice
Základním nástrojem pro studium stability numerických metod je testovací rovnice
$$
y' = \lambda y.
$$
Jejím přesným řešením je
$$
y(t) = e^{\lambda t} y_0.
$$
Pokud $\operatorname{Re}(\lambda) < 0$, skutečné řešení klesá k nule. Tato rovnice se používá k testování stability numerických metod.

## Absolutní stabilita
Numerická metoda je absolutně stabilní, pokud při řešení testovací rovnice
$$
y' = \lambda y
$$
dává řešení, které sice nemusí být nejpřesnější, ale klesá k nule stejně jako přesné řešení. Metoda se destabilizuje tehdy, když hodnoty $y_n$ začnou růst.

## Explicitní Eulerova metoda a stabilita
Pro explicitní Eulerovu metodu platí
$$
y_{n+1} = y_n + h \lambda y_n = (1 + h\lambda) y_n.
$$
Aby numerické řešení nerostlo, musí být splněna podmínka
$$
|1 + h\lambda| < 1.
$$
Pro reálné $\lambda < 0$ z toho plyne nerovnost
$$
-2 < h\lambda < 0,
$$
což znamená, že krok $h$ musí být velmi malý.

## Selhání explicitní Eulerovy metody
U rovnic s velmi záporným parametrem $\lambda$ vychází podmínka stability ve tvaru
$$
h < \frac{2}{|\lambda|}.
$$
Numerická metoda je tedy nucena používat extrémně malý krok, aby se řešení nestalo nestabilním.

## Stiff problém
Stiff problém je diferenciální rovnice nebo soustava rovnic, ve které se současně vyskytují rychlé a pomalé složky řešení. Tyto problémy typicky obsahují velmi záporná vlastní čísla a nutí explicitní numerické metody k použití velmi malého kroku.

## Volba kroku
Velikost kroku je u stiff problémů omezena stabilitou metody, nikoli volbou uživatele. Parametr $\lambda$, který je vlastním číslem matice soustavy, přímo určuje maximální přípustnou velikost kroku.
