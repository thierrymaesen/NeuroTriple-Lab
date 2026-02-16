"""
=============================================================================
NeuroTriple-Lab - Laboratoire Pedagogique de Reseaux de Neurones
=============================================================================
Projet educatif demontrant l'impact de l'entrainement sur la precision
d'une IA. Le reseau de neurones apprend a tripler un nombre.

5 FONCTIONNALITES PEDAGOGIQUES :
1. Comparaison d'Epochs  - Voir l'impact du nombre d'epochs sur la precision
2. Architecture Variable - Tester differentes profondeurs de reseau
3. Visualisation        - Graphiques de la courbe d'apprentissage (loss)
4. Tableau de Precision  - Mesurer l'erreur sur un jeu de test
5. Mode Experimentation  - Lancer des experiences automatisees completes

Auteur : Projet pedagogique NeuroTriple-Lab
Licence : MIT
=============================================================================
"""

import numpy as np
import os
import sys

# ============================================================================
# Verification et installation automatique des dependances
# ============================================================================
try:
    import tensorflow as tf
    from tensorflow import keras
    from keras import Sequential
    from keras import layers
except ImportError:
    print("TensorFlow n'est pas installe.")
    print("Installez-le avec : pip install tensorflow")
    sys.exit(1)

try:
    import matplotlib
    matplotlib.use('Agg')  # Backend non-interactif par defaut
    import matplotlib.pyplot as plt
    MATPLOTLIB_DISPONIBLE = True
except ImportError:
    MATPLOTLIB_DISPONIBLE = False
    print("[INFO] matplotlib non installe. Les graphiques seront desactives.")
    print("       Installez-le avec : pip install matplotlib")


# ============================================================================
# DONNEES D'ENTRAINEMENT
# ============================================================================
# Le reseau doit apprendre la fonction f(x) = 3x
ENTREE = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
SORTIE = np.array([3, 6, 9, 12, 15, 18, 21, 24, 27, 30], dtype=float)  # Triple

# Jeu de test (jamais vu pendant l'entrainement)
TEST_ENTREE = np.array([11, 15, 20, 25, 50, 100], dtype=float)
TEST_SORTIE = np.array([33, 45, 60, 75, 150, 300], dtype=float)


# ============================================================================
# FONCTIONS UTILITAIRES
# ============================================================================

def afficher_banniere():
    """Affiche la banniere du programme."""
    print("\n" + "=" * 65)
    print("   _   _                    _____     _       _        ")
    print("  | \\ | | ___ _   _ _ __ __|_   _| __(_)_ __ | | ___  ")
    print("  |  \\| |/ _ \\ | | | '__/ _ \\| || '__| | '_ \\| |/ _ \\ ")
    print("  | |\\  |  __/ |_| | | | (_) | || |  | | |_) | |  __/ ")
    print("  |_| \\_|\\___|\\__,_|_|  \\___/|_||_|  |_| .__/|_|\\___| ")
    print("                                        |_| LAB        ")
    print("=" * 65)
    print("  Laboratoire Pedagogique - Impact de l'entrainement")
    print("  sur la precision d'un reseau de neurones")
    print("=" * 65)
    print("")
    print("  " + "!" * 61)
    print("  ! ATTENTION : Si votre ordinateur est peu puissant,       !")
    print("  ! ne mettez pas des valeurs trop elevees pour les epochs  !")
    print("  ! et les couches denses, sinon l'apprentissage sera       !")
    print("  ! tres long ! Commencez petit et augmentez graduellement. !")
    print("  " + "!" * 61)


