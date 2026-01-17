# Řídicí prvky

Řídicí prvky hydraulických obvodů slouží ke změně, usměrnění a regulaci průtoku tlakové kapaliny. Všechny řídicí prvky pracují na principu proměnného hydraulického odporu, přičemž výsledný účinek závisí na způsobu změny tohoto odporu a na konstrukčním provedení prvku.

Na základě způsobu ovládání se řídicí prvky rozdělují na:
- konvenční – seřizované a ovládané ručně, mechanicky nebo elektromagneticky  
- proporcionální – schopné plynulé regulace, zpravidla spolupracující s PLC nebo CNC systémem, obvykle bez vnitřní zpětné vazby  
- servoventily – vysoce přesné zpětnovazební prvky řízené elektronicky (PLC nebo CNC)

## Jednosměrné (zpětné) ventily – VJ

Jednosměrné ventily umožňují samočinné proudění kapaliny pouze v jednom směru. V opačném směru je průtok zablokován.

Základní vlastnosti jednosměrných ventilů:
- samočinné hrazení průtoku v jednom směru  
- hrazení je zajištěno dosednutím funkčního prvku, kterým je kulička nebo kužel  
- funkční prvek je zpravidla přitlačován pružinou  
- ventil může pracovat v libovolné montážní poloze, u některých konstrukcí se doporučuje svislá montáž  

Jednosměrné ventily se vyznačují tlakovou ztrátou, která roste s průtokem a závisí na konstrukci ventilu.
![](Schema_VJ.png)
## Řízené jednosměrné ventily

Řízený jednosměrný ventil kombinuje funkci samočinného hrazení s možností nuceného otevření nebo uzavření.

Charakteristické vlastnosti:
- samočinné hrazení průtoku v jednom směru  
- možnost řízeného otevření ventilu pomocí řídicího tlaku  
- využití zejména pro zajištění polohy hydromotorů a hydraulických válců  

Řízené jednosměrné ventily se používají tam, kde je požadováno bezpečné zablokování pohybu při výpadku tlaku a současně možnost řízeného uvolnění.
![](Schema_VJ_rizene.png)
## Charakteristika zpětných ventilů 

Charakteristika zpětného ventilu vyjadřuje závislost tlakové ztráty $\Delta p$ na průtoku $Q$. Pro otevřený směr je charakteristika nelineární a závislá na konstrukci ventilu. Pro zavřený směr je průtok prakticky nulový až do dosažení destrukčních tlaků.

Typická charakteristika zahrnuje:
- otevírací tlak ventilu  
- nárůst tlakové ztráty s rostoucím průtokem  
- maximální dovolený průtok $Q_{max}$  
![](Graf_VJ_staticka_charka.png)
## Tlakové ventily – VT

Tlakové ventily slouží k omezení, regulaci a udržování tlaku v hydraulickém obvodu. Jsou základním bezpečnostním a regulačním prvkem každého hydraulického systému. Podle konstrukce a způsobu činnosti se rozlišují tlakové ventily přímo řízené a nepřímo řízené.
![](Schema_VT_znacka.png)

### Hydraulické tlakové ventily

Hydraulické tlakové ventily mohou být provedeny jako:
- jednostupňové – přímo řízené  
- dvoustupňové – nepřímo řízené  

Jednostupňové ventily reagují přímo na tlak působící na uzavírací prvek. Dvoustupňové ventily využívají pomocný řídicí stupeň, který umožňuje přesnější regulaci a menší kolísání tlaku při změnách průtoku.

### Seřízení tlakových ventilů

Pro nastavení požadované hodnoty tlaku $p_v$ je rozhodující pracovní tlak $p_p$ v místě připojení ventilu. Tlakový ventil může pracovat ve dvou základních režimech.

a) Přepouštěcí funkce  
Při dosažení nastaveného tlaku platí
$$
p_v = p_p \Rightarrow Q_v \neq 0,
$$
ventil se otevře a část průtoku je odváděna zpět do nádrže nebo do jiné části obvodu. Ventil tak omezuje maximální tlak v systému.

b) Pojistná funkce  
Při překročení nastavené hodnoty tlaku platí
$$
p_v > p_p \Rightarrow Q_v = 0,
$$
ventil zůstává uzavřen a otevře se pouze při nebezpečném nárůstu tlaku. Slouží jako ochrana obvodu proti přetížení.

### Umístění tlakových ventilů v obvodu

