<div align="center">

🇫🇷 [Version française](#french) | 🇬🇧 [English version](#english)

</div>

---

<a name="french"></a>

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
entree = [1, 2, 3, 4, 5]       # Nombres en entrée
sortie = [3, 6, 9, 12, 15]     # Le triple (résultat attendu)
```

Le réseau n'a **aucune connaissance préalable** de la multiplication. Il apprend uniquement à partir des exemples fournis, en ajustant ses poids internes à chaque epoch.

---

## 🚀 5 Fonctionnalités Pédagogiques

### 1. 📊 Comparaison du Nombre d'Epochs

Entraîne le même modèle avec différents nombres d'epochs (ex: 10, 50, 100, 500, 1000, 3000) et compare la précision obtenue.

**Ce que vous apprenez** : L'impact direct du nombre d'itérations sur la qualité de l'apprentissage.

### 2. 🏗️ Comparaison des Architectures

Teste différentes profondeurs de réseau :
- Simple : 1 couche, 8 neurones
- Moyenne : 1 couche, 64 neurones
- Profonde : 3 couches (128→64→32)
- Très profonde : 5 couches (256→128→64→32→16)

### 3. 📈 Visualisation de l'Apprentissage

Affiche en détail la courbe d'apprentissage (loss) avec trois graphiques.

### 4. 📋 Tableau de Précision Détaillé

Combine différents epochs ET architectures pour produire un tableau comparatif complet.

### 5. 🔬 Mode Expérimentation Automatisée

Lance une batterie complète de tests (16 combinaisons) et produit un classement du meilleur au moins bon.

### 🎮 Mode Interactif (Bonus)

Après l'entraînement, entrez n'importe quel nombre et voyez la prédiction de l'IA en temps réel.

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

## 📊 Exemples de Résultats

| Epochs | Erreur Moyenne | Qualité |
|--------|---------------|---------|
| 10     | ~150.0000     | Insuffisant |
| 50     | ~25.0000      | Moyen |
| 100    | ~8.0000       | Bon |
| 500    | ~0.5000       | Très bon |
| 1000   | ~0.0500       | Excellent |
| 3000   | ~0.0010       | Excellent |

---

## 📜 Licence

Ce projet est sous licence **MIT** - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🤝 Contribuer

Les contributions sont les bienvenues !

1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser la branche
5. Ouvrir une Pull Request

---

<p align="center">
  <strong>🧠 Plus on entraîne, plus l'IA est précise ! 🎯</strong>
</p>

---

<a name="english"></a>

# 🧠 NeuroTriple-Lab

> **Educational Neural Network Laboratory**
> Demonstrating that the more you train an AI, the more accurate it becomes.

---

## 📋 Description

**NeuroTriple-Lab** is an interactive educational project that uses a simple neural network to learn the mathematical function `f(x) = 3x` (tripling a number).

The main goal is to **visually and measurably demonstrate** that:

- ✅ **The more you increase the number of epochs** (training iterations), the more accurate the model becomes
- ✅ **The more intermediate layers you add** (network depth), the more efficiently the model can learn
- ✅ Architecture and training duration are key factors in AI performance

---

## 🎯 Core Concept

The original code is simple: a neural network receives numbers as input and must learn to predict their triple.

```python
# Training data
input_data = [1, 2, 3, 4, 5]        # Input numbers
output_data = [3, 6, 9, 12, 15]     # The triple (expected result)
```

The network has **no prior knowledge** of multiplication. It learns solely from the provided examples, adjusting its internal weights at each epoch.

---

## 🚀 5 Educational Features

### 1. 📊 Epoch Count Comparison

Trains the same model with different numbers of epochs (e.g., 10, 50, 100, 500, 1000, 3000) and compares the accuracy achieved.

**What you learn**: The direct impact of iteration count on learning quality.

### 2. 🏗️ Architecture Comparison

Tests different network depths:
- Simple: 1 layer, 8 neurons
- Medium: 1 layer, 64 neurons
- Deep: 3 layers (128→64→32)
- Very deep: 5 layers (256→128→64→32→16)

### 3. 📈 Learning Visualization

Displays the learning curve (loss) in detail with three graphs.

### 4. 📋 Detailed Accuracy Table

Combines different epochs AND architectures to produce a complete comparative table.

### 5. 🔬 Automated Experimentation Mode

Launches a complete battery of tests (16 combinations) and produces a ranking from best to worst.

### 🎮 Interactive Mode (Bonus)

After training, enter any number and see the AI prediction in real time.

---

## 💻 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/thierrymaesen/NeuroTriple-Lab.git

# 2. Navigate to the folder
cd NeuroTriple-Lab

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the program
python neurotriplelab.py
```

---

## 📊 Example Results

| Epochs | Average Error | Quality |
|--------|--------------|---------|
| 10     | ~150.0000    | Insufficient |
| 50     | ~25.0000     | Average |
| 100    | ~8.0000      | Good |
| 500    | ~0.5000      | Very Good |
| 1000   | ~0.0500      | Excellent |
| 3000   | ~0.0010      | Excellent |

---

## 📜 License

This project is licensed under the **MIT** License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome!

1. Fork the project
2. Create a branch for your feature
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

<p align="center">
  <strong>🧠 The more you train, the more accurate the AI becomes! 🎯</strong>
</p><div align="center">

🇫🇷 [Version française](#french) | 🇬🇧 [English version](#english)

</div>

---

<a name="french"></a>

# 🧠 NeuroTriple-Lab

> **Laboratoire Pédagogique de Réseaux de Neurones**
> > Démontrer que plus on entraîne une IA, plus elle est précise dans ses réponses.
> >
> > ---
> >
> > ## 📋 Description
> >
> > **NeuroTriple-Lab** est un projet éducatif interactif qui utilise un réseau de neurones simple pour apprendre la fonction mathématique `f(x) = 3x` (tripler un nombre).
> >
> > Le but principal est de **démontrer de manière visuelle et mesurable** que :
> >
> > - ✅ **Plus on augmente le nombre d'epochs** (itérations d'entraînement), plus le modèle est précis
> > - - ✅ **Plus on ajoute de couches intermédiaires** (profondeur du réseau), plus le modèle peut apprendre efficacement
> >   - - ✅ L'architecture et la durée d'entraînement sont des facteurs clés de la performance d'une IA
> >    
> >     - ---
> >
> > ## 🎯 Concept de Base
> >
> > Le code original est simple : un réseau de neurones reçoit des nombres en entrée et doit apprendre à prédire leur triple.
> >
> > ```python
> > # Données d'entraînement
> > entree = [1, 2, 3, 4, 5]       # Nombres en entrée
> > sortie = [3, 6, 9, 12, 15]     # Le triple (résultat attendu)
> > ```
> >
> > Le réseau n'a **aucune connaissance préalable** de la multiplication. Il apprend uniquement à partir des exemples fournis, en ajustant ses poids internes à chaque epoch.
> >
> > ---
> >
> > ## 🚀 5 Fonctionnalités Pédagogiques
> >
> > ### 1. 📊 Comparaison du Nombre d'Epochs
> >
> > Entraîne le même modèle avec différents nombres d'epochs (ex: 10, 50, 100, 500, 1000, 3000) et compare la précision obtenue. Génère un graphique montrant la courbe de loss et l'erreur finale.
> >
> > **Ce que vous apprenez** : L'impact direct du nombre d'itérations sur la qualité de l'apprentissage.
> >
> > ### 2. 🏗️ Comparaison des Architectures
> >
> > Teste différentes profondeurs de réseau :
> > - Simple : 1 couche, 8 neurones
> > - - Moyenne : 1 couche, 64 neurones
> >   - - Profonde : 3 couches (128→64→32)
> >     - - Très profonde : 5 couches (256→128→64→32→16)
> >      
> >       - **Ce que vous apprenez** : Comment le nombre de couches et de neurones influence la capacité d'apprentissage.
> >      
> >       - ### 3. 📈 Visualisation de l'Apprentissage
> >      
> >       - Affiche en détail la courbe d'apprentissage (loss) avec trois graphiques :
> > - Courbe de loss complète
> > - - Courbe en échelle logarithmique
> >   - - Prédictions du modèle vs valeurs réelles
> >    
> >     - **Ce que vous apprenez** : Comment le modèle réduit progressivement son erreur au fil de l'entraînement.
> >    
> >     - ### 4. 📋 Tableau de Précision Détaillé
> >    
> >     - Combine différents epochs ET architectures pour produire un tableau comparatif complet avec temps d'entraînement, erreur absolue et statut de qualité.
> > 
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
- - pip (gestionnaire de paquets Python)
 
  - ### Étapes
 
  - ```bash
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

    > ⚠️ **ATTENTION — Performance et temps de calcul**
    > >
    > >> Le Deep Learning (apprentissage profond) est **très gourmand en ressources**. Si vous utilisez un ordinateur peu puissant (ancien PC, machine sans GPU), soyez prudent avec les paramètres suivants :
    > >> >
    > >> >> - **Nombre d'epochs** : Au-delà de **5000 epochs**, le temps de calcul peut devenir très long. Commencez avec des valeurs modestes (500-1000) et augmentez progressivement.
    > >> >> - > - **Couches denses (Dense layers)** : Plus vous ajoutez de couches et de neurones (ex: `[256, 128, 64, 32, 16]`), plus chaque epoch prend du temps.
    > >> >>   > - > - **Combinaison des deux** : 5000 epochs × 5 couches denses = temps de calcul potentiellement **très élevé** !
    > >> >>   >   > - >
    > >> >>   >   >   >> 💡 **Conseil** : Commencez petit (ex: 500 epochs, 1 couche de 64 neurones), observez les résultats, puis augmentez graduellement.
    > >> >>   >   >   >>
    > >> >>   >   >   >> ---
    > >> >>   >   >   >>
    > >> >>   >   >   >> ## 📖 Utilisation
    > >> >>   >   >   >>
    > >> >>   >   >   >> Au lancement, un menu interactif s'affiche :
    > >> >>   >   >   >>
    > >> >>   >   >   >> ```
    > >> >>   >   >   >> MENU PRINCIPAL
    > >> >>   >   >   >> ----------------------------------------
    > >> >>   >   >   >> 1. Comparer différents nombres d'Epochs
    > >> >>   >   >   >> 2. Comparer différentes Architectures
    > >> >>   >   >   >> 3. Visualiser l'Apprentissage
    > >> >>   >   >   >> 4. Tableau de Précision Détaillé
    > >> >>   >   >   >> 5. Mode Expérimentation Automatisée
    > >> >>   >   >   >> 6. Mode Interactif (tester le modèle)
    > >> >>   >   >   >> 0. Quitter
    > >> >>   >   >   >> ----------------------------------------
    > >> >>   >   >   >> Votre choix :
    > >> >>   >   >   >> ```
    > >> >>   >   >   >>
    > >> >>   >   >   >> ---
    > >> >>   >   >   >>
    > >> >>   >   >   >> ## 📊 Exemples de Résultats
    > >> >>   >   >   >>
    > >> >>   >   >   >> ### Impact des Epochs sur la Précision
    > >> >>   >   >   >>
    > >> >>   >   >   >> | Epochs | Erreur Moyenne | Qualité |
    > >> >>   >   >   >> |--------|---------------|---------|
    > >> >>   >   >   >> | 10     | ~150.0000     | Insuffisant |
    > >> >>   >   >   >> | 50     | ~25.0000      | Moyen |
    > >> >>   >   >   >> | 100    | ~8.0000       | Bon |
    > >> >>   >   >   >> | 500    | ~0.5000       | Très bon |
    > >> >>   >   >   >> | 1000   | ~0.0500       | Excellent |
    > >> >>   >   >   >> | 3000   | ~0.0010       | Excellent |
    > >> >>   >   >   >>
    > >> >>   >   >   >> > ⚡ **Conclusion** : Avec 10 epochs, l'IA se trompe énormément. Avec 3000 epochs, elle est quasi parfaite !
    > >> >>   >   >   >> >
    > >> >>   >   >   >> > ---
    > >> >>   >   >   >> >
    > >> >>   >   >   >> > ## 🧩 Comment ça marche ?
    > >> >>   >   >   >> >
    > >> >>   >   >   >> > ### Le Réseau de Neurones
    > >> >>   >   >   >> >
    > >> >>   >   >   >> > ```
    > >> >>   >   >   >> > Entrée (x) → [Couche 1: N neurones] → [Couche 2: N neurones] → ... → Sortie (3x)
    > >> >>   >   >   >> > ```
    > >> >>   >   >   >> >
    > >> >>   >   >   >> > 1. **Entrée** : Un nombre (ex: 7)
    > >> >>   >   >   >> > 2. 2. **Couches cachées** : Traitent l'information avec des poids et des biais
    > >> >>   >   >   >> >    3. 3. **Sortie** : La prédiction du triple (ex: 21.0003)
    > >> >>   >   >   >> >       4. 4. **Loss** : L'erreur entre la prédiction et la réalité
    > >> >>   >   >   >> >          5. 5. **Optimisation** : L'algorithme Adam ajuste les poids pour réduire la loss
    6. **Epochs** : Nombre de fois que le réseau voit toutes les données
   
    7. ### Pourquoi plus d'epochs = plus de précision ?
   
    8. À chaque epoch, le réseau ajuste légèrement ses poids pour réduire l'erreur. C'est comme un élève qui s'améliore en pratiquant :
    9. - **10 epochs** = L'élève a lu le cours une fois → résultats médiocres
       - - **1000 epochs** = L'élève a pratiqué intensivement → résultats excellents
        
         - ---

         ## 📁 Structure du Projet

         ```
         NeuroTriple-Lab/
         ├── neurotriplelab.py       # Script principal avec les 5 fonctionnalités
         ├── requirements.txt        # Dépendances Python
         ├── README.md               # Ce fichier
         ├── LICENSE                 # Licence MIT
         └── .gitignore              # Fichiers ignorés par Git
         ```

         ---

         ## 🔧 Dépendances

         | Package | Version | Rôle |
         |---------|---------|------|
         | TensorFlow | ≥ 2.10.0 | Framework de deep learning (Keras) |
         | NumPy | ≥ 1.21.0 | Calculs numériques |
         | Matplotlib | ≥ 3.5.0 | Génération des graphiques |

         ---

         ## 📜 Licence

         Ce projet est sous licence **MIT** - voir le fichier [LICENSE](LICENSE) pour plus de détails.

         ---

         ## 🤝 Contribuer

         Les contributions sont les bienvenues ! N'hésitez pas à :
         1. Fork le projet
         2. 2. Créer une branche pour votre fonctionnalité
            3. 3. Commiter vos changements
               4. 4. Pousser la branche
                  5. 5. Ouvrir une Pull Request
                    
                     6. ---
                    
                     7. <p align="center">
                       <strong>🧠 Plus on entraîne, plus l'IA est précise ! 🎯</strong>
                       </p>

                       ---

                     <a name="english"></a>

                     # 🧠 NeuroTriple-Lab

                     > **Educational Neural Network Laboratory**
                     > > Demonstrating that the more you train an AI, the more accurate it becomes.
                     > >
                     > > ---
                     > >
                     > > ## 📋 Description
                     > >
                     > > **NeuroTriple-Lab** is an interactive educational project that uses a simple neural network to learn the mathematical function `f(x) = 3x` (tripling a number).
                     > >
                     > > The main goal is to **visually and measurably demonstrate** that:
                     > >
                     > > - ✅ **The more you increase the number of epochs** (training iterations), the more accurate the model becomes
                     > > - - ✅ **The more intermediate layers you add** (network depth), the more efficiently the model can learn
                     > >   - - ✅ Architecture and training duration are key factors in AI performance
                     > >    
                     > >     - ---
                     > >
                     > > ## 🎯 Core Concept
                     > >
                     > > The original code is simple: a neural network receives numbers as input and must learn to predict their triple.
                     > >
                     > > ```python
                     > > # Training data
                     > > input_data = [1, 2, 3, 4, 5]        # Input numbers
                     > > output_data = [3, 6, 9, 12, 15]     # The triple (expected result)
                     > > ```
                     > >
                     > > The network has **no prior knowledge** of multiplication. It learns solely from the provided examples, adjusting its internal weights at each epoch.
                     > >
                     > > ---
                     > >
                     > > ## 🚀 5 Educational Features
                     > >
                     > > ### 1. 📊 Epoch Count Comparison
                     > >
                     > > Trains the same model with different numbers of epochs (e.g., 10, 50, 100, 500, 1000, 3000) and compares the accuracy achieved. Generates a graph showing the loss curve and final error.
                     > >
                     > > **What you learn**: The direct impact of iteration count on learning quality.
                     > >
                     > > ### 2. 🏗️ Architecture Comparison
                     > >
                     > > Tests different network depths:
                     > > - Simple: 1 layer, 8 neurons
                     > > - - Medium: 1 layer, 64 neurons
                     > >   - - Deep: 3 layers (128→64→32)
                     > >     - - Very deep: 5 layers (256→128→64→32→16)
                     > >      
                     > >       - **What you learn**: How the number of layers and neurons influences learning capacity.
                     > >      
                     > >       - ### 3. 📈 Learning Visualization
                     > >      
                     > >       - Displays the learning curve (loss) in detail with three graphs:
                     > > - Complete loss curve
                     > > - - Logarithmic scale curve
                     > >   - - Model predictions vs actual values
                     > >    
                     > >     - **What you learn**: How the model progressively reduces its error during training.
                     > >    
                     > >     - ### 4. 📋 Detailed Accuracy Table
                     > >    
                     > >     - Combines different epochs AND architectures to produce a complete comparative table with training time, absolute error, and quality status.
                     > > 
                     **What you learn**: The relationship between model complexity, training duration, and final accuracy.

                     ### 5. 🔬 Automated Experimentation Mode

                     Launches a complete battery of tests (16 combinations) and produces a ranking from best to worst, with a summary graph.

                     **What you learn**: How to systematically find the best configuration for a given problem.

                     ### 🎮 Interactive Mode (Bonus)

                     After training, enter any number and see the AI prediction in real time, with the error compared to the exact value.

                     ---

                     ## 💻 Installation

                     ### Prerequisites

                     - Python 3.8 or higher
                     - - pip (Python package manager)
                      
                       - ### Steps
                      
                       - ```bash
                         # 1. Clone the repository
                         git clone https://github.com/thierrymaesen/NeuroTriple-Lab.git

                         # 2. Navigate to the folder
                         cd NeuroTriple-Lab

                         # 3. Install dependencies
                         pip install -r requirements.txt

                         # 4. Run the program
                         python neurotriplelab.py
                         ```

                         ---

                         > ⚠️ **WARNING — Performance and computation time**
                         > >
                         > >> Deep Learning is **very resource-intensive**. If you're using a low-powered computer (old PC, machine without GPU), be careful with the following parameters:
                         > >> >
                         > >> >> - **Number of epochs**: Beyond **5000 epochs**, computation time can become very long. Start with modest values (500-1000) and increase gradually.
                         > >> >> - > - **Dense layers**: The more layers and neurons you add (e.g., `[256, 128, 64, 32, 16]`), the longer each epoch takes.
                         > >> >>   > - > - **Combination of both**: 5000 epochs × 5 dense layers = potentially **very high** computation time!
                         > >> >>   >   > - >
                         > >> >>   >   >   >> 💡 **Tip**: Start small (e.g., 500 epochs, 1 layer of 64 neurons), observe the results, then gradually increase.
                         > >> >>   >   >   >>
                         > >> >>   >   >   >> ---
                         > >> >>   >   >   >>
                         > >> >>   >   >   >> ## 📊 Example Results
                         > >> >>   >   >   >>
                         > >> >>   >   >   >> ### Impact of Epochs on Accuracy
                         > >> >>   >   >   >>
                         > >> >>   >   >   >> | Epochs | Average Error | Quality |
                         > >> >>   >   >   >> |--------|--------------|---------|
                         > >> >>   >   >   >> | 10     | ~150.0000    | Insufficient |
                         > >> >>   >   >   >> | 50     | ~25.0000     | Average |
                         > >> >>   >   >   >> | 100    | ~8.0000      | Good |
                         > >> >>   >   >   >> | 500    | ~0.5000      | Very Good |
                         > >> >>   >   >   >> | 1000   | ~0.0500      | Excellent |
                         > >> >>   >   >   >> | 3000   | ~0.0010      | Excellent |
                         > >> >>   >   >   >>
                         > >> >>   >   >   >> > ⚡ **Conclusion**: With 10 epochs, the AI makes huge errors. With 3000 epochs, it's nearly perfect!
                         > >> >>   >   >   >> >
                         > >> >>   >   >   >> > ---
                         > >> >>   >   >   >> >
                         > >> >>   >   >   >> > ## 🧩 How does it work?
                         > >> >>   >   >   >> >
                         > >> >>   >   >   >> > ### The Neural Network
                         > >> >>   >   >   >> >
                         > >> >>   >   >   >> > ```
                         > >> >>   >   >   >> > Input (x) → [Layer 1: N neurons] → [Layer 2: N neurons] → ... → Output (3x)
                         > >> >>   >   >   >> > ```
                         > >> >>   >   >   >> >
                         > >> >>   >   >   >> > 1. **Input**: A number (e.g., 7)
                         > >> >>   >   >   >> > 2. 2. **Hidden layers**: Process information with weights and biases
                         > >> >>   >   >   >> >    3. 3. **Output**: The triple prediction (e.g., 21.0003)
                         > >> >>   >   >   >> >       4. 4. **Loss**: The error between prediction and reality
                         > >> >>   >   >   >> >          5. 5. **Optimization**: The Adam algorithm adjusts weights to reduce the loss
                         > >> >>   >   >   >> >             6. 6. **Epochs**: Number of times the network sees all the data
                         > >> >>   >   >   >> >               
                         > >> >>   >   >   >> >                7. ### Why more epochs = more accuracy?
                         > >> >>   >   >   >> >               
                         > >> >>   >   >   >> >                8. At each epoch, the network slightly adjusts its weights to reduce error. It's like a student improving through practice:
                         > >> >>   >   >   >> >                9. - **10 epochs** = The student read the course once → poor results
                         > >> >>   >   >   >> >                   - - **1000 epochs** = The student practiced intensively → excellent results
                         > >> >>   >   >   >> > 
                         ---

                         ## 📁 Project Structure

                         ```
                         NeuroTriple-Lab/
                         ├── neurotriplelab.py       # Main script with all 5 features
                         ├── requirements.txt        # Python dependencies
                         ├── README.md               # This file
                         ├── LICENSE                 # MIT License
                         └── .gitignore              # Files ignored by Git
                         ```

                         ---

                         ## 🔧 Dependencies

                         | Package | Version | Role |
                         |---------|---------|------|
                         | TensorFlow | ≥ 2.10.0 | Deep learning framework (Keras) |
                         | NumPy | ≥ 1.21.0 | Numerical computations |
                         | Matplotlib | ≥ 3.5.0 | Graph generation |

                         ---

                         ## 📜 License

                         This project is licensed under the **MIT** License - see the [LICENSE](LICENSE) file for details.

                         ---

                         ## 🤝 Contributing

                         Contributions are welcome! Feel free to:
                         1. Fork the project
                         2. 2. Create a branch for your feature
                            3. 3. Commit your changes
                               4. 4. Push the branch
                                  5. 5. Open a Pull Request
                                    
                                     6. ---
                                    
                                     7. <p align="center">
                                       <strong>🧠 The more you train, the more accurate the AI becomes! 🎯</strong>
                                       </p>
