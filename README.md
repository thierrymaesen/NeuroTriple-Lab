<div align="center">

**FR** [Version francaise](#french) | **GB** [English version](#english)

</div>

---

<a name="french"></a>

# 🧠 NeuroTriple-Lab

> **Laboratoire Pedagogique de Reseaux de Neurones**
> Demontrer que plus on entraine une IA, plus elle est precise dans ses reponses.

---

## 🌐 Demo en Ligne (Live Demo)

**[▶ Lancer la Demo Interactive](https://thierrymaesen.github.io/NeuroTriple-Lab/)**

> L interface web fonctionne directement dans votre navigateur — aucune installation requise !
> Le reseau de neurones s entraine en temps reel sous vos yeux grace a TensorFlow.js.

---

## 📋 Description

**NeuroTriple-Lab** est un projet educatif interactif qui utilise un reseau de neurones simple pour apprendre la fonction mathematique `f(x) = 3x` (tripler un nombre).

Le but principal est de demontrer de maniere **visuelle et mesurable** que :

- ✅ Plus on augmente le nombre d **epochs** (iterations d entrainement), plus le modele est precis
- ✅ Plus on ajoute de **couches intermediaires** (profondeur du reseau), plus le modele peut apprendre efficacement
- ✅ L **architecture** et la **duree d entrainement** sont des facteurs cles de la performance d une IA

## 🎯 Concept de Base

Le code est simple : un reseau de neurones recoit des nombres en entree et doit apprendre a predire leur triple.

```python
# Donnees d entrainement
entree = [1, 2, 3, 4, 5]   # Nombres en entree
sortie = [3, 6, 9, 12, 15]  # Le triple (resultat attendu)
```

Le reseau n a aucune connaissance prealable de la multiplication. Il apprend uniquement a partir des exemples fournis, en ajustant ses poids internes a chaque epoch.

---

## 🖥️ Deux Versions Disponibles

### 🌐 Version Web Interactive (NOUVEAU)

L interface web offre une experience visuelle complete directement dans le navigateur :

- **🧠 Animation en temps reel** : Visualisation du reseau de neurones avec les neurones qui s activent et les connexions qui changent de couleur pendant l entrainement
- **📈 Graphique de loss en direct** : La courbe d erreur descend sous vos yeux
- **📊 Comparaison d epochs** : Testez differents nombres d epochs et comparez les resultats
- **🏗️ Comparaison d architectures** : Testez differentes profondeurs de reseau
- **🎮 Mode interactif** : Entrez un nombre et voyez la prediction de l IA
- **🌍 Bilingue FR/EN** : Basculez entre francais et anglais d un clic
- **✨ Particules animees** : Fond anime style "laboratoire neuronal"

**Technologies** : TensorFlow.js, Chart.js, Canvas HTML5 — tout tourne dans le navigateur !

### 💻 Version Terminal (Python)

La version originale en Python avec TensorFlow/Keras offre 5 fonctionnalites pedagogiques via un menu interactif en terminal.

---

## 🚀 Installation (Version Python)

### Prerequis
- Python 3.8 ou superieur
- pip (gestionnaire de paquets Python)

### Etapes

```bash
# 1. Cloner le depot
git clone https://github.com/thierrymaesen/NeuroTriple-Lab.git

# 2. Acceder au dossier
cd NeuroTriple-Lab

# 3. Installer les dependances
pip install -r requirements.txt

# 4. Lancer le programme
python neurotriplelab.py
```

---

## ⚠️ ATTENTION — Performance et temps de calcul

Le Deep Learning est tres gourmand en ressources. Commencez petit (500 epochs, 1 couche de 64 neurones) et augmentez graduellement.

---

## 📊 Exemples de Resultats

| Epochs | Erreur Moyenne | Qualite |
|--------|---------------|---------|
| 10     | ~150.0000     | Insuffisant |
| 50     | ~25.0000      | Moyen |
| 100    | ~8.0000       | Bon |
| 500    | ~0.5000       | Tres bon |
| 1000   | ~0.0500       | Excellent |
| 3000   | ~0.0010       | Excellent |

**Conclusion** : Avec 10 epochs l IA se trompe enormement. Avec 3000 epochs, elle est quasi parfaite !

---

## 🧩 Comment ca marche ?

```
Entree (x) → [Couche 1: N neurones] → [Couche 2: N neurones] → ... → Sortie (3x)
```

A chaque epoch, le reseau ajuste legerement ses poids pour reduire l erreur. C est comme un eleve qui s ameliore en pratiquant.

---

## 📁 Structure du Projet

```
NeuroTriple-Lab/
├── index.html          # Interface web interactive (TensorFlow.js)
├── neurotriplelab.py   # Script Python avec les 5 fonctionnalites
├── requirements.txt    # Dependances Python
├── README.md           # Ce fichier
├── LICENSE             # Licence MIT
└── .gitignore          # Fichiers ignores par Git
```

## 🔧 Dependances

| Package | Version | Role |
|---------|---------|------|
| TensorFlow | >= 2.10.0 | Framework de deep learning (Keras) |
| NumPy | >= 1.21.0 | Calculs numeriques |
| Matplotlib | >= 3.5.0 | Generation des graphiques |
| TensorFlow.js | CDN | Reseau de neurones dans le navigateur |
| Chart.js | CDN | Graphiques dynamiques web |

## 📜 Licence

Ce projet est sous licence **MIT** - voir le fichier [LICENSE](LICENSE) pour plus de details.

## 🤝 Contribuer

Les contributions sont les bienvenues ! N hesitez pas a Fork le projet, creer une branche, commiter vos changements et ouvrir une Pull Request.

> 🧠 **Plus on entraine, plus l IA est precise !** 🎯

---
---

<a name="english"></a>

# 🧠 NeuroTriple-Lab

> **Educational Neural Network Laboratory**
> Demonstrating that the more you train an AI, the more accurate it becomes.

---

## 🌐 Live Demo

**[▶ Launch Interactive Demo](https://thierrymaesen.github.io/NeuroTriple-Lab/)**

> The web interface runs directly in your browser — no installation required!
> The neural network trains in real-time before your eyes thanks to TensorFlow.js.

---

## 📋 Description

**NeuroTriple-Lab** is an interactive educational project that uses a simple neural network to learn the mathematical function `f(x) = 3x` (tripling a number).

The main goal is to visually and measurably demonstrate that:

- ✅ The more you increase the number of **epochs** (training iterations), the more accurate the model becomes
- ✅ The more **intermediate layers** you add (network depth), the more efficiently the model can learn
- ✅ **Architecture** and **training duration** are key factors in AI performance

## 🎯 Core Concept

The code is simple: a neural network receives numbers as input and must learn to predict their triple.

```python
# Training data
input_data = [1, 2, 3, 4, 5]    # Input numbers
output_data = [3, 6, 9, 12, 15]  # The triple (expected result)
```

The network has no prior knowledge of multiplication. It learns solely from the provided examples, adjusting its internal weights at each epoch.

---

## 🖥️ Two Versions Available

### 🌐 Interactive Web Version (NEW)

The web interface offers a complete visual experience directly in your browser:

- **🧠 Real-time animation**: Neural network visualization with neurons activating and connections changing color during training
- **📈 Live loss chart**: Watch the error curve drop before your eyes
- **📊 Epoch comparison**: Test different epoch counts and compare results
- **🏗️ Architecture comparison**: Test different network depths
- **🎮 Interactive mode**: Enter a number and see the AI prediction
- **🌍 Bilingual FR/EN**: Switch between French and English with one click
- **✨ Animated particles**: Animated background "neural lab" style

**Technologies**: TensorFlow.js, Chart.js, HTML5 Canvas — everything runs in the browser!

### 💻 Terminal Version (Python)

The original Python version with TensorFlow/Keras offers 5 educational features via an interactive terminal menu.

---

## 🚀 Installation (Python Version)

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

## ⚠️ WARNING — Performance and computation time

Deep Learning is very resource-intensive. Start small (500 epochs, 1 layer of 64 neurons) and gradually increase.

---

## 📊 Example Results

| Epochs | Average Error | Quality |
|--------|--------------|---------|
| 10     | ~150.0000    | Poor |
| 50     | ~25.0000     | Average |
| 100    | ~8.0000      | Good |
| 500    | ~0.5000      | Very Good |
| 1000   | ~0.0500      | Excellent |
| 3000   | ~0.0010      | Excellent |

**Conclusion**: With 10 epochs, the AI makes huge errors. With 3000 epochs, it is nearly perfect!

---

## 🧩 How does it work?

```
Input (x) → [Layer 1: N neurons] → [Layer 2: N neurons] → ... → Output (3x)
```

At each epoch, the network slightly adjusts its weights to reduce error. It is like a student improving through practice.

---

## 📁 Project Structure

```
NeuroTriple-Lab/
├── index.html          # Interactive web interface (TensorFlow.js)
├── neurotriplelab.py   # Python script with all 5 features
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── LICENSE             # MIT License
└── .gitignore          # Files ignored by Git
```

## 🔧 Dependencies

| Package | Version | Role |
|---------|---------|------|
| TensorFlow | >= 2.10.0 | Deep learning framework (Keras) |
| NumPy | >= 1.21.0 | Numerical computations |
| Matplotlib | >= 3.5.0 | Graph generation |
| TensorFlow.js | CDN | Neural network in the browser |
| Chart.js | CDN | Dynamic web charts |

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to Fork the project, create a branch, commit your changes and open a Pull Request.

> 🧠 **The more you train, the more accurate the AI becomes!** 🎯