Tlakové ventily lze v hydraulickém obvodu umístit několika způsoby:
1) paralelně k větvi nebo části obvodu, ve které se řídí tlak  
2) sériově ve větvi nebo části obvodu, ve které má být řízen tlakový spád  
3) jako nedílnou součást každého zdroje tlakové kapaliny  

Volba umístění ventilu má zásadní vliv na chování obvodu, stabilitu tlaku a energetickou účinnost.

### Statická charakteristika tlakového ventilu

Statická charakteristika tlakového ventilu vyjadřuje závislost řízeného tlaku $p_p$ na průtoku ventilem $Q_v$, tedy funkci
$$
p_p = p_p(Q_v).
$$

Tato charakteristika se v praxi stanovuje experimentálně, protože tlakový ventil představuje proměnný hydraulický odpor, jehož velikost závisí na okamžité poloze regulačního prvku.

Tlakový ventil lze popsat jako odpor $R$, který reaguje:
- na vstupní tlak $p_p$  
- na velikost průtoku $Q_v$  
- při daném nastaveném tlaku $p_v$  

Pro tlakové poměry na ventilu platí
$$
p_p = p_v + \Delta p = p_v + R(p, Q) \cdot Q_v^2.
$$

Tlaková ztráta $\Delta p$ roste s průtokem a je závislá na konstrukci ventilu a jeho aktuálním otevření.

### Tlaková regulační diference

Tlaková regulační diference je rozdíl mezi nastaveným tlakem ventilu $p_v$ a skutečným pracovním tlakem $p_p$ při průtoku ventilem
$$
\Delta p_r = p_p - p_v.
$$

Tato diference vzniká v důsledku:
- nutného otevření regulačního prvku pro průchod průtoku  
- působení hydraulických sil na uzavírací prvek  
- deformace pružiny regulačního mechanismu  

Tlaková regulační diference:
- roste s rostoucím průtokem  
- závisí na tuhosti pružiny a tvaru regulačního prvku  
- je menší u dvoustupňových ventilů než u jednostupňových  

V oblasti malých průtoků je rozdíl tlaků malý, při vyšších průtocích dochází k výraznějšímu nárůstu pracovního tlaku nad nastavenou hodnotu.

### Tlaková uzavírací diference

Tlaková uzavírací diference je rozdíl mezi tlakem, při kterém se tlakový ventil otevře, a tlakem, při kterém se po poklesu tlaku opět uzavře
$$
\Delta p_u = p_{otev} - p_{uzav}.
$$
![](Graf_VT_uzaviraci_diference.png)
Tato diference vzniká zejména vlivem:
- tření pohyblivých částí ventilu  
- hystereze pružiny a mechanického systému  
- rozdílných hydraulických sil při otevírání a zavírání ventilu  

Tlaková uzavírací diference způsobuje, že ventil se při poklesu tlaku neuzavírá okamžitě při dosažení nastavené hodnoty $p_v$, ale až při nižším tlaku. Tento jev je důležitý z hlediska stability regulace a potlačení kmitání ventilu.

### Vliv výstupního průtočného průřezu a výstupního odporu

Statická charakteristika tlakového ventilu je ovlivněna také velikostí výstupního průtočného průřezu a výstupním hydraulickým odporem.

Zvětšení výstupního odporu způsobuje:
- posun charakteristiky k vyšším tlakům  
- zvětšení tlakové regulační diference  
- zvětšení tlakové uzavírací diference  
- snížení maximálního dosažitelného průtoku  

Maximální otevření regulačního prvku je omezeno konstrukčně. Pro maximální zdvih regulačního prvku platí vztah
$$
x_{max} = \frac{d^2}{5D},
$$
kde $d$ je průměr sedla a $D$ charakteristický rozměr regulačního prvku.
![](Graf_Vystupni_prutocny_prurez_vystupni_odpor.png)
Tyto vlivy je nutné zohlednit při návrhu hydraulického obvodu, zejména při dimenzování tlakového ventilu a navazujících spotřebičů.

## Hydraulické redukční ventily - VR

Hydraulické redukční ventily slouží ke snížení a udržování konstantního tlaku v určité části obvodu bez ohledu na tlak v hlavním přívodu. Provádějí se jako:
- jednostupňové  
- dvoustupňové  

Redukční ventil vytváří řízený tlakový spád mezi vstupním tlakem $p_p$ a výstupním tlakem $p_2$.
![](Schema_VR.png)
![](Schema_VR_znacka.png)
### Statická charakteristika redukčního ventilu

