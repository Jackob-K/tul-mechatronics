# Rotační převodníky

Rotační převodníky slouží k přeměně tlakové energie kapaliny na mechanickou rotační energii. Typickými zástupci jsou hydraulické motory, které mohou být konstruovány jako lamelové nebo pístové.

## Hydraulické rotační převodníky
Hydraulické rotační převodníky jsou objemové stroje, jejichž základním parametrem je geometrický objem $V_0$. Tento objem určuje množství kapaliny teoreticky dodané do systému v režimu hydrogenerátoru nebo odebrané ze systému v režimu motoru při jedné otáčce.

## Kyvné motory

Kyvné motory vykonávají omezený rotační pohyb. Konstrukčně mohou být řešeny jako lamelové nebo pístové, přičemž princip přeměny energie je obdobný jako u rotačních motorů s plynulou rotací.

## Lamelový motor

Lamelový motor je tvořen rotorem s drážkami, ve kterých jsou uloženy lamely. Na lamely působí tlak kapaliny a vytváří výslednou sílu, která vyvolává točivý moment.

Teoretický točivý moment je dán vztahem
$$
M_t = S \, p_m \, z \, r,
$$
kde $S$ je účinná plocha lamely, $p_m$ střední tlak, $z$ počet lamel a $r$ rameno působící síly. Účinná plocha lamely je
$$
S = \frac{D - d}{2} \, b,
$$
a rameno
$$
r = \frac{D + d}{4}.
$$
Po úpravě lze psát
$$
M_t = D_m \, p_m.
$$

Skutečný točivý moment je
$$
M = M_t \, \eta_{hm}.
$$

Teoretický průtok je dán vztahem
$$
Q_0 = D_m \, \omega.
$$
Skutečný průtok je
$$
Q = \frac{Q_0}{\eta_v},
$$
a úhlová rychlost
$$
\omega = \frac{Q}{D_m} \, \eta_v.
$$
![|400](Schema_HM_lamelovy.png)

## Pístový motor

Pístový motor využívá tlak kapaliny působící na písty, které prostřednictvím mechanického převodu vytvářejí rotační pohyb.

Teoretický točivý moment je vyjádřen vztahem
$$
M_t = S \, p_m \, \frac{d}{2} = \frac{\pi D^2 d}{8} \, p_m = D_m \, p_m.
$$

Skutečný točivý moment je
$$
M = M_t \, \eta_{hm}.
$$

Teoretický průtok platí
$$
Q_0 = S \, v = S \, \frac{d}{2} \, \omega = D_m \, \omega,
$$
a skutečný průtok
$$
Q = \frac{Q_0}{\eta_v}.
$$
![|400](Schema_HM_pistovy.png)
![](Schema_Rotacni_prevodniky.jpeg)