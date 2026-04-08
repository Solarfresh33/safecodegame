# SafeCodeGame

Un petit jeu web basé sur Flask où il faut deviner un code secret, et surtout comprendre pourquoi c'est si facile à casser.

## C'est quoi ce projet ?

L'idée est simple :
- Au lancement du serveur, un **code secret à 3 chiffres** (de 0 à 9 pour chaque chiffre) est généré aléatoirement
- Le joueur essaie de le deviner via une interface web
- Un script de brute-force est fourni pour montrer à quel point ce genre de code est vulnérable

Bref, c'est un projet pensé pour apprendre, pas pour nuire.

## Mise en route

### Prérequis

- Python 3.x
- pip

### Installation

1. Cloner le dépôt
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

### Lancer le jeu

On démarre le serveur Flask :
```bash
python app.py
```

Ensuite, direction le navigateur : http://127.0.0.1:5000

## La démo brute-force

Le script `bruteforce.py` teste bêtement les 1 000 combinaisons possibles (de 000 à 999) jusqu'à trouver la bonne. Rien de sorcier, et c'est justement ça le problème : un code à 3 chiffres, ça ne tient pas longtemps.

Pour le lancer (pendant que le serveur tourne) :
```bash
python bruteforce.py
```

## 📁 Structure du projet

```
safecodegame/
├── app.py           # L'appli Flask (serveur + logique du jeu)
├── bruteforce.py    # Le script d'attaque par force brute
├── requirements.txt # Les dépendances Python
├── templates/
│   ├── index.html   # Page principale du jeu
│   └── win.html     # Page de victoire
└── README.md
```

## À quoi ça sert, concrètement ?

Ce projet est là **uniquement pour apprendre**. Il permet de comprendre :
- Comment fonctionne une attaque par force brute dans la pratique
- Pourquoi un code numérique court, c'est vraiment pas suffisant pour protéger quoi que ce soit
- L'importance de mettre en place des mécanismes de défense comme le rate limiting ou le verrouillage de compte après plusieurs tentatives

## Licence

Projet open source, libre d'utilisation à des fins pédagogiques.

Imaginé, créé et développé par Maxime ISIDORE