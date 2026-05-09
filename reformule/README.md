# reformule

`reformule` est un petit outil en ligne de commande qui lit un texte depuis un fichier, envoie une consigne de reformulation a l'API Ollama, puis affiche ou enregistre le resultat.

Le script permet de choisir un ton de sortie et d'ajouter un contexte complementaire pour guider la reformulation.

## Fonctionnalites

- lecture du texte source depuis un fichier
- choix du ton de reformulation
- ajout d'un fichier de contexte optionnel
- affichage du resultat dans le terminal ou ecriture dans un fichier
- gestion simple des erreurs de lecture, d'ecriture et d'appel HTTP

## Structure du dossier

- `reformule_cli.py` : point d'entree principal
- `args.py` : definition des arguments de ligne de commande
- `ia.py` : appel HTTP a l'API Ollama
- `get_token.py` : recuperation de la variable d'environnement `OLLAMA_API_KEY`

## Prerequis

- Python 3
- le paquet Python `requests`
- une cle API exportee dans la variable d'environnement `OLLAMA_API_KEY`

## Installation

Depuis la racine du projet, installez la dependance necessaire :

```bash
pip install requests
```

Puis exportez votre cle API :

```bash
export OLLAMA_API_KEY="votre_cle_api"
```

## Utilisation

Depuis la racine du depot :

```bash
python reformule/reformule_cli.py -i mon_texte.txt
```

Le resultat est affiche dans la console si aucun fichier de sortie n'est fourni.

## Options disponibles

```bash
python reformule/reformule_cli.py \
  -i entree.txt \
  -t professionnel \
  -c contexte.txt \
  -o sortie.txt
```

Arguments :

- `-i`, `--input` : fichier texte a reformuler
- `-t`, `--tone` : ton de reformulation
- `-o`, `--output` : fichier de sortie optionnel
- `-c`, `--context` : fichier de contexte optionnel

Tons acceptes actuellement :

- `simple`
- `humoristique`
- `commercial`
- `professionnel`
- `amical`
- `formel`
- `informel`
- `redacteur_web_seo`

## Exemples

Reformuler un texte avec le ton par defaut :

```bash
python reformule/reformule_cli.py -i brouillon.txt
```

Reformuler un texte avec un ton commercial et enregistrer le resultat :

```bash
python reformule/reformule_cli.py -i brouillon.txt -t commercial -o version_commerciale.txt
```

Reformuler un texte avec des instructions supplementaires :

```bash
python reformule/reformule_cli.py -i brouillon.txt -c consignes.txt -t redacteur_web_seo
```

## Fonctionnement

Le programme construit un message systeme de la forme :

```text
Reformule le texte suivant en utilisant un ton <ton> :
```

Si un fichier de contexte est fourni, son contenu est ajoute a cette consigne.

Le texte a reformuler est ensuite envoye a l'endpoint `https://ollama.com/api/chat` avec le modele actuellement fixe a `gpt-oss:20b`.

## Gestion des erreurs

Le script signale notamment :

- un fichier d'entree introuvable
- un chemin qui pointe vers un dossier au lieu d'un fichier
- un probleme de droits en lecture ou ecriture
- l'absence de la variable `OLLAMA_API_KEY`
- une erreur HTTP, un timeout ou une erreur reseau lors de l'appel a l'API

## Limites actuelles

- le modele utilise est code en dur dans `ia.py`
- l'URL de l'API est egalement codee en dur
- il n'y a pas encore de tests automatises
- il n'y a pas de fichier `requirements.txt` pour installer les dependances automatiquement

## Pistes d'amelioration

- rendre le modele configurable en ligne de commande
- ajouter un mode lecture depuis l'entree standard
- ajouter des tests unitaires
- fournir un packaging propre avec un point d'entree installable