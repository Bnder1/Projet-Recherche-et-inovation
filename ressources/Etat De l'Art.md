La détection de points d’intérêts (ou coins) est, au même titre que la détection de contours, une étape préliminaire à de nombreux processus de vision par
ordinateur. Les points d’intérêts, dans une image, correspondent à des doubles discontinuités de la fonction d’intensités. Celles-ci peuvent être provoquées, comme
pour les contours, par des discontinuités de la fonction de réflectance ou des discontinuités de profondeur. Ce sont par exemple : les coins, les jonctions en T ou
les points de fortes variations de texture.

le détecteur de Moravec (1980)
L’idée du détecteur de Moravec est de considérer le voisinage d’un pixel (une
fenêtre) et de déterminer les changements moyens de l’intensité dans le voisinage
considéré lorsque la fenêtre se déplace dans diverses directions.

Le détecteur de Harris (1988)
Le détecteur de Moravec fonctionne dans un contexte limité. Il souffre en effet de
nombreuses limitations. Harris et Stephen ont identifié certaines limitations et, en
les corrigeant, en ont déduit un détecteur de coins très populaire : le détecteur de
Harris

SLAM

Le but est de produire depuis des données visuelles, une description exploitable par un robot mobile, d’une scène dynamique : modélisation du monde statique, localisation du
robot dans ce monde, et comment les autres objets mobiles
s’y déplacent. Une approche combinant Segmentation par
Clustering et Classification permet de détecter d’une part
des points statiques pris en compte dans le SLAM visuel, et
d’autre part des groupes de points mobiles exploités pour
détecter et suivre les composantes dynamiques de la scène.
L’approche globale est évaluée sur des bases d’images acquises en milieu urbain.
