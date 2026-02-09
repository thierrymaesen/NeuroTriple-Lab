# 🧠 NeuroTriple-Lab

> **Laboratoire Pédagogique de Réseaux de Neurones**
> Démontrer que plus on entraîne une IA, plus elle est précise dans ses réponses.

---

## 📋 Description

**NeuroTriple-Lab** est un projet éducatif interactif qui utilise un réseau de neurones simple pour apprendre la fonction mathématique `f(x) = 3x` (tripler un nombre).

Le but principal est de **démontrer de manière visuelle et mesurable** que :

- ✅ **Plus on augmente le nombre d'epochs** (itérations d'entraînement), plus le modèle est précis
- ✅ **Plus on ajoute de couches intermédiaires** (profondeur du réseau), plus le modèle peut apprendre efficacement
- ✅ L'architecture et la durée d'entraînement sont des facteurs clés de la performance d'une IA

---

## 🎯 Concept de Base

Le code original est simple : un réseau de neurones reçoit des nombres en entrée et doit apprendre à prédire leur triple.

```python
# Données d'entraînement
entree = [1, 2, 3, 4, 5]     # Nombres en entrée
sortie = [3, 6, 9, 12, 15]   # Le triple (résultat attendu)
```

Le réseau n'a **aucune connaissance préalable** de la multiplication. Il apprend uniquement à partir des exemples fournis, en ajustant ses poids internes à chaque epoch.

---

## 🚀 5 Fonctionnalités Pédagogiques

### 1. 📊 Comparaison du Nombre d'Epochs
Entraîne le même modèle avec différents nombres d'epochs (ex: 10, 50, 100, 500, 1000, 3000) et compare la précision obtenue. Génère un graphique montrant la courbe de loss et l'erreur finale.

**Ce que vous apprenez** : L'impact direct du nombre d'itérations sur la qualité de l'apprentissage.

### 2. 🏗️ Comparaison des Architectures
Teste différentes profondeurs de réseau :
- Simple : 1 couche, 8 neurones
- Moyenne : 1 couche, 64 neurones
- Profonde : 3 couches (128→64→32)
- Très profonde : 5 couches (256→128→64→32→16)

**Ce que vous apprenez** : Comment le nombre de couches et de neurones influence la capacité d'apprentissage.

### 3. 📈 Visualisation de l'Apprentissage
Affiche en détail la courbe d'apprentissage (loss) avec trois graphiques :
- Courbe de loss complète
- Courbe en échelle logarithmique
- Prédictions du modèle vs valeurs réelles

**Ce que vous apprenez** : Comment le modèle réduit progressivement son erreur au fil de l'entraînement.

### 4. 📋 Tableau de Précision Détaillé
Combine différents epochs ET architectures pour produire un tableau comparatif complet avec temps d'entraînement, erreur absolue et statut de qualité.

**Ce que vous apprenez** : La relation entre complexité du modèle, durée d'entraînement et précision finale.

### 5. 🔬 Mode Expérimentation Automatisée
Lance une batterie complète de tests (16 combinaisons) et produit un classement du meilleur au moins bon, avec un graphique récapitulatif.

**Ce que vous apprenez** : Comment trouver systématiquement la meilleure configuration pour un problème donné.

### 🎮 Mode Interactif (Bonus)
Après l'entraînement, entrez n'importe quel nombre et voyez la prédiction de l'IA en temps réel, avec l'erreur par rapport à la valeur exacte.

---

## 💻 Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/thierrymaesen/NeuroTriple-Lab.git

# 2. Accéder au dossier
cd NeuroTriple-Lab

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer le programme
python neurotriplelab.py
```

---

## 📖 Utilisation

Au lancement, un menu interactif s'affiche :

```
  MENU PRINCIPAL
  ----------------------------------------
  1. Comparer différents nombres d'Epochs
  2. Comparer différentes Architectures
  3. Visualiser l'Apprentissage
  4. Tableau de Précision Détaillé
  5. Mode Expérimentation Automatisée
  6. Mode Interactif (tester le modèle)
  0. Quitter
  ----------------------------------------
  Votre choix :