Statická charakteristika redukčního ventilu vyjadřuje závislost redukovaného tlaku $p_2$ na průtoku ventilem $Q_v$. Tato charakteristika se stanovuje experimentálně.
![](Graf_VR_staticka_charka.png)
Chování ventilu lze popsat vztahem
$$
p_2 = p_p - \Delta p = p_p - R(p, Q) \cdot Q_v^2,
$$
kde $R(p, Q)$ je proměnný hydraulický odpor ventilu závislý na tlaku a průtoku.

Regulační prvek redukčního ventilu reaguje na změnu výstupního tlaku $p_2$ a automaticky upravuje průtočný průřez tak, aby byl udržován nastavený tlak.

### Seřízení a zatížení redukčních ventilů

Seřízení redukčního ventilu se provádí na požadovaný redukovaný tlak při nulovém nebo minimálním průtoku. Ventil musí být při seřizování zatížen, aby bylo dosaženo stabilního pracovního stavu.

Redukční ventil se zpravidla zařazuje před spotřebič, jehož tlak má být omezen, a tvoří tak ochranu proti nadměrnému tlakovému namáhání.

## Škrticí ventily - VŠ

Škrticí ventily slouží k řízení průtoku tlakové kapaliny změnou hydraulického odporu. Pracují na principu škrcení proudu kapaliny v místě zúženého průtočného průřezu, přičemž regulace průtoku je dosažena změnou velikosti tohoto průřezu. Škrticí ventily se používají především pro řízení rychlosti pohybu hydraulických pohonů.

Z hlediska energetického je škrcení nehospodárný způsob regulace, protože přebytečná energie je disipována ve formě tlakové ztráty.

### Schematická značka

Škrticí ventil je ve schématech znázorňován symbolem proměnného odporu v potrubí. Značka vyjadřuje nastavitelné zúžení průtočného průřezu bez vazby na tlak v obvodu.
![](Schema_VS.png)

### Typy škrticích ventilů

Podle konstrukčního provedení se škrticí ventily dělí zejména na:
- jehlové – plynulá změna průtočného průřezu kuželovou jehlou, dobrá jemnost regulace  
- šoupátkové – změna průtočné plochy posuvem šoupátka, jednodušší konstrukce  
- štěrbinové – regulace průtoku změnou délky nebo šířky úzké štěrbiny, citlivé na nečistoty  

Jednotlivé typy se liší citlivostí regulace, tlakovými ztrátami a nároky na čistotu pracovní kapaliny.
![](Schema_VS_typ2.png)
![](Schema_VS_typ4.png)
### Průtoková charakteristika škrticího ventilu

Závislost průtoku $Q$ škrticím ventilem na tlakovém spádu $\Delta p$ při daném otevření ventilu je nelineární a lze ji obecně vyjádřit vztahem
$$
Q = Q(\Delta p)_{G_x}.
$$

Pro odpor typu ostrá hrana platí
$$
Q = \mu \cdot S_x \cdot \sqrt{\frac{2}{\rho} \cdot \Delta p},
$$
kde $\mu$ je součinitel průtoku, $S_x$ okamžitá průtočná plocha a $\rho$ hustota kapaliny.

Zavedením propustnosti $G_x$ lze vztah zapsat ve tvaru
$$
Q = G_x \cdot \sqrt{\Delta p}.
$$

Pro různé hodnoty otevření ventilu $x$ vzniká svazek průtokových charakteristik odpovídajících různým hodnotám $G_x$.
![](Graf_VS_Prutok_spad.png)

### Citlivost škrticího ventilu

Citlivost škrticího ventilu vyjadřuje změnu průtoku při malé změně otevření ventilu při konstantním tlakovém spádu
$$
\Delta p = konst.
$$

Citlivost je definována vztahem
$$
c = \frac{\delta Q}{\delta x}.
$$

Po dosazení za průtok platí
$$
c = \mu \cdot \frac{\delta S_x}{\delta x} \cdot \sqrt{\frac{2}{\rho}} \cdot \sqrt{\Delta p},
$$
resp.
$$
c = \frac{\delta G_x}{\delta x} \cdot \sqrt{\Delta p}.
$$

Citlivost regulace je výrazně ovlivněna geometrií průtočné plochy. Různý tvar regulačního prvku vede k odlišnému průběhu závislosti $Q = Q(x)$, a tím k rozdílným regulačním vlastnostem škrticího ventilu.
![](Graf_VS_Vlilv_geometrie.png)

