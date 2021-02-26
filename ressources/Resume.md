# Lecture des ressources


## Guillaume
- URL : https://hal.archives-ouvertes.fr/hal-00656550/document

>Resume :

## Rémi
- URL : https://hal.archives-ouvertes.fr/hal-00989067/
		https://www.irit.fr/~Sylvie.Chambon/PUBLICATIONS/GalesRapportMaster2007.pdf

>Resume :

## Fabien
- URL : 1. http://eprints.lincoln.ac.uk/id/eprint/9566/1/mozos2008lncs_caepia.pdf
		2. http://eprints.lincoln.ac.uk/id/eprint/9330/1/gil2009mva.pdf

>Resume :
>
>The first document reports the comparison of several points of interest detection algorithms (Harris Corner Detector, Harris-Laplace, SIFT, SURF, SUSAN). The document conclude that each of this algorithms are equivalent but the **Harris Corner Detector** algorithm keep a higher numbers of point of interest between frames unlike others.
>
>The second document reports the comparison of several points of interest detection algorithms in order to use them in a SLAM.

## Zac

- URL1 : https://hal.archives-ouvertes.fr/hal-00656572/document
- URL2 :https://hal.archives-ouvertes.fr/tel-01713128

>Resume1 :Cet article présente un système conçu pour traiter ensemble du SLAM, et de la Détection et du Suivi d’objets
mobiles (DATMO), en exploitant uniquement la vision. Le
but est de produire depuis des données visuelles, une description exploitable par un robot mobile, d’une scène dynamique : modélisation du monde statique, localisation du
robot dans ce monde, et comment les autres objets mobiles
s’y déplacent. Une approche combinant Segmentation par
Clustering et Classification permet de détecter d’une part
des points statiques pris en compte dans le SLAM visuel, et
d’autre part des groupes de points mobiles exploités pour
détecter et suivre les composantes dynamiques de la scène.
L’approche globale est évaluée sur des bases d’images acquises en milieu urbain.


>Resume2 :En raison de la demande croissante des systemes d’analyse video, la reconnaissance ainsi
que la detection de l’action humaine sont ciblees par les chercheurs. L’objectif etant de
realiser une description precise et rapide de la video, essentielement dans les grandes bases
de donnees. Ainsi, le but ultime de la reconnaissance de l’action humaine sur les videos
est de determiner de maniere automatique ce qui se passe dans une video donnee.
Cette these vise a repondre a cette question en apportant une contribution dans la phase
de detection et la phase de reconnaissance d’actions. Dans cet esprit, nous introduisons de
nouvelles methodes de description de reconnaissance de l’action humaine.
Pour la partie detection des actions, nous avons introduit deux approches basees sur
les points d’interets locaux. La premiere proposition est une methode simple et efficace qui
vise a detecter les mouvements humains ensuite contribuer a extraire des sequences video
decrivant des actions importantes. Afin d’atteindre cet objectif, les premieres sequences
video sont segmentees en volumes de trames et groupes de points d'interet . Dans cette
methode, nous nous basons sur le suivi du mouvement des points d’interet. Nous avons
utilise, dans un premier lieu, des videos simples puis nous avons progressivement augmente
la complexite des videos en optant pour des videos realistes.
Les jeux de donnees simples presentent generalement un arriere-plan statique avec un
seul acteur qui effectue une seule action unique ou bien la mˆeme action mais d’une maniere
repetitive. Nous avons ensuite teste la robustesse de la detection d’action proposee dans
des jeux de donnees plus complexes realistes recueillis a partir des reseaux sociaux.
Nous avons introduit une approche de detection d’actions efficace pour resoudre le
probleme de la reconnaissance d’actions humaines dans les videos realistes contenant des
mouvements de camera et n’etant pas de bonne qualite. Le mouvement humain est donc
segmente d’une manire spatio-temporelle afin de detecter le nombre optimal de trames
suffisant pour effectuer une description video.
Pour ce qui est du volet de la description, nous avons propose dans cette these deux
nouveaux descripteurs spatio-temporels. Ces descripteurs sont bases sur le suivi de la
trajectoire des points d’interet. Les suivis et la description video sont effectues sur les
patchs video qui contiennent un mouvement ou une partie d’un mouvement detecte par la
segmentation realisee lors de l’etape precedante. Nous nous sommes base sur le descripteur
SURF non seulement pour son efficacite et mais essentiellement pour la rapidite de son
extraction. Le premier descripteur propose est appel ST-SURF, il est base sur une nouvelle
combinaison du (SURF) et du flot optique. Le ST-SURF permet le suivi de la trajectoire
des points d’interet tout en gardant les informations spatiales, pertinentes, provenant du
SURF.
Le deuxieme descripteur propose dans le cadre de cette these est un histogramme du
mouvement de la trajectoire (HMTO). HMTO est base sur la position ainsi que l’echelle
relative a un SURF. Ainsi, pour chaque SURF detecte, nous definissons une region du
voisinage du point d’interˆet en nous basant sur l’echelle. Pour le patch detecte, nous
extrayons le flux otique d’une maniere dense. Les trajectoires de mouvement sont ensuite
generees pour chaque pixel en exploitant les composantes horizontale et verticale de flux
optique (u, v). La precision de la description de la video proposee est testee sur un ensemble
de donnees complexe et un plus grand ensemble de donnees realistes. Les descripteurs
de video proposes sont testes d’une maniere simple puis en les fusionnants avec d’autres
descripteurs. Les descripteurs video ont ete introduit dans un processus de classification
basee sur le sac de mots et ont demontre une amelioration des taux de reconnaissance par
rapport aux approches precedemment proposees dans l’etat-de-l’art.
