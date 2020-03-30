# Guide de style pour commits

## Granularité des commits

Un commit sert à valider l'avancement du projet, et non pas "sauvegarder ses changements en ligne". La granularité d'un commit correspond donc à l'ajout d'une fonctionnalité, la correction d'un bug, etc..

Un commit ne devrait pas être utilisé pour des fonctionnalités non terminés ("Work In Progress").

## Guide de style pour le message de commit



![https://imgs.xkcd.com/comics/git_commit.png](https://imgs.xkcd.com/comics/git_commit.png)



Un bon message de commit doit permettre de savoir ce qui a changé et  pourquoi. Le comment (la manière d’effectuer ces  changements) n’a pas à être expliqué.  La lecture du code (normalement bien documenté) et la mise en  évidence des changements via un `diff` est explicite en soi. 

L'objectif est vraiment que le commit soit compréhensible auprès de tous les développeurs, et ce même 2 semaines plus tard.

Voici un template que nous suivrons, tiré du projet open-source Angular :

```
<type>(<portée>): <Sujet>
<LIGNE VIDE>
<description>
<LIGNE VIDE>
<footer>
```

### Type

Le type sera utile pour identifier rapidement la partie du projet impactée par le commit, et permet de filtrer les commits par fonctionnalité.

- `feat` : ajout d’une nouvelle fonctionnalité
- `fix` : correction d’un bug
- `refactor` : modification qui n’apporte ni nouvelle fonctionnalité ni d’amélioration de performances
- `style` : changement qui n’apporte aucune altération fonctionnelle ni sémantique (autrement dit, indentation, mise en forme, ajout d’espace, renommage d’une variable…)
- `docs` : rédaction ou mise à jour de documentation
- `test` : ajout ou modification de tests
- `perf` : amélioration des performances
- `chore`: changement qui affectent le build, les dépendances externes, ou encore les fichiers de configuration, mais pas le code en lui même

À cela s’ajoute `revert`. Ce dernier permet comme son nom l’indique, d’annuler un précédent commit. Dans ce cas, le message prend la forme suivante :

```
revert Sujet du commit annulé 4e4a6f7c
```

### Portée

- Facultatif (pas toujours pertienent)
- Permet d' immédiatement savoir quelle partie du projet est affectée
- Les portées seront à définir à l'avance dans l'hexanome, mais on peut déjà imaginer *ihm*, *algo*, carte, etc...

### Sujet

- Description **succinte** des  changements.
- Se limite à 50 caractères.
- Pour adopter un style descriptif efficace, on utilise l’impératif présent : c'est à dire `Add ....` et non `Added ...` ou bien `Adds ...`  par exemple.
- Commence par une majuscule et ne termine pas par un point

### Description

- Facultatif
- Peut être une description de la fonctionnalité ajoutée, 
- De nouveau, on explique ici la raison du changement de code et en quoi c’est nouvelle manière est différente de l’état précédent
- Ne pas hésiter à mettre des liens vers des pages Stackoverflow pour des corrections de bugs etc... Tout ce qui serait agréable de retrouver deux semaines plus tard quand on ne sait plus de quoi parle le projet, mais ne pas aborder le COMMENT qui est déjà dans le code
- Pas plus de 70-80 caractères par ligne.
- Possibilité d'ajouter des "bullet-points" et du code Markdown

### Footer

	- Facultatif
	- On réserve le footer aux *breaking changes* et on y référence aussi le ticket d’erreur que règlent les modifications le cas échéant.

### Exemple

```
docs(global): Summarize changes in around 50 characters or less

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of the commit and the rest of the text as the body. The
blank line separating the summary from the body is critical (unless
you omit the body entirely); various tools like `log`, `shortlog`
and `rebase` can get confused if you run the two together.

Explain the problem that this commit is solving. Focus on why you
are making this change as opposed to how (the code explains that).
Are there side effects or other unintuitive consequences of this
change? Here's the place to explain them.

Further paragraphs come after blank lines.

 - Bullet points are okay, too

 - Typically a hyphen or asterisk is used for the bullet, preceded
   by a single space, with blank lines in between, but conventions
   vary here

If you use an issue tracker, put references to them at the bottom,
like this:

Resolves: #123
See also: #456, #789
```