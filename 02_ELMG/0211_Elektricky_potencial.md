## Elektrický potenciál – $\varphi \; [V]$
- Skalární fyzikální veličina charakterizující elektrické pole
- Vyjadřuje potenciální energii jednotkového elektrického náboje
- Udává práci potřebnou k přenesení jednotkového náboje z referenčního bodu
- Za nulový potenciál se obvykle volí nekonečno nebo povrch Země

$$
\varphi(\vec{r}_2) = \frac{1}{4\pi \varepsilon_0 \varepsilon_r} \int_V \frac{\rho(\vec{r}_1)}{|\vec{r}_2 - \vec{r}_1|} \, dV
$$

| Symbol | Význam |
|------|--------|
| $\varphi(\vec{r}_2)$ | elektrický potenciál v bodě $\vec{r}_2$ |
| $\rho(\vec{r}_1)$ | objemová hustota náboje |
| $\varepsilon_0$ | permitivita vakua |
| $\varepsilon_r$ | relativní permitivita prostředí |
| $\vec{r}_1, \vec{r}_2$ | polohové vektory |
| $V$ | integrační objem |

### Coulombův potenciál bodového náboje
$$
\varphi = \frac{1}{4\pi \varepsilon_0 \varepsilon_r} \cdot \frac{Q}{r}
$$

| Symbol | Význam |
|------|--------|
| $Q$ | bodový elektrický náboj |
| $r$ | vzdálenost od náboje |
| $\varepsilon_0$ | permitivita vakua |
| $\varepsilon_r$ | relativní permitivita prostředí |

### Vztah intenzity pole a potenciálu
- Elektrická intenzita je dána záporným gradientem elektrického potenciálu
$$
\vec{E} = - \nabla \varphi
$$

| Symbol | Význam |
|------|--------|
| $\vec{E}$ | intenzita elektrického pole |
| $\nabla \varphi$ | gradient elektrického potenciálu |

### Poissonova a Laplaceova rovnice
- Dosazením vztahu mezi intenzitou pole a potenciálem do Gaussova zákona vzniká Poissonova rovnice
$$
\nabla^2 \varphi = - \frac{\rho}{\varepsilon_0}
$$

| Symbol | Význam |
|------|--------|
| $\nabla^2 \varphi$ | Laplaceův operátor |
| $\rho$ | hustota elektrického náboje |
| $\varepsilon_0$ | permitivita vakua |

- V případě, kdy v prostoru není přítomen elektrický náboj ($\rho = 0$), přechází Poissonova rovnice v Laplaceovu rovnici
$$
\nabla^2 \varphi = 0
$$

### Potenciální energie elektrického pole
- Potenciální energie elektrického náboje v elektrickém poli je dána elektrickým potenciálem

$$
E_p = Q \cdot \varphi
$$

| Symbol    | Význam               |
| --------- | -------------------- |
| $E_p$     | potenciální energie  |
| $Q$       | elektrický náboj     |
| $\varphi$ | elektrický potenciál |

### Elektrické napětí – $U \; [V]$
- Elektrické napětí je rozdíl elektrických potenciálů mezi dvěma body
$$
U = \varphi_1 - \varphi_2
$$

| Symbol      | Význam                        |
| ----------- | ----------------------------- |
| $U$         | elektrické napětí             |
| $\varphi_i$ | elektrický potenciál v bodě i |
