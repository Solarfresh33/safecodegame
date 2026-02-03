# 🔐 Coffre-Fort Challenge - Application Pédagogique

## 📋 Description

Application web Flask simulant un coffre-fort sécurisé avec une combinaison à 4 chiffres. Conçue pour enseigner les boucles imbriquées et le concept de bruteforce aux étudiants.

## ✨ Fonctionnalités

- 🎲 Combinaison aléatoire générée à chaque session
- 🔒 Vérification obligatoire de la combinaison pour accéder au flag
- 🎨 Interface moderne et intuitive
- 📚 Page d'aide avec exemple de code bruteforce
- 🏆 Flag : `YNOV{Bravo!tuasgagné}`

## 🚀 Installation

### Prérequis
- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner ou télécharger le projet**

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

Ou directement :
```bash
pip install Flask
```

3. **Lancer l'application**
```bash
python app.py
```

4. **Accéder à l'application**
Ouvrez votre navigateur et allez sur : http://localhost:5000

## 🎯 Objectifs Pédagogiques

Cette application permet d'apprendre :

1. **Les boucles imbriquées** : Comprendre comment 4 boucles for peuvent explorer toutes les combinaisons
2. **Les requêtes HTTP** : Envoyer des données via POST
3. **Le bruteforce** : Technique de test exhaustif (10 000 combinaisons possibles)
4. **La sécurité web** : Importance des bonnes pratiques de sécurité

## 📖 Utilisation pour les Étudiants

### Option 1 : Interface Manuelle
- Tester manuellement des combinaisons via l'interface web
- Observer les messages d'erreur

### Option 2 : Script Bruteforce
- Consulter la page `/bruteforce` pour voir un exemple de code
- Écrire un script Python avec 4 boucles imbriquées
- Utiliser la bibliothèque `requests` pour automatiser les tests

### Exemple de Script Bruteforce

```python
import requests

url = "http://localhost:5000/verifier"

for chiffre1 in range(10):
    for chiffre2 in range(10):
        for chiffre3 in range(10):
            for chiffre4 in range(10):
                data = {
                    'chiffre1': chiffre1,
                    'chiffre2': chiffre2,
                    'chiffre3': chiffre3,
                    'chiffre4': chiffre4
                }
                
                response = requests.post(url, data=data, allow_redirects=True)
                
                if "/win" in response.url:
                    print(f"✅ Trouvé : {chiffre1}-{chiffre2}-{chiffre3}-{chiffre4}")
                    print("Flag : YNOV{Bravo!tuasgagné}")
                    exit()
```

## 🔧 Structure du Projet

```
coffre-fort-challenge/
│
├── app.py                  # Application Flask principale
├── requirements.txt        # Dépendances Python
├── README.md              # Ce fichier
│
└── templates/
    ├── index.html         # Page d'accueil avec le coffre
    ├── win.html           # Page de victoire avec le flag
    └── bruteforce.html    # Page d'aide et guide
```

## 🎨 Captures d'Écran

### Page d'Accueil
Interface avec 4 champs pour entrer la combinaison

### Page de Victoire
Affiche le flag et la combinaison trouvée

### Page Guide
Explications et exemple de code bruteforce

## 🔒 Sécurité

⚠️ **Important** : Cette application est conçue à des fins pédagogiques uniquement. Dans un environnement de production réel :

- Implémenter un rate limiting (limitation du nombre de tentatives)
- Ajouter des délais entre les tentatives
- Logger les tentatives suspectes
- Utiliser des combinaisons plus complexes
- Ajouter une authentification

## 📝 Notes pour les Enseignants

- La combinaison change à chaque rechargement de page
- Le flag est toujours le même : `YNOV{Bravo!tuasgagné}`
- L'application utilise des sessions Flask pour stocker la combinaison
- Environ 10 000 combinaisons possibles (0000 à 9999)

## 🤝 Contribution

N'hésitez pas à améliorer ce projet :
- Ajouter des niveaux de difficulté
- Implémenter un système de score
- Ajouter des animations supplémentaires
- Créer des défis bonus

## 📄 Licence

Ce projet est libre d'utilisation à des fins pédagogiques.

## 🎓 YNOV

Projet créé pour l'enseignement de la programmation et de la cybersécurité.

---

**Bon apprentissage ! 🚀**
