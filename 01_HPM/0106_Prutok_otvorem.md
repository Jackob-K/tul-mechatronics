# Průtok otvorem a funkčními vůlemi

Průtok otvorem je zpravidla považován za turbulentní proudění, i když se nejedná o proudění v potrubí.

## Průtok kapaliny otvorem

U kapaliny je vliv stlačitelnosti a viskozity vzhledem k rozměrům otvoru zanedbatelný. Platí stavová rovnice
$$
\rho = konst.
$$
Objemový průtok je dán vztahem
$$
Q = S \, w,
$$
kde $S$ je plocha otvoru a $w$ střední rychlost proudění. Po úpravě a integraci se získá průtoková rovnice
$$
Q = \mu \, S \, \sqrt{\frac{2}{\rho} \, \Delta p},
$$
kde $\mu$ je bezrozměrný součinitel, který je funkcí geometrie otvoru.

Průtokovou rovnici lze zapisovat i v alternativních tvarech
$$
Q = G \, \sqrt{\Delta p},
$$
$$
Q = \sqrt{\frac{\Delta p}{R}},
$$
$$
\Delta p = R \, Q^2.
$$

## Průtok funkčními vůlemi

Funkční vůle lze modelovat jako štěrbinu, tedy prostor s jedním rozměrem výrazně menším než ostatní. Proudění je omezeno nepoddajnými stěnami a v reálných systémech vzniká nejčastěji v důsledku výrobních nepřesností nebo záměrně vytvořených vůlí.

Štěrbina je tvořena rovnoběžnými deskami o délce $l$ a šířce $b$ se vzájemnou vzdáleností $h$, přičemž $h \ll b$. Proudění je laminární ve směru osy $x$ a probíhá při konstantní teplotě a konstantní viskozitě.

Na základě řešení proudění mezi deskami platí vztah
$$
Q_p = \frac{\Delta p}{R_s} = G_s \, \Delta p,
$$
kde $R_s$ je svodový odpor a $G_s$ svodová propustnost.

Pro prizmatickou štěrbinu je průtok dán vztahem
$$
Q_p = \frac{b \, h^3}{12 \, \eta \, l} \, \cdot \Delta p.
$$