## Rozváděče - R

Rozváděče slouží k rozdělování, spojování nebo změně směru proudění tlakové kapaliny v hydraulickém obvodu. Patří mezi diskrétní řídicí prvky s konečným počtem stabilních poloh.

Základní funkce rozváděčů:
- změna směru průtoku  
- připojení a odpojení jednotlivých větví obvodu  
- řízení pohybu hydromotorů a hydraulických válců  

## Rozdělení rozváděčů

Rozváděče se dělí podle počtu cest a počtu poloh.

Podle počtu cest:
- dvoucestné  
- třícestné  
- čtyřcestné  

Podle počtu poloh:
- dvoupolohové  
- třípolohové

Označení rozváděče je tvořeno kombinací počtu cest a počtu poloh, například 4/2 nebo 4/3.
![](Tabulka_Rozvadece_polohy.png)

## Provedení rozváděčů

Z konstrukčního hlediska se rozváděče provádějí jako:
- šoupátkové  
- sedlové  

Šoupátkové rozváděče umožňují plynulejší přechody mezi polohami, avšak vykazují větší vnitřní netěsnosti. Sedlové rozváděče mají velmi malé netěsnosti, ale jejich přepínání je skokové a vyžaduje vyšší ovládací síly.
![](Tabulka_Rozvadece_ovladani.png)
## Typy rozváděčů

Rozváděče lze z hlediska konstrukčního provedení rozdělit na šoupátkové a sedlové. Jednotlivé typy se liší způsobem hrazení průtoku, dosažitelnými pracovními tlaky, těsností a možnostmi konstrukčního uspořádání.

### a) Šoupátkové rozváděče

Šoupátkové rozváděče se používají převážně pro nižší pracovní tlaky. Jejich konstrukce je založena na posuvu šoupátka v tělese rozváděče, přičemž propojení jednotlivých kanálů je realizováno pomocí kruhových vybrání na šoupátku.

Vlastnosti šoupátkových rozváděčů:
- vhodné zejména pro nízké a střední pracovní tlaky  
- plynulejší přechody mezi jednotlivými polohami  
- větší vnitřní netěsnosti způsobené nutnou funkční vůlí  
- snadná realizace vícecestných a vícepolo­hových provedení  

Nevýhodou je složité radiální těsnění, které omezuje maximální tlak a zvyšuje nároky na přesnost výroby.

### b) Sedlové rozváděče

Sedlové rozváděče pracují na principu dosedání funkčního prvku, kterým je kulička nebo kuželka, do sedla. V základní poloze je uzávěr držen v sedle působením pružiny nebo tlaku kapaliny z prostoru připojeného k přívodu $P$.

Vlastnosti sedlových rozváděčů:
- velmi malé až zanedbatelné vnitřní netěsnosti  
- vhodné pro vysoké pracovní tlaky  
- skokové přepínání průtoku  
- omezená variabilita počtu cest a tvaru průtočných kanálů  

Sedlové rozváděče se používají zejména pro menší průtoky, kde je kladen důraz na těsnost a bezpečné uzavření.

## Splnění základních požadavků rozváděčů

### Dosažení nulové nebo minimální svodové propustnosti

U šoupátkových rozváděčů nelze vzhledem k nutné funkční vůli mezi šoupátkem a tělesem dosáhnout ideální těsnosti. Typická velikost této vůle je řádově jednotky mikrometrů, což představuje kompromis mezi těsností a odolností proti zadření.

Ke snížení svodové propustnosti se používají:
- přesné lícování funkčních ploch  
- povrchové úpravy snižující tření  
- vhodná volba materiálů  

Úplné uzavření průtoku lze zajistit pouze sedlovými rozváděči nebo použitím uzavíracích ventilů.

### Minimalizace odporu při proudění

Minimalizace tlakových ztrát je dosažena vhodným tvarem a dimenzováním průtočných kanálů. Proudění by mělo probíhat bez náhlých změn průřezu a směru.

Z konstrukčního hlediska platí:
- průtočné kanály musí být plynule tvarované  
- sedlové plochy jsou přesně obráběny  
- u šoupátkových rozváděčů jsou frézovány pouze lokální funkční plochy  

Splnění těchto požadavků má přímý vliv na energetickou účinnost a provozní spolehlivost hydraulického obvodu.