def creer_modele(couches_cachees=None):
    """
    Cree un modele de reseau de neurones.

    Args:
    couches_cachees: Liste d'entiers definissant le nombre de neurones
    par couche cachee. Ex: [64] ou [128, 64, 32]
    Par defaut: [64]
    Returns:
    Modele Keras compile
    """
    if couches_cachees is None:
        couches_cachees = [64]

    model = Sequential()
    # Couche d'entree
    model.add(layers.Dense(units=couches_cachees[0], input_shape=[1], activation='relu'))

    # Couches cachees supplementaires
    for neurones in couches_cachees[1:]:
        model.add(layers.Dense(units=neurones, activation='relu'))

    # Couche de sortie (1 neurone pour la prediction)
    model.add(layers.Dense(units=1))

    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


def entrainer_modele(model, epochs=1000, verbose=0):
    """
    Entraine le modele et retourne l'historique.

    Args:
    model: Modele Keras a entrainer
    epochs: Nombre d'epochs d'entrainement
    verbose: Niveau d'affichage (0=silencieux, 1=barre, 2=detail)
    Returns:
    Historique d'entrainement (loss par epoch)
    """
    history = model.fit(
        x=ENTREE,
        y=SORTIE,
        epochs=epochs,
        verbose=verbose
    )
    return history


def evaluer_precision(model, nom="Modele"):
    """
    Evalue la precision du modele sur le jeu de test.

    Args:
    model: Modele entraine
    nom: Nom du modele pour l'affichage
    Returns:
    Erreur moyenne absolue
    """
    predictions = model.predict(TEST_ENTREE, verbose=0).flatten()
    erreurs = np.abs(predictions - TEST_SORTIE)
    erreur_moyenne = np.mean(erreurs)
    erreur_relative = np.mean(erreurs / TEST_SORTIE) * 100

    print(f"\n{'=' * 55}")
    print(f"  EVALUATION : {nom}")
    print(f"{'=' * 55}")
    print(f"  {'Entree':<10} {'Attendu':<10} {'Predit':<12} {'Erreur':<10}")
    print(f"  {'-' * 45}")

    for e, s, p, err in zip(TEST_ENTREE, TEST_SORTIE, predictions, erreurs):
        symbole = "OK" if err < 1 else "!!"
        print(f"  {e:<10.0f} {s:<10.0f} {p:<12.4f} {err:<10.4f} {symbole}")

    print(f"  {'-' * 45}")
    print(f"  Erreur moyenne absolue : {erreur_moyenne:.4f}")
    print(f"  Erreur relative moyenne : {erreur_relative:.2f}%")
    print(f"{'=' * 55}")

    return erreur_moyenne


# ============================================================================
# FONCTIONNALITE 1 : Comparaison d'Epochs
# ============================================================================
def comparer_epochs():
    """
    Compare la precision du modele avec differents nombres d'epochs.
    Demontre que plus on entraine, plus le modele est precis.
    """
    print("\n" + "#" * 65)
    print("#  FONCTIONNALITE 1 : Comparaison du nombre d'Epochs")
    print("#" * 65)
    print("\n  Cette experience montre l'impact du nombre d'iterations")
    print("  d'entrainement (epochs) sur la precision du modele.\n")

    liste_epochs = [10, 50, 100, 500, 1000, 3000]

    print("  Quels nombres d'epochs voulez-vous tester ?")
    print(f"  Par defaut : {liste_epochs}")
    choix = input("  Appuyez sur Entree pour les valeurs par defaut, ou entrez les votres (separes par des virgules) : ").strip()

    if choix:
        try:
            liste_epochs = [int(x.strip()) for x in choix.split(',')]
        except ValueError:
            print("  Valeurs invalides, utilisation des valeurs par defaut.")

    resultats = []
    historiques = []

    for epochs in liste_epochs:
        print(f"\n  >>> Entrainement avec {epochs} epochs...")
        model = creer_modele([64])
        history = entrainer_modele(model, epochs=epochs)
        erreur = evaluer_precision(model, f"{epochs} epochs")
        resultats.append((epochs, erreur))
        historiques.append((epochs, history.history['loss']))

    # Affichage du resume
    print("\n" + "=" * 55)
    print("  RESUME COMPARATIF - Impact des Epochs")
    print("=" * 55)
    print(f"  {'Epochs':<15} {'Erreur Moyenne':<20} {'Qualite'}")
    print(f"  {'-' * 50}")

    for epochs, erreur in resultats:
        if erreur < 0.1:
            qualite = "Excellent"
        elif erreur < 1:
            qualite = "Tres bon"
        elif erreur < 5:
            qualite = "Bon"
        elif erreur < 20:
            qualite = "Moyen"
        else:
            qualite = "Insuffisant"
        print(f"  {epochs:<15} {erreur:<20.4f} {qualite}")

    print(f"\n  CONCLUSION : Plus le nombre d'epochs augmente,")
    print(f"  plus l'erreur diminue et plus le modele est precis !")

    # Graphique
    if MATPLOTLIB_DISPONIBLE:
        sauvegarder_graphique_epochs(historiques, resultats)

    return resultats