```

Choisissez une option en tapant le numéro correspondant. Chaque fonctionnalité vous guide pas à pas et vous permet de personnaliser les paramètres (nombre d'epochs, etc.).

---

## 📊 Exemples de Résultats

### Impact des Epochs sur la Précision

| Epochs | Erreur Moyenne | Qualité |
|--------|---------------|---------|
| 10     | ~150.0000     | Insuffisant |
| 50     | ~25.0000      | Moyen |
| 100    | ~8.0000       | Bon |
| 500    | ~0.5000       | Très bon |
| 1000   | ~0.0500       | Excellent |
| 3000   | ~0.0010       | Excellent |

> ⚡ **Conclusion** : Avec 10 epochs, l'IA se trompe énormément. Avec 3000 epochs, elle est quasi parfaite !

---

## 🧩 Comment ça marche ?

### Le Réseau de Neurones

```
Entrée (x) → [Couche 1: N neurones] → [Couche 2: N neurones] → ... → Sortie (3x)
```

1. **Entrée** : Un nombre (ex: 7)
2. **Couches cachées** : Traitent l'information avec des poids et des biais
3. **Sortie** : La prédiction du triple (ex: 21.0003)
4. **Loss** : L'erreur entre la prédiction et la réalité
5. **Optimisation** : L'algorithme Adam ajuste les poids pour réduire la loss
6. **Epochs** : Nombre de fois que le réseau voit toutes les données

### Pourquoi plus d'epochs = plus de précision ?

À chaque epoch, le réseau ajuste légèrement ses poids pour réduire l'erreur. C'est comme un élève qui s'améliore en pratiquant :
- **10 epochs** = L'élève a lu le cours une fois → résultats médiocres
- **1000 epochs** = L'élève a pratiqué intensivement → résultats excellents

---

## 📁 Structure du Projet

```
NeuroTriple-Lab/
├── neurotriplelab.py    # Script principal avec les 5 fonctionnalités
├── requirements.txt     # Dépendances Python
├── README.md            # Ce fichier
├── LICENSE              # Licence MIT
└── .gitignore           # Fichiers ignorés par Git
```

### Fichiers générés après exécution (graphiques)
```
├── comparaison_epochs.png           # Graphique fonctionnalité 1
├── comparaison_architectures.png    # Graphique fonctionnalité 2
├── visualisation_apprentissage.png  # Graphique fonctionnalité 3
└── experimentation_complete.png     # Graphique fonctionnalité 5
```

---

## 🔧 Dépendances

| Package | Version | Rôle |
|---------|---------|------|
| TensorFlow | ≥ 2.10.0 | Framework de deep learning (Keras) |
| NumPy | ≥ 1.21.0 | Calculs numériques |
| Matplotlib | ≥ 3.5.0 | Génération des graphiques |

> 💡 **Note** : Le programme fonctionne même sans matplotlib (les graphiques seront simplement désactivés).

---

## 🎓 Pour Aller Plus Loin

Voici des idées pour approfondir votre compréhension :

1. **Modifier les données** : Changez la fonction cible (ex: f(x) = 2x + 1 ou f(x) = x²)
2. **Ajouter du bruit** : Ajoutez des erreurs aléatoires dans les données d'entraînement
3. **Tester d'autres optimiseurs** : Remplacez adam par sgd ou rmsprop
4. **Varier le learning rate** : Modifiez la vitesse d'apprentissage
5. **Ajouter de la régularisation** : Testez le dropout ou la régularisation L2

---

## 📜 Licence

Ce projet est sous licence **MIT** - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser la branche
5. Ouvrir une Pull Request

---

<p align="center">
  <strong>🧠 Plus on entraîne, plus l'IA est précise ! 🎯</strong>
</p>
