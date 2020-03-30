# Guide d'utilisation de git

## Utilisation de base

### Principe

Git est un gestionnaire de version, c'est à dire un logiciel permettant de garder un historique de toutes les modifications faites à un ensemble de fichiers, et revenir quand on le souhaite à n'importe quelle état enregistré du projet.

L'ensemble des fichiers et l'historique de leurs modifications est appelé dépôt. Chaque développeur dispose d'une copie locale du dépôt, qu'il devra ensuite pousser sur un serveur (dans notre cas, Gitlab) qui servira de point de référence pour tous les collaborateurs de l'état courant du projet.

Lorsqu’on travaille avec git, on suit donc en général toujours les étapes suivantes :

1. Récupération des dernières modifications du dépôt distant (clone / pull)
2. Modification du code source, tests, etc..
3. Enregistrement des changements afin de les faire connaître localement à git (add / commit)
4. Partage des changements aux autres développeurs sur le dépôt distant (push)
5. Retour à l'étape 1 pour la prochaine modifications

### Récupération d'un dépôt distant (clone / pull)

Récupérer un projet sur son ordinateur quand on n'en a encore aucune version :

```bash
git clone https://gitlab.com/h4122/pld-agile.git
```

Une fois le projet cloné une fois, on récupère régulièrement les modifications apportées par les autres développeurs avec :

```bash
git pull
```

### Prise en compte des modifications locales par git (add / commit)

Le cycle de vie d'un fichier ce présente de la manière suivante :

