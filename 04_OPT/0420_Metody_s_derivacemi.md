# Metody s derivacemi

Metody s derivacemi slouží k hledání **kořenů** a **minim funkcí** pomocí informací o derivacích účelové funkce. Oproti metodám bez derivací jsou zpravidla **rychlejší**, ale kladou vyšší nároky na hladkost funkce a volbu počátečního bodu.

#### Základní úloha

- minimalizace funkce jedné proměnné
$$
\min f(x)
$$
- nebo hledání kořene funkce
$$
f(x) = 0
$$
- metody jsou obvykle **iterační**
- vyžadují **počáteční bod** $x_0$

#### Kořen a minimum funkce

- **kořen funkce**
  - hodnota $x$, pro kterou platí
$$
f(x) = 0
$$
  - funkce protíná nebo se dotýká osy $x$

- **minimum funkce**
  - bod, kde má funkce nejmenší hodnotu
  - v minimu platí
$$
f'(x^*) = 0, \quad f''(x^*) > 0
$$
- hledání minima se často převádí na hledání kořene derivace

#### Charakter metod s derivacemi

- využívají:
  - **první derivaci**
  - často i **druhou derivaci**
- rozdíl mezi metodami není v principu, ale v cíli:
  - hledání kořene
  - hledání minima
- typickým zástupcem je **Newtonova metoda**

#### Počáteční bod

- **počáteční bod $x_0$** je nutný pro iterační metody
- musí:
  - ležet v oblasti, kde existují derivace
  - být rozumně blízko řešení
- špatná volba může vést:
  - ke konvergenci k maximu
  - k inflexnímu bodu
  - k divergenci metody

#### Přesnost a ukončení

- výpočet se ukončuje při splnění některého z kritérií:
  - **velikost derivace**
$$
|f'(x_k)| < \varepsilon
$$
  - **změna mezi iteracemi**
$$
|x_{k+1}-x_k| < \varepsilon
$$
  - **maximální počet iterací**

#### Výpočet derivací

- **analytický**
  - derivace dány vzorcem
  - rychlý a přesný
- **numerický**
  - derivace jsou pouze odhadnuty
  - pomalejší
  - méně stabilní

#### Vlastnosti metod

- **výhody**
  - rychlá konvergence
  - vysoká přesnost
- **nevýhody**
  - nutnost znalosti derivací
  - citlivost na počáteční bod
  - vyšší nároky na hladkost funkce

#### Zařazení mezi metody

- metody **s derivacemi**
- minimalizace **jedné proměnné**
- iterační metody

→ konkrétní postup je rozpracován v kapitole [Newtonova metoda](0421_Newtonova_metoda_1D.md)