def sauvegarder_graphique_epochs(historiques, resultats):
    """Sauvegarde le graphique de comparaison des epochs."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Graphique 1 : Courbes de loss
        for epochs, loss in historiques:
            ax1.plot(loss, label=f'{epochs} epochs')
            ax1.set_title('Courbe de Loss par nombre d\'Epochs')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss (Erreur)')
    ax1.set_yscale('log')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Graphique 2 : Erreur finale par epochs
    epochs_list = [r[0] for r in resultats]
    erreurs_list = [r[1] for r in resultats]
    ax2.bar(range(len(epochs_list)), erreurs_list, color='steelblue')
    ax2.set_xticks(range(len(epochs_list)))
    ax2.set_xticklabels([str(e) for e in epochs_list])
    ax2.set_title('Erreur moyenne selon le nombre d\'Epochs')
    ax2.set_xlabel('Nombre d\'Epochs')
    ax2.set_ylabel('Erreur Moyenne Absolue')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fichier = 'comparaison_epochs.png'
    plt.savefig(fichier, dpi=150)
    plt.close()
    print(f"\n  [GRAPHIQUE] Sauvegarde dans '{fichier}'")


# ============================================================================
# FONCTIONNALITE 2 : Architecture Variable (Couches intermediaires)
# ============================================================================
def comparer_architectures():
    """
    Compare differentes architectures de reseau (nombre et taille des couches).
    Demontre l'impact de la profondeur du reseau sur la precision.
    """
    print("\n" + "#" * 65)
    print("#  FONCTIONNALITE 2 : Comparaison des Architectures")
    print("#" * 65)
    print("\n  Cette experience montre l'impact du nombre de couches")
    print("  intermediaires et de neurones sur la precision.\n")

    architectures = {
        "Simple (1 couche, 8 neurones)": [8],
        "Moyenne (1 couche, 64 neurones)": [64],
        "Profonde (3 couches: 128-64-32)": [128, 64, 32],
        "Tres profonde (5 couches: 256-128-64-32-16)": [256, 128, 64, 32, 16],
        "Large (1 couche, 256 neurones)": [256],
    }

    epochs = 1000
    print(f"  Nombre d'epochs fixe : {epochs}")
    choix_epochs = input(f"  Appuyez sur Entree pour garder {epochs}, ou entrez une autre valeur : ").strip()
    if choix_epochs:
        try:
            epochs = int(choix_epochs)
        except ValueError:
            print("  Valeur invalide, utilisation de 1000 epochs.")

    resultats = []

    for nom, couches in architectures.items():
        print(f"\n  >>> Test de l'architecture : {nom}")
        nb_params = None
        model = creer_modele(couches)
        nb_params = model.count_params()
        entrainer_modele(model, epochs=epochs)
        erreur = evaluer_precision(model, nom)
        resultats.append((nom, couches, erreur, nb_params))

    # Resume
    print("\n" + "=" * 70)
    print("  RESUME COMPARATIF - Impact de l'Architecture")
    print("=" * 70)
    print(f"  {'Architecture':<45} {'Params':<10} {'Erreur'}")
    print(f"  {'-' * 65}")

    for nom, couches, erreur, params in resultats:
        print(f"  {nom:<45} {params:<10} {erreur:.4f}")

    print(f"\n  CONCLUSION : La profondeur et la largeur du reseau")
    print(f"  influencent la capacite d'apprentissage du modele !")

    # Graphique
    if MATPLOTLIB_DISPONIBLE:
        sauvegarder_graphique_architectures(resultats)

    return resultats


def sauvegarder_graphique_architectures(resultats):
    """Sauvegarde le graphique de comparaison des architectures."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    noms = [r[0][:20] + "..." if len(r[0]) > 20 else r[0] for r in resultats]
    erreurs = [r[2] for r in resultats]
    params = [r[3] for r in resultats]

    colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(resultats)))

    ax1.barh(range(len(noms)), erreurs, color=colors)
    ax1.set_yticks(range(len(noms)))
    ax1.set_yticklabels(noms, fontsize=8)
    ax1.set_title('Erreur par Architecture')
    ax1.set_xlabel('Erreur Moyenne Absolue')
    ax1.grid(True, alpha=0.3)

    ax2.bar(range(len(noms)), params, color=colors)
    ax2.set_xticks(range(len(noms)))
    ax2.set_xticklabels(noms, rotation=45, ha='right', fontsize=7)
    ax2.set_title('Nombre de Parametres par Architecture')
    ax2.set_ylabel('Nombre de parametres')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fichier = 'comparaison_architectures.png'
    plt.savefig(fichier, dpi=150)
    plt.close()
    print(f"\n  [GRAPHIQUE] Sauvegarde dans '{fichier}'")


