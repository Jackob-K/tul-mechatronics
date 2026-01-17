# Runge–Kuttovy metody
Runge–Kuttovy metody jsou numerické metody pro řešení Cauchyovy úlohy
$$
y'(t) = f(t,y), \qquad y(t_0) = y_0.
$$
Na rozdíl od Eulerovy metody nevyužívají pouze jeden směr v počátečním bodě, ale kombinují více směrů uvnitř jednoho kroku. Metody jsou stále explicitní, ale dosahují výrazně vyšší přesnosti.

## Typy Runge–Kuttových metod
Explicitní Runge–Kuttovy metody počítají nový krok přímo, bez řešení rovnic. Nejčastěji používanou metodou je metoda čtvrtého řádu (RK4).  
Implicitní Runge–Kuttovy metody vyžadují řešení soustavy rovnic, často pomocí Newtonovy metody, a vyznačují se lepší stabilitou, zejména pro stiff problémy.

## RK4 – Runge–Kuttova metoda čtvrtého řádu
Pro krok $h$ definujeme
$$
k_1 = f(t_n, y_n),
$$
$$
k_2 = f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} k_1\right),
$$
$$
k_3 = f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} k_2\right),
$$
$$
k_4 = f(t_n + h, y_n + h k_3).
$$
Nová hodnota řešení je dána vztahem
$$
y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4).
$$
Jednotlivé hodnoty $k_1, k_2, k_3, k_4$ odpovídají směrům v počátečním bodě, ve středu kroku a na jeho konci. Výsledná hodnota je jejich váženým průměrem, což vede ke čtvrtému řádu přesnosti. Oproti Eulerově metodě je RK4 při stejném kroku výrazně přesnější.

## Okrajové úlohy a metoda sítí

### Cauchyova úloha
Cauchyova úloha je zadána počáteční podmínkou v jednom bodě intervalu
$$
y'(t) = f(t,y), \qquad y(t_0) = y_0.
$$
Řešení se určuje postupně od počátečního bodu a je vhodné pro popis časového vývoje. Typicky se řeší metodami Eulerova typu nebo Runge–Kuttovými metodami.

### Okrajová úloha
U okrajové úlohy jsou podmínky zadány na více bodech intervalu
$$
y''(x) = f(x), \qquad y(a) = \alpha,\; y(b) = \beta.
$$
Řešení musí splnit obě okrajové podmínky současně a určuje se globálně na celém intervalu.

### Metoda sítí
Základní myšlenkou metody sítí je diskretizace intervalu $[a,b]$ na $N+1$ bodů
$$
x_0 = a,\; x_1,\; x_2,\; \dots,\; x_N = b,
$$
kde krok sítě je
$$
h = \frac{b-a}{N}.
$$
Derivace jsou nahrazeny konečnými diferencemi, například druhá derivace
$$
y''(x_i) \approx \frac{y_{i+1} - 2y_i + y_{i-1}}{h^2}.
$$
Tím vznikne diferenční rovnice, která představuje algebraický vztah mezi hodnotami v uzlech sítě. Pro každý vnitřní bod získáme jednu rovnici a neznámými jsou hodnoty
$$
y_1, y_2, \dots, y_{N-1}.
$$
Po dosazení okrajových podmínek
$$
y_0 = \alpha,\qquad y_N = \beta
$$
vznikne lineární soustava rovnic tvaru
$$
A y = b.
$$
