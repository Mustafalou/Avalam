<h1> Projet AI Avalam</h1>
<h2> Name = Yilmaz, Mustafa Ali</h2>
<h2> Matricule = 17292</h2>
Voici mon projet d'intelligence artificielle qui jouera pendant la comptétition entre camarade de classe.

<h2> Inscription: </h2>
<p>Pour m'inscrire il faudra taper, par exemple, 'py subscribe.py 9090' dans le terminal</p>
<p>Pour inscrire la classe qui va avec, c'est la meme chose : 'py AI_Avalam.py 9090' dans le terminal</p>

<h2> Le jeu: </h2>
<p>J'ai crée une classe qui aura une fonction qui envoie le mouvement qui paraît le plus adapaté.</p>
<p>Pour chaque coup possible, je donne le score qu'il va donner si il est utilisé, et c'est par rapport à ce score que le mouvement sera décidé. Le score étant le score du jeu.</p>
<h2>Il y'a 3 possibilité de coup possible pour mon IA:</h2>
<h3> 1. Si le coup produit un score positif pour la classe, il sera privilégié.</h3>
<p>J'ai mis quatres listes dans lesquelles j'ai séparé les bons coups selon les différents meilleurs scores possible.</p>
<h3> 2. Si le coup produit un score égal à l'ancien score, il sera mis en attente:</h3>
<p>c'est-à-dire, la classe va d'abord regarder si il n'ya pas de coup privilégié puis ensuite jouer celle ci.</p>
<p>Pour ce cas ci, j'ai dû rajouter la fonction notgoodmove qui va regarder si àprès ce coup l'ennemi aurait la possibilité de prendre une tour, si oui il ne la jouerait pas, si non il va le rajouter à une nouvelle liste dans laquelle il va pouvoir piocher au hasard gràce à la module random. Pour pouvoir prédire 1 coup à l'avance, j'ai dû implémenter le module copy pour copier en profondeur la grille de jeu.</p>
<p>Si aucun coup n'est possible en ma faveur, il jouera le prochain coup complètement au hasard.</p>

<h3> 3. si le coup produit un score négatif pour la classe, il fera tout pour ne pas le jouer.</h3>