# ============================================================================
# FONCTIONNALITE 3 : Visualisation de la Courbe d'Apprentissage
# ============================================================================
def visualiser_apprentissage():
    """
    Entraine un modele et affiche la courbe d'apprentissage en detail.
    Montre comment la loss diminue au fil des epochs.
    """
    print("\n" + "#" * 65)
    print("#  FONCTIONNALITE 3 : Visualisation de l'Apprentissage")
    print("#" * 65)
    print("\n  Cette experience montre en detail comment le modele")
    print("  apprend progressivement en reduisant son erreur.\n")

    epochs = 2000
    choix = input(f"  Nombre d'epochs (defaut={epochs}) : ").strip()
    if choix:
        try:
            epochs = int(choix)
        except ValueError:
            pass

    print(f"\n  Entrainement en cours ({epochs} epochs)...")
    model = creer_modele([128, 64])
    history = entrainer_modele(model, epochs=epochs, verbose=0)

    loss = history.history['loss']

    # Affichage textuel de la progression
    print(f"\n  PROGRESSION DE L'APPRENTISSAGE :")
    print(f"  {'-' * 50}")
    etapes = [0, int(epochs*0.1), int(epochs*0.25), int(epochs*0.5), int(epochs*0.75), epochs-1]
    for i in etapes:
        if i < len(loss):
            barre = "#" * min(int(loss[i] * 2), 30)
            print(f"  Epoch {i+1:>6}/{epochs} | Loss: {loss[i]:>10.4f} | {barre}")

    print(f"\n  Loss initiale  : {loss[0]:.4f}")
    print(f"  Loss finale    : {loss[-1]:.6f}")
    print(f"  Amelioration   : {((loss[0] - loss[-1]) / loss[0] * 100):.2f}%")

    evaluer_precision(model, f"Modele ({epochs} epochs)")

    if MATPLOTLIB_DISPONIBLE:
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))

        # Graphique 1 : Loss complete
        axes[0].plot(loss, color='blue', linewidth=0.5)
        axes[0].set_title('Courbe de Loss Complete')
        axes[0].set_xlabel('Epoch')
        axes[0].set_ylabel('Loss')
        axes[0].grid(True, alpha=0.3)

        # Graphique 2 : Loss en echelle log
        axes[1].plot(loss, color='red', linewidth=0.5)
        axes[1].set_yscale('log')
        axes[1].set_title('Courbe de Loss (echelle logarithmique)')
        axes[1].set_xlabel('Epoch')
        axes[1].set_ylabel('Loss (log)')
        axes[1].grid(True, alpha=0.3)

        # Graphique 3 : Predictions vs Realite
        x_test = np.linspace(0, 110, 100)
        y_pred = model.predict(x_test, verbose=0).flatten()
        y_reel = x_test * 3

        axes[2].plot(x_test, y_reel, 'g--', label='Reel (f(x)=3x)', linewidth=2)
        axes[2].plot(x_test, y_pred, 'b-', label='Prediction IA', linewidth=1.5)
        axes[2].scatter(ENTREE, SORTIE, color='red', zorder=5, label='Donnees entrainement')
        axes[2].set_title('Predictions vs Realite')
        axes[2].set_xlabel('Entree (x)')
        axes[2].set_ylabel('Sortie (3x)')
        axes[2].legend()
        axes[2].grid(True, alpha=0.3)

        plt.tight_layout()
        fichier = 'visualisation_apprentissage.png'
        plt.savefig(fichier, dpi=150)
        plt.close()
        print(f"\n  [GRAPHIQUE] Sauvegarde dans '{fichier}'")


