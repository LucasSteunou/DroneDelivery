# Drone livreur de colis : recherche d’un chemin optimal
Au cours de ces dernières années, l’idée des livraisons automatisées par drone est devenue de plus
en plus concrète chez les entreprises du e-commerce. Nous nous sommes donc intéressés au sujet en
recherchant le trajet optimal que doit suivre le drone, afin de consommer un minimum d’énergie.
L’essor de la livraison en ville s’accompagne naturellement de nombreuses problématiques, telles
que la pollution engendrée ou l’engorgement des routes par les camions de livraison. Il est donc
naturel de s'intéresser à des alternatives innovantes, comme la livraison automatisée par drones.

## Ce TIPE fait l'objet d'un travail de groupe.
### Liste des membres du groupe :
 - STEUNOU Lucas
 - GINESTE Pierre
 - NEGRE Baptiste
 
# Positionnement thématique (ETAPE 1)
 INFORMATIQUE (Informatique pratique), INFORMATIQUE (Informatique Théorique),
PHYSIQUE (Mécanique).

# Mots-clés (ETAPE 1)
| Mots-Clés (en français) | Mots-Clés (en anglais) |
|---|---|
|Livraison par drone | Drone delivery |
| Graphe | Graph |
| Consommation d'énergie | Energy consumption |
|Optimisation | Optimisation |
|Modèle physique | Physical model |

# Bibliographie commentée
Les drones sont utilisés depuis la Guerre Froide. Leur usage fût d’abord militaire, pour de la
reconnaissance et des opérations. Il s’élargit ensuite peu à peu à un usage civil (recherche,
divertissement). Aujourd’hui, le secteur de la livraison s’est emparé de cette technologie, en
espérant une utilisation massive d’ici quelques années.
C’est le cas de l’entreprise Wing, une filiale d’Alphabet qui réalise des livraisons par drone dans la
ville de Logan en Australie depuis 2012. Elle a réalisé plus de 100 000 livraisons, principalement de
denrées alimentaires, ce qui en fait une entreprise de référence dans le domaine . C’est également le
cas en France, avec l’entreprise DPD, une filiale de La Poste, qui réalise des livraisons régulières
par drone dans le Var. Cela permet au village de Mont-Saint-Marin, difficile d’accès de par la
géographie montagneuse de la zone, de bénéficier du service de livraison.

Cependant, l’usage en ville est tout aussi - voire plus - pertinent. En effet, les livraisons par
drone en ville permettraient non seulement de remplacer peu à peu les camions de transport, ce qui
réduirait grandement la pollution et l’engorgement des routes en ville, mais aussi d’effectuer des
livraisons plus rapides et économiques. Les drones partiraient d’un entrepôt centralisé pour une
ville, et déposeraient les colis dans des zones prévues à cet effet, par exemple des "lockers" 
personnels. L’ordre de livraison étant défini par le placement des colis sous le drone, il convient de
se demander dans quel ordre les disposer afin d’effectuer le trajet le moins coûteux
énergétiquement.
Néanmoins, la stricte réglementation des drones en ville pose divers problèmes, d’occupation de
l’espace aérien ou de respect de la vie privée par exemple. En effet, même s’il est possible pour une
entreprise d’obtenir une autorisation pour voler en ville sous certaines conditions, la circulation
au-dessus de propriétés privées reste controversée. C’est pourquoi nous restreindrons notre étude
au seul cas où le drone se déplace au-dessus de routes.
De plus, le principe d’optimalité de Bellman nous indique que le cycle Hamiltonien optimal est une
combinaison de chemins optimaux d’un sommet à l’autre, nous chercherons donc dans un
premier temps le chemin optimal associé à chaque couple de sommets à livrer en se basant sur un
algorithme type Dijkstra / A-star.
En outre, le calcul du coût énergétique d’un trajet nécessite de s’intéresser à la dimension physique
de l’étude, notamment l’impact du poids des colis sur le drone ainsi que celui (non négligeable) du
vent, afin d’être en mesure d’estimer le coût énergétique d’un trajet pour optimiser la rentabilité de
celui-ci.
Il est vrai que l’utilisation d’une telle technologie pourrait engendrer de nombreux inconvénients,
comme des nuisances sonores, des risques de chute et de collision, ainsi que des limitations
techniques comme le rayon d’action et le poids maximal de colis emportés. Cependant, dans le
cadre de notre étude, nous nous intéresserons uniquement à la recherche du chemin
énergétiquement optimal.

# Problématique retenue
Il s’agit de déterminer, pour un drone livrant un certain nombre de colis dans une ville, le trajet
impliquant une consommation énergétique minimale.

# Objectifs du TIPE
Après une étude sur les graphes afin de décomplexifier le problème, nous essaierons de transposer
une carte d’une ville en graphe sous python, puis en graphe complet orienté reliant tous les
sommets à livrer.
Nous étudierons ensuite les propriétés physiques du drone nécessaires au calcul de la consommation
du drone, afin de déterminer algorithmiquement le cycle hamiltonien optimal énergétiquement.
Enfin nous comparerons le modèle numérique à l’expérience, et nous proposerons des optimisations pour les algorithmes.

# Références bibliographiques (ETAPE 1)
- [1] Encyclopédie Universalis : Histoire Des Drones :
https://www.universalis.fr/encyclopedie/drones/2-histoire-desdrones/#:~:text=Les%20premiers%20drones%20op%C3%A9rationnels,op%C3%A9rationnelles%2C
%20a%20vu%20le%20jour
- [2] DPD : Entreprise de livraison française utilisant les drones :
https://www.dpd.com/fr/fr/expedier-des-colis/nos-services-innovants/livraison-drone/
- [3] Anthony A. Tarr, Julie-Anne Tarr, Maurice Thompson and Jeffrey Ellis : Drone Law and
Policy - Global Development, Risks, Regulation and Insurance : p.115-116
- [4] Alexandre Cassart : Droit des Drones - Belgique, France, Luxembourg : Partie II :
L’insertion des drones dans l’espace aérien
- [5] David Hodgkinson : Aviation laws and drones.Unmanned aircraft and the future of aviation.
: p.25-26
- [6] Richard Bellman : Dynamic Programming, Princeton, Princeton University Press, 1957
- [7] Edsger W. Dijkstra : A short introduction to the art of programming : p.67 à 73
- [8] Physique du drone : calculer-la-duree-de-vol-de-son-multicopter
- [9] American journal of physics : Etude des collisions de drones livreurs à New-York :
https://aapt.scitation.org/doi/10.1119/10.0005035
