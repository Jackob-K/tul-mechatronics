# Vlastnosti nositele energie

V systémech přenosu energie dochází k přeměně hlavního druhu přenášené energie. V reálných mechanismech jsou tyto přeměny vždy spojeny se ztrátami, které se projevují snížením účinnosti. V hydraulických a pneumatických mechanismech se tlaková energie částečně mění na energii kinetickou, deformační a tepelnou, přičemž tyto přeměny vedou k objemovým a energetickým ztrátám. Vlastnosti nositele energie proto významně ovlivňují chování celého systému.

## Vzduch

Vzduch je v technických výpočtech nejčastěji popisován modelem ideálního plynu. Tento model předpokládá stlačitelné prostředí bez vnitřního tření. Vztah mezi tlakem, hustotou a teplotou ideálního plynu je popsán stavovou rovnicí
$$
p \, v = \frac{p}{\rho} = r \, T.
$$
Tato rovnice vyjadřuje základní vazbu mezi stavovými veličinami plynu a tvoří výchozí vztah pro analýzu pneumatických systémů.

| Veličina | Popis                   |   Jednotka    |
| :------: | ----------------------- | :-----------: |
|   $p$    | absolutní tlak          |     $Pa$      |
|   $v$    | měrný objem             |   $m^3/kg$    |
|  $\rho$  | hustota                 |   $kg/m^3$    |
|   $T$    | absolutní teplota       |      $K$      |
|   $r$    | měrná plynová konstanta | $J/(kg \, K)$ |

## Kapalina

Kapalina je v základních modelech často uvažována jako ideální, tedy nestlačitelná a bez vnitřního tření. Za těchto předpokladů je hustota kapaliny považována za konstantní a nezávislou na tlaku a teplotě:
$$
\rho = konst.
$$
Tento model je použitelný pouze v omezeném rozsahu stavů, kdy jsou změny tlaku a teploty malé a objem kapaliny se prakticky nemění.

## Reálná kapalina

Reálné kapaliny jsou do určité míry stlačitelné a jejich hustota závisí na tlaku a teplotě:
$$
\rho = \rho(p, T).
$$
Chování reálných kapalin nelze přímo odvodit z kinetické teorie plynů a jejich popis je založen převážně na experimentálně zjištěných závislostech. Tyto vlastnosti jsou významné zejména při vysokých tlacích a větších teplotních změnách.
![Závislot hustoty na tlaku a teplotě](Graph_Density_water_temperature_pressure.png)

## Stlačitelnost kapaliny a vlivy na nosič energie

Objemová stlačitelnost kapaliny je charakterizována objemovým modulem pružnosti kapaliny $E_k$, který vyjadřuje odpor kapaliny proti objemové deformaci způsobené změnou tlaku. Pro běžné hydraulické kapaliny nabývá objemový modul přibližných hodnot
$$
E_k \approx (1{,}4\text{–}1{,}6) \cdot 10^9.
$$
Změna objemu kapaliny je ovlivněna nejen tlakem, ale také teplotou. Tento vliv je popsán součinitelem objemové teplotní roztažnosti $\alpha$, jehož běžná hodnota je přibližně
$$
\alpha \approx 7 \cdot 10^{-4}.
$$

### Vliv nerozpuštěných plynů a par

V reálných hydraulických systémech se kapalina často vyskytuje ve směsi s nerozpuštěnými plyny, typicky ve formě vzduchových bublinek. Přítomnost plynu výrazně ovlivňuje výslednou stlačitelnost nosiče energie. Pro popis tohoto jevu se zavádí ekvivalentní objemový modul $E_e$, který zahrnuje vliv kapaliny i plynu.

Poměr ekvivalentního objemového modulu k objemovému modulu kapaliny je dán vztahem
$$
\frac{E_e}{E_k} =
\frac{1 + \alpha \left( \frac{p}{p_a} \right)^{1/n}}
{1 + \frac{\alpha E_k}{n p} \left( \frac{p}{p_a} \right)^{1/n}},
$$
kde exponent $n$ charakterizuje průběh děje stlačování plynu.

Bezrozměrný parametr $\alpha$ je definován jako poměr objemu plynu k objemu kapaliny při atmosférickém tlaku:
$$
\alpha = \frac{V_a}{V_k}.
$$
Tento parametr vyjadřuje množství vzduchu obsaženého v kapalině a má zásadní vliv na výslednou poddajnost systému.
![Vliv nerozpuštěných plynů](vliv_nerozpustenych_plynu_Ee_Ek.svg)


### Vliv poddajnosti stěn

Dalším významným faktorem ovlivňujícím stlačitelnost hydraulického systému je pružná deformace stěn potrubí a pracovních prostor. Poddajnost stěn způsobuje dodatečné zvětšení objemu při nárůstu tlaku, čímž se dále snižuje výsledný ekvivalentní objemový modul soustavy.

Celková poddajnost systému je dána kombinací stlačitelnosti kapaliny, přítomnosti nerozpuštěných plynů a mechanické poddajnosti stěn. Tyto vlivy se výrazně projevují zejména při nízkých tlacích a u systémů s vyšším obsahem plynu nebo tenkostěnnými konstrukčními prvky.
![Vliv poddajnosti stěn](vliv_poddajnosti_sten.svg)

## Viskozita kapalin

Viskozita vyjadřuje vnitřní odpor kapaliny proti proudění. Minerální oleje používané v hydraulických systémech jsou newtonovské kapaliny, jejichž dynamická viskozita nezávisí na rychlostním spádu.

Viskozita kapaliny se mění s provozními podmínkami. Se vzrůstající teplotou viskozita klesá, zatímco se zvyšujícím se tlakem viskozita roste.
![Viskozita kapalin|300](Graf_Viskozita_kapalin.png)

### Závislost viskozity na teplotě

Se zvyšující se teplotou dochází k poklesu viskozity. Tento jev je výrazný zejména u hydraulických olejů.

### Závislost viskozity na tlaku

Se zvyšujícím se tlakem viskozita kapaliny roste.
![Viskozita kapaliny závislá na teplotě](Graf_Vizkozita_na_tlaku.png)

### Porovnání vzduchu a oleje

Změny viskozity vzduchu s tlakem a teplotou jsou menší než u oleje. U oleje jsou závislosti viskozity na tlaku i teplotě výraznější.

## Hustota

Hustota vzduchu výrazně závisí na tlaku a teplotě. Hustota oleje se s tlakem a teplotou mění méně, avšak tyto změny nejsou zanedbatelné.
![Vlastnosti Vzduchu a oleje](Graf_Vlastnosti_vzduchu_oleje.png)
