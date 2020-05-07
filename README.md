# Projet AI Avalam
### Name = Yilmaz, Mustafa Ali
### Matricule = 17292
Voici mon projet d'intelligence artificielle qui jouera pendant la comptétition entre camarade de classe.

## Inscription:
Pour s'inscrire il faudra taper, par exemple, 'py subscribe.py 9090' dans le terminal

## Le jeu:
J'ai crée une classe qui aura une fonction qui envoie le mouvement qui paraît le plus adapaté.
Pour chaque coup possible, je donne le score qu'il va donner si il est utilisé, et c'est par rapport à ce score que le mouvement sera décidé. Le score étant le score du jeu.
## Il y'a 3 possibilité de coup possible pour mon IA:
### 1. Si le coup produit un score positif pour la classe, il sera privilégié.
J'ai mis quatres listes dans laquelle j'ai séparé les bons coups selon les différents meilleurs scores possible.
### 2. Si le coup produit un score égal à l'ancien score, il sera mis en attente:
c'est-à-dire, la classe va d'abord regarder si il n'ya pas de coup privilégié puis ensuite jouer celle ci.
Pour ce cas ci, j'ai dû rajouter la fonction notgoodmove qui va regarder si àprès ce coup l'ennemi aurait la possibilité de prendre une tour, si oui il ne la jouerait pas, si non il va le rajouter à une nouvelle liste dans laquelle il va pouvoir piocher au hasard gràce à la module random. Pour pouvoir prédire 1 coup à l'avance, j'ai dû implémenter le module copy pour copier en profondeur la grille de jeu.
Si aucun coup n'est possible en ma faveur, il jouera le prochain coup complètement au hasard.

### 3. si le coup produit un score négatif pour la classe, il fera tout pour ne pas le jouer.