![img](https://git-scm.com/figures/18333fig0201-tn.png)

Chaque fichier du dépôt peut avoir deux états : sous suivi de version (*tracked*) ou non suivi (*untracked*). 

Les fichiers *tracked* sont les fichiers qui appartenaient déjà au dernier  enregistrement, ils peuvent être inchangés (*unmodified*), modifiés (*modified*) ou indexés (*staged*). 

Tous les autres fichiers sont non suivis, autrement dit tout fichier de la copie locale du dépôt qui n'appartenait au dernier enregistrement et qui n'a pas été *staged*. Quand on clone un dépôt pour la première fois, tous les fichiers  seront *tracked* et *unmodified* car on vient tout juste de les enregistrer sans les avoir encore édités.

Au fur et à mesure que vous éditez des fichiers, git les considère  comme *modified*, il faudra *stage* ces fichiers modifiés et *commit* les fichiers *staged*. 

Afin de voir l'état des fichiers on peut utiliser :

```bash
git status
```

Et pour plus de détails sur les modifications :

```bash
git diff
git diff classe.java # les lignes ajoutées/supprimées sont précédées d'un +/-
```

On peut annuler les modifications faites à un fichier avec :

```bash
git checkout -- classe.java
```

Afin de *track* un fichier nouvellement crée, on utilise :

```bash
git add classe1.java classe2.java ...
git add . # pour tout ajouter, à bien faire à la racine du dépôt
```

Cette commande sert également à *stage* les fichiers.

A l'inverse, on peut *unstage* un fichier avec :

```bash
git reset HEAD classe.java
```

Ensuite, on commit avec :

```bash
git commit
git commit classe1.java classe2.java ...
```

Et pour les fichiers déjà *tracked*, les *stage* automatiquement lors du commit avec :

```bash
git commit -a
```

Lorsque la commande *commit* est lancée, l’éditeur par défaut (généralement nano ou vim) s’ouvre pour y écrire sa description. 

On peut choisir son éditeur de texte pour les commits (pour vim/nano), sinon passer directement par des extensions dans les IDE :

```bash
git config --global core.editor "vim"
git config --global core.editor "code --wait"
```

Voir le [guide de style](./git-style-guide.md) pour savoir avec quelle granularité commit et comment en rédiger une bonne description.

### Consulter l'historique des commits

On peut consulter l'historique des commits avec :

```bash
git log
```

On voit que chaque commit est associé à un identifiant hexadécimal unique, son `SHA`. Les logs se parcourent avec les flèches directionnelles ou page up/down, et se quittent avec la touche *Q*.

Quelques arguments intéressants à git log :

- -p pour avoir le détail des commits
- --stat pour avoir un résumé plus court des commits

### Annuler un commit non envoyé sur le répertoire distant

Pour effectuer des modifications légères sur le dernier commit (ajout de fichier, modification de description, etc..) on pourra utiliser :

```bash
git commit --amend
```

Pour annuler le dernier commit sans les modifications faites aux fichiers (*soft reset*) :

```bash
git reset HEAD^
```

Pour indiquer a quel commit on souhaite revenir il y a plusieurs notations :

- `HEAD` : dernier commit ;
- `HEAD^` : avant-dernier commit ;
- `HEAD^^` : avant-avant-dernier commit ;
- Le SHA du commit en question

Pour annuler le dernier commit avec les modifications faites aux fichiers (*hard reset*) :

```bash
git reset --hard HEAD^
```

Globalement, reset sert en fait à se positionner sur le commit passé que l'on veut.

Une autre solution est d'effectuer un nouveau commit apportant exactement inverses au dernier :

```bash
git revert
```

### Envoi des modifications sur le répertoire distant (push)

Un commit avec git est local : à moins d’envoyer ce commit sur le serveur, personne ne sait que vous avez fait ce commit pour le moment. Cela a un avantage : si vous vous rendez compte que vous avez fait une erreur dans votre dernier commit, vous avez la possibilité de l’annuler.

Il est toujours recommandé de vérifier ses logs locaux avant d'envoyer :

```bash
git log -p
```

Une fois que vous êtes sûrs, passez à l’envoi. Vous pouvez envoyer vos commits avec la commande :

```bash
git pull
git push
```

Il est recommandé de faire régulièrement des commits, mais pas forcément des push car il est bien plus facile de modifier un commit en local. En effet, il est impossible de modifier un commit une fois envoyé sur le serveur, la solution pour annuler un commit publié est de revert.

### Gérer les conflits

Il arrive que le répertoire local ne soit pas à jour avec le répertoire distant, par exemple si le répertoire distant à été modifié entre le dernier *pull* et *push*. Quand deux fichiers différents ont été édités, git s'arrange pour fusionner proprement le tout. Mais si deux développeurs ont éditer la même ligne d'un fichier : il y a conflit, c'est à dire que git ne peut décider automatiquement quelles modifications doivent être conservées.

Il indique alors le nom des fichiers en conflit, qu'on peut ouvrir avec l'éditeur de texte. La zone en conflit s'affiche entre symboles *>>>>>>>>>>>>>>>>>>>>* et *<<<<<<<<<<<<<<<<<<<<*, il suffit de supprimer les symboles et garder uniquement ce que l'on veut, enregistrer le fichier et commit à nouveau pour corriger le problème.

De nombreux outils permettent de visualiser facilement les changements apportés au fichier, et IntellJ le fait très bien.

## Branches

### Principe

Dans Git,  toutes les modifications que vous faites au fil du temps sont par défaut  considérées comme appartenant à la branche principale appelée  « master » :

![La branche principale master](https://user.oc-static.com/files/236001_237000/236930.png)

Supposons  que vous ayez une idée pour améliorer la gestion des erreurs dans votre  programme mais que vous ne soyez pas sûrs qu’elle va fonctionner : vous  voulez faire des tests, ça va vous prendre du temps, donc vous ne voulez  pas que votre projet incorpore ces changements dans l’immédiat.

Il  suffit de créer une branche, que vous nommerez par exemple  « idee_gestion_erreurs », dans laquelle vous allez pouvoir travailler *en parallèle* :

![Une branche secondaire](https://user.oc-static.com/files/236001_237000/236931.png)

Pour voir toutes les branches :

```bash
git branch
```

### Granularité des branches

Lorsque vous vous apprêtez à faire des modifications sur le code source, posez-vous les questions suivantes :

- « Ma modification sera-t-elle rapide ? » ;
- « Ma modification est-elle simple ? » ;
- « Ma modification nécessite-t-elle un seul commit ? » ;
- « Est-ce que je vois précisément comment faire ma modification d’un seul coup ? ».

Si  la réponse à l’une de ces questions est « non », vous devriez  probablement créer une branche. Créer une branche est très simple, très  rapide et très efficace. Il ne faut donc pas s’en priver.

**Créez une branche pour toute modification que vous vous apprêtez à faire et qui risque d’être un peu longue.**

Au  pire, si votre modification est plus courte que prévu, vous aurez créé  une branche « pour pas grand-chose », mais c’est toujours mieux que de  se rendre compte de l’inverse.

###  Mise en œuvre

Créer une branche :

```bash
git branch options_bonus
```

Pour passer de la branche *master* à *options_membres* :

```bash
git checkout options_bonus
```

Le code reste dans le même dossier, mais est remplacé par celui de la branche.

Fusionner les changements avec la branche principale :

```bash
git checkout master
git merge options_bonus
```

Supprimer une branche

```bash
git branch -d options_bonus
git branch -D options_bonus  /!\ Supprime la branche et perd tous les changements
```

Changer de branche sans avoir à faire de commit :

```bash
git stash 		# pour sauver le working directory de la branche
git stash apply # pour récupérer le tout
```

Récupérer une branche :

```bash
git branch --track branchelocale origin/brancheserveur
```

Partager une branche :

```bash
git branch -r # pour voir les branches que le serveur connaît
```

```bash
git push origin origin:refs/heads/nom_nouvelle_branche
```

Supprimer :

```bash
git push origin :heads/nom_branche_a_supprimer
```

## Autres fonctionnalités utiles

### Faire ignorer certains fichiers à git (.gitignore)

Pour ignorer un fichier dans git, créez un fichier *.gitignore* (à la racine) et indiquez-y le nom du fichier. Entrez un nom de fichier par ligne, comme ceci :

```
project.xml
dossier/temp.txt
*.tmp
cache/*
```

On ignorera en général :

- Les fichiers et dossiers temporaires
- Les fichiers inutiles comme ceux créés par son IDE ou OS
- De manière générale de pas laisser de fichier de config avec mot de passe ou information confidentielle

### Identifier qui a fait quelles modifications (blame)

```bash
git blame fichier
git show sha
```

Permet de savoir quel commit a affecté quelle partie du fichier.
