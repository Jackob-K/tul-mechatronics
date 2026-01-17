# Hydromotor

Hydromotor převádí hydraulickou energii na mechanickou (rotační pohyb).

## Výpočtové schéma hydromotoru
- vstupní veličiny: průtok $Q_m$, tlak $p_m$
- výstupní veličiny: otáčky $n_m$, moment $M$
![|450](Schema_HM_vypocetni.png)

## Průtok hydromotorem

### Konstantní geometrický objem
$$
Q_m = V_0 \cdot n_m + C_m \cdot p_m = Q_0 + Q_z
$$

### Proměnný geometrický objem
$$
Q_m = V_0 \cdot q_m \cdot n_m + C_m \cdot p_m
$$

- $V_0$ – geometrický objem  
- $q_m$ – regulační parametr hydromotoru  
- $C_m$ – koeficient netěsností  

## Statické charakteristiky hydromotoru
- **průtoková**
$$
Q_m = Q(p_m,\ \nu,\ T)
$$
![](Graf_Hydromotor_prutokova_charka.png)
- **otáčková**
$$
n_m = n(p_m,\ Q_m,\ \nu,\ T)
$$
![](Graf_Hydromotor_otackova_charka.png)
- **zátěžová**
$$
M = M(p_m,\ n_m)
$$

## Otáčková charakteristika

### Konstantní $V_0$
$$
n_m = \frac{Q_m}{V_0} - \frac{C_m}{V_0} \cdot p_m = n_0 - n_z
$$

### Proměnný $V_0$
$$
n_m = \frac{Q_m}{V_0 \cdot q_m} - \frac{C_m}{V_0 \cdot q_m} \cdot p_m
$$
## Momentová charakteristika hydromotoru

Moment hydromotoru je dán rozdílem teoretického momentu a momentu pasivních odporů.

$$
M = M_t - M_{po}
$$

### Teoretický moment
$$
M_t = \frac{V_0}{2\pi} \cdot p_m
$$

### Skutečný moment
$$
M = \frac{V_0}{2\pi} \cdot p_m - M_{po}
$$

- $M_{po}$ – moment pasivních odporů  
- hydromotor je **poměrně tuhý** (pokles momentu cca 2–5 %)
![](Graf_HM_Momentova_charka.png)

## Účinnosti hydromotoru

### Objemová účinnost
- zohledňuje vnitřní netěsnosti

$$
\eta_v = \frac{Q_0}{Q_m} = \frac{V_0 \cdot n_m}{Q_m}
$$

### Hydromechanická účinnost
- zohledňuje mechanické a hydraulické ztráty

$$
\eta_{hm} = \frac{M}{M_t} = \frac{2\pi \cdot M}{V_0 \cdot p_m}
$$

### Celková účinnost
$$
\eta_c = \eta_v \cdot \eta_{hm}
$$

## Parametry hydromotoru

- $V_0$ – geometrický objem $[\mathrm{cm^3}]$
- $n_n$ – jmenovité otáčky $[\mathrm{min^{-1}}]$
- $n_{min}$ – minimální otáčky
- $n_{max}$ – maximální otáčky
- $p_n$ – jmenovitý tlak $[\mathrm{MPa}]$
- $p_{max}$ – maximální tlak $[\mathrm{MPa}]$
