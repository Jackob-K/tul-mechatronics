# Hydraulická indukčnost

Hydraulická indukčnost vyjadřuje schopnost hydraulického systému klást odpor proti změně průtoku. Je dána hmotností pohybující se tekutiny a určuje tlakový spád nutný k jejímu urychlení.

Základní vztah mezi tlakovým spádem a časovou změnou průtoku má tvar
$$
\Delta p = H \, \frac{dQ}{dt},
$$
kde hydraulická indukčnost je definována vztahem
$$
H = \frac{m}{S^2} = \frac{\rho \, L}{S}.
$$

## Celková indukčnost

Celková indukčnost systému se skládá z indukčnosti tekutiny a indukčnosti mechanických částí:
$$
H_c = H + H_m.
$$
Tomu odpovídá tlakový spád
$$
\Delta p = H_c \, \frac{dQ}{dt}.
$$

## Indukčnost rotačního motoru
![|200](Schema_Rotacni_motor.png)

U rotačního motoru se do výpočtu indukčnosti zahrnuje pouze hmotnost tuhých částí, které jsou popsány konstantním momentem setrvačnosti $J_m$.

Zrychlující moment motoru je dán vztahem
$$
M_z = \Delta p \, \frac{V_0}{2\pi}.
$$
Po úpravě platí vztah
$$
\Delta p = H_m \, \frac{dQ}{dt},
$$
kde mechanická indukčnost rotačního motoru je
$$
H_m = \frac{J_m}{D^2}.
$$
Zde $V_0$ označuje geometrický objem motoru a $D$ konstrukční konstantu motoru.

## Shrnutí indukčnosti

- hydraulická indukčnost popisuje odpor systému proti změně průtoku  
- je způsobena pohybující se hmotností tekutiny a mechanických částí  
- skládá se z hydraulické složky $H$ a mechanické složky $H_m$  
- určuje tlakový spád potřebný k urychlení průtoku  
- na indukčnosti dochází k přeměně tlakové energie na kinetickou energii a opačně  
- při sériovém zapojení hydraulických prvků se indukčnosti sčítají