# ============================================================================
# FONCTIONNALITE 4 : Tableau de Precision Detaille
# ============================================================================
def tableau_precision():
    """
    Entraine plusieurs modeles et produit un tableau comparatif
    detaille de la precision, incluant le temps d'entrainement.
    """
    print("\n" + "#" * 65)
    print("#  FONCTIONNALITE 4 : Tableau de Precision Detaille")
    print("#" * 65)
    print("\n  Cette experience mesure la precision de maniere detaillee")
    print("  en combinant differents epochs ET architectures.\n")

    import time

    configurations = [
        ("Basique - 100 epochs",      [64],            100),
        ("Basique - 500 epochs",      [64],            500),
        ("Basique - 2000 epochs",     [64],            2000),
        ("Profond - 100 epochs",      [128, 64, 32],   100),
        ("Profond - 500 epochs",      [128, 64, 32],   500),
        ("Profond - 2000 epochs",     [128, 64, 32],   2000),
    ]

    resultats = []
    print(f"  {'Configuration':<30} {'Epochs':<10} {'Temps':<10} {'Erreur':<12} {'Statut'}")
    print(f"  {'-' * 75}")

    for nom, couches, epochs in configurations:
        debut = time.time()
        model = creer_modele(couches)
        entrainer_modele(model, epochs=epochs)
        duree = time.time() - debut

        predictions = model.predict(TEST_ENTREE, verbose=0).flatten()
        erreur = np.mean(np.abs(predictions - TEST_SORTIE))
        erreur_pct = np.mean(np.abs(predictions - TEST_SORTIE) / TEST_SORTIE) * 100

        if erreur < 0.5:
            statut = "EXCELLENT"
        elif erreur < 2:
            statut = "TRES BON"
        elif erreur < 10:
            statut = "BON"
        else:
            statut = "A AMELIORER"

        resultats.append((nom, epochs, duree, erreur, erreur_pct, statut))
        print(f"  {nom:<30} {epochs:<10} {duree:<10.2f}s {erreur:<12.4f} {statut}")

    print(f"\n  {'=' * 75}")
    print(f"  CONCLUSION :")
    meilleur = min(resultats, key=lambda x: x[3])
    print(f"  Meilleure configuration : {meilleur[0]}")
    print(f"  Avec une erreur de seulement {meilleur[3]:.4f}")
    print(f"  L'entrainement plus long + architecture adaptee = meilleure precision !")


