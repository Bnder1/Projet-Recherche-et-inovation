# Projet-Recherche-et-inovation
SLAM - détection de point d'intérêt par traitement d'image


##Agile

>Scrum ne se considère pas comme une méthode mais comme un cadre méthodologique.
	
>Il se contente d’offrir un cadre de gestion de projet Agile (et c’est déjà beaucoup) : des rôles, un rythme itératif, des réunions précises et limitées dans le temps, des artefacts (product backlog, sprint backlog, graphique d’avancement) et des règles du jeu.


Scrum définit seulement 3 rôles :

- **Le Product Owner** qui porte la vision du produit à réaliser et travaille en interaction avec l’équipe de développement. Il s’agit généralement d’un expert du domaine métier du projet.

- **L’Equipe de Développement** qui est chargée de transformer les besoins exprimés par le Product Owner en fonctionnalités utilisables. Elle est pluridisciplinaire et peut donc encapsuler d’autres rôles tels que développeur, architecte logiciel, DBA, analyste fonctionnel, graphiste/ergonome, ingénieur système.

- **Le Scrum Master** qui doit maîtriser Scrum et s’assurer que ce dernier est correctement appliqué. Il a donc un rôle de coach à la fois auprès du Product Owner et auprès de l’équipe de développement. Il doit donc faire preuve de pédagogie. Il est également chargé de s’assurer que l’équipe de développement est pleinement productive. Généralement le candidat tout trouvé au rôle de Scrum Master est le chef de projet. Celui ci devra cependant renoncer au style de management « commander et contrôler » pour adopter un mode de management participatif.

- **Stackholders** font les Users stories

> Communication avant processus et dev. Faire des feedBack / visual management / découper / Infos


###Risques
- Metier -> On construit la bonne chose?
- Social -> on peut la construire?
- Technique -> ça fonctione?
- Cout / delais

###Roles

- Rémi : Scrum master
- Zac : Product owner
- Guillaume / Fabien : équipe de recherche

##Projet
- 1.3 : SLAM - détection de point d'intérêt par traitement d'image
Compétences principales travaillées: Vision par ordinateur, 

- Traitement d’image

- Matériel nécessaire: Smartphone OU PC + WebCam

## 1.3 : SLAM - détection de point d'intérêt par traitement d'image

>En vision par ordinateur et en traitement d'images, la détection de zones d'intérêt d'une image numérique (feature detection en anglais) consiste à mettre en évidence des zones de cette image jugées « intéressantes » pour l'analyse, c'est-à-dire présentant des propriétés locales remarquables. De telles zones peuvent apparaître, selon la méthode utilisée, sous la forme de points, de courbes continues, ou encore de régions connexes rectangulaires ou non et qui constituent le résultat de la détection.

Les algorithmes de détection de points d'intérêt se focalisent en général sur des points particuliers des contours, sélectionnés selon un critère précis.

Ainsi, les coins (corners) sont les points de l'image où le contour (de dimension 1) change brutalement de direction, comme aux quatre sommets d'un rectangle. Il s'agit de points particulièrement stables, et donc intéressants pour la répétabilité (voir plus haut). La méthode la plus répandue pour le détecter est probablement le détecteur de Harris (illustration ci-contre).

Comme celle de Harris, la plupart des autres techniques de détection de points d'intérêt sont fondées sur une analyse locale de l'image à l'ordre 2. Ce qui les différencie entre elles est l'opérateur de dérivation utilisé. Nous pouvons par exemple citer les méthodes fondées sur l'analyse des DoG (Difference of Gaussians), des LoG (Laplacian of Gaussian) ou des DoH (Difference of Hessians).

### Slam
La localisation et cartographie simultanées, connue en anglais sous le nom de SLAM (simultaneous localization and mapping) ou CML (concurrent mapping and localization), consiste, pour un robot ou véhicule autonome, à simultanément construire ou améliorer une carte de son environnement et de s’y localiser.

## Links

- [Wiki](https://fr.wikipedia.org/wiki/D%C3%A9tection_de_zones_d%27int%C3%A9r%C3%AAt#:~:text=En%20vision%20par%20ordinateur%20et,pr%C3%A9sentant%20des%20propri%C3%A9t%C3%A9s%20locales%20remarquables.)

- [Machine Learning - Classification automatique d'images](https://github.com/CEREMA/dtermed.ML_bati_non-bati)

- [Thèse on git Latex](https://github.com/blefaudeux/phd_thesis/tree/7f5ecfb382fb1d06e09aac2d3fbe48061a57039d/Chapter3)

- [Object detection with openCV](https://www.pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-opencv/)

- [Détection de mouvement](https://www.labri.fr/projet/AIV/analyseinterpretation.php)

- [Formules et Principes PDF](http://devernay.free.fr/cours/vision/pdf/c4.pdf)

- [SLAM](https://fr.wikipedia.org/wiki/Cartographie_et_localisation_simultan%C3%A9es)

- [SLAM monoculaire](https://www.ensta-bretagne.fr/jaulin/rapport_pfe_amine_ouadrhiri.pdf)