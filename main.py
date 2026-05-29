# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 09:50:57 2025

@author: JDION
"""

import numpy as np
import matplotlib.pyplot as plt
from simulateur import SimulateurTraitement
from strategies_gp10 import StrategieAleatoire, StrategieCyclique, MaStrategie

def simulation(strategie, simulateur):
    """
    Exécute une simulation complète d'une stratégie sur un simulateur
    """
    N = simulateur.n_patients
    K = simulateur.n_traitements
    mapping = {i: chr(65+i) for i in range(K)}
    X = np.zeros(N)
    strategie.initialiser()
    for n in range(N):
        t = strategie.choisir_traitement()
        x = simulateur.administrer_traitement(mapping[t])
        strategie.mettre_a_jour(t, x)
        X[n] = x
    return X

def affiche_resultats(X, noms):
    """
    Affiche les courbes cumulées de patients guéris pour chaque stratégie.
    """
    plt.figure()
    for i, nom in enumerate(noms):
        plt.plot(np.cumsum(X[i]), label=nom)
    plt.legend()
    plt.xlabel("Patients")
    plt.ylabel("Nombre cumulé de guérisons")
    plt.title("Cumul de patients guéris")
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    repetitions = 5 # changé pour l'évaluation
    seed = 2025 # changé pour l'évaluation
    seeds = range(seed, seed + repetitions)
    
    sim_tmp = SimulateurTraitement(seed)
    N = sim_tmp.n_patients
    K = sim_tmp.n_traitements

    strategies = [
        StrategieAleatoire(K),
        StrategieCyclique(K),
        MaStrategie(K)
    ]
    noms = ["Stratégie aléatoire", "Stratégie cyclique", "Stratégie bayésienne"]
    
    X = np.zeros((len(noms), N))

    for s in seeds:
        for i, strat in enumerate(strategies):
            sim = SimulateurTraitement(seed=s)
            X[i] += simulation(strat, sim)

    X /= len(seeds)

    affiche_resultats(X, noms)
    for i, nom in enumerate(noms):
        score = np.sum(X[i])
        print(f"{nom} : {score:.1f} / {N} patients guéris en moyenne")

        # Strategie 1 et 2
        # Calcul l'esperance et la variance des strategie
        esperance = np.mean(X[i])
        variance = np.var(X[i])
        print(f"esperance {nom} = {esperance}\nvariance {nom} = {variance}\n")



        # Strategie 3
        if nom == "Stratégie cyclique":
            # Extract first 30 results for each treatment (every K-th element starting from position j)
            x_A = X[i][0:30*K:K]
            x_B = X[i][1:30*K:K]
            x_C = X[i][2:30*K:K]
            x_D = X[i][3:30*K:K]
            x_E = X[i][4:30*K:K]
            
            list_x = [x_A, x_B, x_C, x_D, x_E]
            for j, x in enumerate(list_x):
                print(f"esperance {nom} traitement {chr(65+j)} = {np.mean(x)}\nvariance {nom} traitement {chr(65+j)} = {np.var(x)}\n")

        
        # Strategie 4
        if nom == "Stratégie bayésienne":
            print("\nAnalyse par traitement de la stratégie bayésienne :\n")

            # Récupère l'historique de la dernière simulation
            sim = SimulateurTraitement(seed=seed + repetitions - 1)
            strat = MaStrategie(K)
            simulation(strat, sim)

            # Analyse chaque traitement
            for t in range(K):
                indices = np.where(np.array(strat.historique_traitements) == t)[0]
                resultats_t = np.array(strat.historique_resultats)[indices]

                if len(resultats_t) > 0:
                    taux_succes = np.mean(resultats_t)
                    nb_fois = len(resultats_t)
                    print(f"Traitement {chr(65+t)} : {taux_succes:.2%} ({int(np.sum(resultats_t))}/{nb_fois})")
            