# ============================================================================
# FONCTIONNALITE 5 : Mode Experimentation Automatisee
# ============================================================================
def mode_experimentation():
    """
    Lance une experience automatisee complete qui teste systematiquement
    de nombreuses combinaisons et genere un rapport complet.
    """
    print("\n" + "#" * 65)
    print("#  FONCTIONNALITE 5 : Mode Experimentation Automatisee")
    print("#" * 65)
    print("\n  Cette experience lance une batterie de tests automatiques")
    print("  pour trouver la meilleure configuration possible.\n")

    import time

    liste_epochs = [100, 500, 1000, 2000]
    liste_architectures = {
        "Minimal": [16],
        "Standard": [64],
        "Double": [64, 32],
        "Profond": [128, 64, 32],
    }

    total_tests = len(liste_epochs) * len(liste_architectures)
    print(f"  Nombre total de tests : {total_tests}")
    print(f"  Lancement de l'experimentation...\n")

    tous_resultats = []
    compteur = 0

    for nom_archi, couches in liste_architectures.items():
        for epochs in liste_epochs:
            compteur += 1
            print(f"  [{compteur}/{total_tests}] {nom_archi} x {epochs} epochs...", end=" ")

            debut = time.time()
            model = creer_modele(couches)
            history = entrainer_modele(model, epochs=epochs)
            duree = time.time() - debut

            predictions = model.predict(TEST_ENTREE, verbose=0).flatten()
            erreur = np.mean(np.abs(predictions - TEST_SORTIE))
            loss_finale = history.history['loss'][-1]

            tous_resultats.append({
                'architecture': nom_archi,
                'couches': str(couches),
                'epochs': epochs,
                'erreur': erreur,
                'loss': loss_finale,
                'duree': duree,
                'predictions': predictions
            })

            symbole = "OK" if erreur < 1 else "!!"
            print(f"Erreur: {erreur:.4f} [{symbole}] ({duree:.1f}s)")

    # Classement
    tous_resultats.sort(key=lambda x: x['erreur'])

    print(f"\n{'=' * 70}")
    print(f"  CLASSEMENT FINAL - Du meilleur au moins bon")
    print(f"{'=' * 70}")
    print(f"  {'Rang':<6} {'Architecture':<15} {'Epochs':<10} {'Erreur':<12} {'Loss':<12} {'Temps'}")
    print(f"  {'-' * 65}")

    for i, r in enumerate(tous_resultats):
        medaille = ["1er", "2eme", "3eme"][i] if i < 3 else f"{i+1}eme"
        print(f"  {medaille:<6} {r['architecture']:<15} {r['epochs']:<10} {r['erreur']:<12.4f} {r['loss']:<12.6f} {r['duree']:.1f}s")

    # Meilleur resultat
    best = tous_resultats[0]
    print(f"\n  CHAMPION : {best['architecture']} avec {best['epochs']} epochs")
    print(f"  Erreur : {best['erreur']:.4f} | Loss : {best['loss']:.6f}")

    print(f"\n  LECON APPRISE :")
    print(f"  Plus on entraine le reseau (epochs eleves) et plus")
    print(f"  l'architecture est adaptee, meilleure est la precision !")

    # Graphique recapitulatif
    if MATPLOTLIB_DISPONIBLE:
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Heatmap-like : erreur par architecture et epochs
        for nom_archi in liste_architectures:
            erreurs = [r['erreur'] for r in tous_resultats if r['architecture'] == nom_archi]
            epochs_vals = [r['epochs'] for r in tous_resultats if r['architecture'] == nom_archi]
            axes[0].plot(epochs_vals, erreurs, 'o-', label=nom_archi, linewidth=2, markersize=8)

        axes[0].set_title('Erreur par Architecture et Epochs')
        axes[0].set_xlabel('Nombre d\'Epochs')
        axes[0].set_ylabel('Erreur Moyenne Absolue')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        axes[0].set_yscale('log')

        # Top 5 barres
        top5 = tous_resultats[:5]
        noms = [f"{r['architecture']}\n{r['epochs']}ep" for r in top5]
        erreurs = [r['erreur'] for r in top5]
        colors = ['gold', 'silver', '#CD7F32', 'steelblue', 'steelblue']
        axes[1].bar(range(len(noms)), erreurs, color=colors[:len(noms)])
        axes[1].set_xticks(range(len(noms)))
        axes[1].set_xticklabels(noms, fontsize=8)
        axes[1].set_title('Top 5 Meilleures Configurations')
        axes[1].set_ylabel('Erreur Moyenne Absolue')
        axes[1].grid(True, alpha=0.3)

        plt.tight_layout()
        fichier = 'experimentation_complete.png'
        plt.savefig(fichier, dpi=150)
        plt.close()
        print(f"\n  [GRAPHIQUE] Sauvegarde dans '{fichier}'")


# ============================================================================
# MODE INTERACTIF (Code original ameliore)
# ============================================================================
def mode_interactif():
    """
    Mode interactif : l'utilisateur entre un nombre et voit la prediction.
    Version amelioree du code original.
    """
    print("\n" + "#" * 65)
    print("#  MODE INTERACTIF - Testez le modele entraine !")
    print("#" * 65)

    epochs = 1000
    choix = input(f"\n  Nombre d'epochs pour l'entrainement (defaut={epochs}) : ").strip()
    if choix:
        try:
            epochs = int(choix)
        except ValueError:
            pass

    print(f"\n  Entrainement du modele avec {epochs} epochs...")
    model = creer_modele([128, 64])
    entrainer_modele(model, epochs=epochs, verbose=1)
    evaluer_precision(model, f"Modele interactif ({epochs} epochs)")

    print("\n  Le modele est pret ! Entrez un nombre pour voir sa prediction.")
    print("  (Tapez 'q' pour quitter)\n")

    while True:
        entree = input("  Nombre : ").strip()
        if entree.lower() == 'q':
            print("\n  Au revoir !")
            break
        try:
            x = float(entree)
            prediction = model.predict(np.array([x]), verbose=0)[0][0]
            attendu = x * 3
            erreur = abs(prediction - attendu)
            print(f"  Prediction IA : {prediction:.4f}")
            print(f"  Valeur exacte : {attendu:.1f}")
            print(f"  Erreur        : {erreur:.4f}")
            print()
        except ValueError:
            print("  Veuillez entrer un nombre valide.\n")


# ============================================================================
# MENU PRINCIPAL
# ============================================================================
def menu_principal():
    """Menu principal interactif du programme."""
    afficher_banniere()

    while True:
        print("\n  MENU PRINCIPAL")
        print("  " + "-" * 40)
        print("  1. Comparer differents nombres d'Epochs")
        print("  2. Comparer differentes Architectures")
        print("  3. Visualiser l'Apprentissage")
        print("  4. Tableau de Precision Detaille")
        print("  5. Mode Experimentation Automatisee")
        print("  6. Mode Interactif (tester le modele)")
        print("  0. Quitter")
        print("  " + "-" * 40)
        print("  [!] PC lent ? Evitez epochs > 5000")
        print("      et architectures trop profondes")

        choix = input("  Votre choix : ").strip()

        if choix == '1':
            comparer_epochs()
        elif choix == '2':
            comparer_architectures()
        elif choix == '3':
            visualiser_apprentissage()
        elif choix == '4':
            tableau_precision()
        elif choix == '5':
            mode_experimentation()
        elif choix == '6':
            mode_interactif()
        elif choix == '0':
            print("\n  Merci d'avoir utilise NeuroTriple-Lab !")
            print("  N'oubliez pas : plus on entraine, plus l'IA est precise !\n")
            break
        else:
            print("  Choix invalide. Veuillez reessayer.")


# ============================================================================
# POINT D'ENTREE
# ============================================================================
if __name__ == "__main__":
    menu_principal()
